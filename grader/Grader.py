#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

import gflags, httplib2, logging, os, sys, re, time, datetime, traceback
import apiclient.discovery
import oauth2client.file, oauth2client.client, oauth2client.tools
import importlib, oauth2, httplib2
from GraderReport import *
from campusvirtual import autenticar_campusvirtual
from xml.etree import ElementTree as etree
import hashlib, base64, urllib, hmac
from blist import sorteddict

# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>
CLIENT_SECRETS = 'client_secrets.json'

# Helpful message to display in the browser if the CLIENT_SECRETS file
# is missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the APIs Console <https://code.google.com/apis/console>.

""" % os.path.join(os.path.dirname(__file__), CLIENT_SECRETS)

FLAGS = gflags.FLAGS

def initialize():
    print 'Initializing'
    if not re.match('^/', FLAGS.logfile):
        ensure_dir(FLAGS.local, silent=True)
        FLAGS.logfile = os.path.join(FLAGS.local, FLAGS.logfile)
    global LOG_FILE
    LOG_FILE = open(FLAGS.logfile, 'w+')
    logging.getLogger().setLevel(getattr(logging, FLAGS.logging_level))


def update_all_grades():
    headers = autenticar_campusvirtual(FLAGS.user, FLAGS.password)
    for dirpath, subdirs, files in os.walk(FLAGS.local):
        update_directory_grades(dirpath, files, headers)


def update_directory_grades(dirpath, files, headers):
    for f in files:
        if not f.endswith('.log') and not f.endswith('.desc'):
            update_file_grade(dirpath, f, headers)


def update_file_grade(dirpath, file, headers):
    # Get report, Find grade
    # Find outcome url and sourcedid

    desc = open(os.path.join(dirpath, file + '.desc'), 'r')
    sourcedid = desc.read()
    desc.close()

    dirdesc = open(os.path.join(dirpath, '.desc'), 'r')
    url = dirdesc.read()
    dirdesc.close()

    reportpath = dirpath.replace(FLAGS.local, FLAGS.reportdir, 1)
    rpt = open(os.path.join(reportpath, file), 'r')
    grade = rpt.readlines()[-1].split(': ')[-1][:-1]
    rpt.close()

    if not lti_post_grade(url, grade, sourcedid, headers):
        print 'Error posting grade %s to %s' % (grade, url)


message_id = 1234
http = httplib2.Http
normalize = http._normalize_headers

def my_normalize(self, headers):
    ret = normalize(self, headers)
    for i in ret:
        key = i[0].upper()+i[1:]
        ret[key] = ret.pop(i)
    return ret

http._normalize_headers = my_normalize

campusvirtual_hostnames = [ 'fmoodle2%d'%i for i in range(1,7) ]

class SignatureMethod_CampusVirtual(oauth2.SignatureMethod_HMAC_SHA1):
    def signing_base(self, request, consumer, token):
        if not hasattr(request, 'normalized_url') or request.normalized_url is None:
            raise ValueError("Base URL for request is not set.")

        url = request.normalized_url
        url = url.replace('https', 'http')
        print 'Signing %s request with url %s' % (request.method, url)

        sig = (
            oauth2.escape(request.method),
            oauth2.escape(url),
            oauth2.escape(request.get_normalized_parameters()),
        )

        key = '%s&' % oauth2.escape(consumer.secret)
        if token:
            key += oauth2.escape(token.secret)
        raw = '&'.join(sig)
        return key, raw

    current_host = 0

    def get_hostname(self):
        return campusvirtual_hostnames[self.current_host]

    def next_hostname(self):
        self.current_host += 1
        self.current_host %= len(campusvirtual_hostnames)


def lti_post_grade(url, grade, lis_result_sourcedid, headers):
    print 'Posting %s to %s' % (grade, lis_result_sourcedid)
    global message_id
    message_identifier_id = str(message_id)
    message_id +=1
    score = float(grade)
    if score < 0. or score > 1.0:
        return False
    xml = generate_request_xml(message_identifier_id,
                               'replaceResult',
                               lis_result_sourcedid,
                               score)
    headers['Content-Type'] = 'application/xml'
    consumer = oauth2.Consumer(key="clave", secret="shared")
    client = oauth2.Client(consumer)
    client.set_signature_method(SignatureMethod_CampusVirtual())

    for i in range(6):
        resp, content = client.request(url,
                                       'POST',
                                       body=xml, headers=headers)
        if resp['status'] == '200':
            print 'Success!', client.method.current_host
            return True

        print 'Failed with status', resp['status']
        #print content
        client.method.next_hostname()
    # print 'HEADERS:', headers
    # print 'BODY:', xml
    # print 'RESPONSE:', resp
    # print 'CONTENT:', content
    return False


def generate_request_xml(message_identifier_id, operation,
                         lis_result_sourcedid, score):
    # pylint: disable=too-many-locals
    """
    Generates LTI 1.1 XML for posting result to LTI consumer.

    :param message_identifier_id:
    :param operation:
    :param lis_result_sourcedid:
    :param score:
    :return: XML string
    """
    root = etree.Element('imsx_POXEnvelopeRequest',
                         xmlns='http://www.imsglobal.org/services/'
                               'ltiv1p1/xsd/imsoms_v1p0')

    header = etree.SubElement(root, 'imsx_POXHeader')
    header_info = etree.SubElement(header, 'imsx_POXRequestHeaderInfo')
    version = etree.SubElement(header_info, 'imsx_version')
    version.text = 'V1.0'
    message_identifier = etree.SubElement(header_info,
                                          'imsx_messageIdentifier')
    message_identifier.text = message_identifier_id
    body = etree.SubElement(root, 'imsx_POXBody')
    xml_request = etree.SubElement(body, '%s%s' % (operation, 'Request'))
    record = etree.SubElement(xml_request, 'resultRecord')

    guid = etree.SubElement(record, 'sourcedGUID')

    sourcedid = etree.SubElement(guid, 'sourcedId')
    sourcedid.text = lis_result_sourcedid
    if score is not None:
        result = etree.SubElement(record, 'result')
        result_score = etree.SubElement(result, 'resultScore')
        language = etree.SubElement(result_score, 'language')
        language.text = 'en'
        text_string = etree.SubElement(result_score, 'textString')
        text_string.text = score.__str__()
    ret = "<?xml version='1.0' encoding='utf-8'?>\n{}".format(
        etree.tostring(root, encoding='utf-8'))
    return ret


def evaluate_all_assignments():
    for dirpath, subdirs, files in os.walk(FLAGS.local):
        evaluate_directory(dirpath, files)


def evaluate_directory(dirpath, files):
    for f in files:
        if not f.endswith('.log') and not f.endswith('.desc'):
            evaluate_file(dirpath, f)


def evaluate_file(dirpath, filename):
    f = os.path.join(dirpath, filename)
    report = FLAGS.reportdir + f[len(FLAGS.local):]
    if os.path.exists(report):
        ltime = datetime.datetime.utcfromtimestamp(os.path.getmtime(f))
        rtime = datetime.datetime.utcfromtimestamp(os.path.getmtime(report))
        if rtime > ltime:
            return
    testpath = dirpath.replace(FLAGS.local, FLAGS.testdir, 1)
    for dp, sd, tests in os.walk(testpath):
        run_tests(dp, tests, f)


def run_tests(testdir, tests, submission):
    for t in tests:
        if t.endswith('.py'):
            run_single_test(os.path.join(testdir, t), submission)


def run_single_test(test, submission):
    log('Running %s for %s' % (test, submission))
    sys.path.append(os.path.dirname(test))
    mod, _ = os.path.splitext(os.path.basename(test))
    tst = importlib.import_module(mod)
    report = report_open(submission)
    report.write('Calificación: %f\n' % eval_submission(submission, report, tst))
    report.close()
    sys.path.remove(os.path.dirname(test))


def eval_submission(submission, report, tst):
    try: os.remove('_sut.py')
    except: pass
    os.symlink(submission, '_sut.py')
    try:
        sut = importlib.import_module('_sut')
        reload(sut)
    except:
        report_exception(report, submission, 'Sintaxis incorrecta')
        return 0
    return tst.test(submission, report, sut)


def download_folders(orig,dest):
    try:
        service = initialize_service()
        contents = service.files().list(q="title='"+orig+"'").execute()
        contents = service.files().list(q="'%s' in parents" % contents['items'][0]['id']).execute()
        for f in contents['items']:
            download_folder(service, f['id'], dest)
    except oauth2client.client.AccessTokenRefreshError:
        print ("The credentials have been revoked or expired, please re-run"
               "the application to re-authorize")


def download_folder(service, id, dest):
    folder = service.files().get(fileId = id).execute()
    print 'Downloading drive folder', folder['title']
    get_folder_contents(service, folder, dest)


def initialize_service():
    storage = oauth2client.file.Storage('drive.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = renew_credentials(storage)
    http = credentials.authorize(httplib2.Http())
    return apiclient.discovery.build("drive", "v2", http=http)


def renew_credentials(storage):
    flow = oauth2client.client.flow_from_clientsecrets(
        CLIENT_SECRETS,
        scope = 'https://www.googleapis.com/auth/drive',
        message = MISSING_CLIENT_SECRETS_MESSAGE)
    return oauth2client.tools.run(flow, storage)


def get_folder_contents(service, folder, base_path='./', depth=0):
    if FLAGS.debug:
        log('  ' * depth + "Getting contents of folder %s" % folder['title'])
    folder_contents = service.files().list(q="'%s' in parents" % folder['id']).execute()
    items = folder_contents['items']
    dest_path = os.path.join(base_path, folder['title'].replace('/', '_'))
    ensure_dir(dest_path)

    if folder.has_key('description'):
        desc = open(os.path.join(dest_path, '.desc'), 'w+')
        desc.write(folder['description'])
        desc.close()

    get_gdrive_files(service, items, dest_path, depth)
    get_gdrive_subfolders(service, items, dest_path, depth)


def get_gdrive_subfolders(service, items, dest_path, depth):

    for item in filter(is_gdrive_folder, items):
        if FLAGS.debug:
            log('  ' * depth + "[] " + item['title'])
        get_folder_contents(service, item, dest_path, depth+1)


def get_gdrive_files(service, items, dest_path, depth):

    for item in filter(is_gdrive_file, items):
        if FLAGS.debug:
            log('  ' * depth + "-- " + item['title'])

        full_path = os.path.join(dest_path, item['title'].replace('/', '_'))
        if not is_drive_file_modified(item, full_path):
            continue

        is_file_new = not os.path.exists(full_path)
        if not download_file(service, item, dest_path):
            log("ERROR while saving %s" % full_path)
            continue

        if is_file_new:
            log("Created %s" % full_path)
        else:
            log("Updated %s" % full_path)


def is_gdrive_folder(item):
    return item['mimeType'] == 'application/vnd.google-apps.folder'


def is_gdrive_file(item):
    return not is_gdrive_folder(item)


def log(str):
    if not type(str) is unicode:
        str = unicode(str, 'utf-8')
    LOG_FILE.write((str + '\n').encode('utf8'))


def ensure_dir(directory, silent=False):
    if not os.path.exists(directory):
        if not silent: log("Creating directory: %s" % directory)
        os.makedirs(directory)


def download_file(service, drive_file, dest_path):

    if not drive_file.has_key('downloadUrl'):
        log('File %s cannot be downloaded.' % drive_file['title'])
        return False

    try:
        resp, content = service._http.request(drive_file['downloadUrl'])

    except httplib2.IncompleteRead:
        log('Error while reading file %s. Retrying...' % drive_file['title'])
        return download_file(service, drive_file, dest_path)

    if resp.status != 200:
        log('An error occurred: %s' % resp)
        return False

    try:
        save_gdrive_content_to_local(drive_file, content, dest_path)
        return True
    except:
        log("Could not write to file to %s. Please check permissions." % dest_path)
        return False


def save_gdrive_content_to_local(drive_file, content, dest_path):
    file_location = os.path.join(dest_path, drive_file['title'].replace('/', '_'))
    target = open(file_location, 'w+')
    target.write(content)
    target.close()
    os.utime(file_location, (-1, get_gdrive_timestamp(drive_file)))
    if drive_file.has_key('description'):
        desc = open(file_location + '.desc', 'w+')
        desc.write(drive_file['description'])
        desc.close()


def get_gdrive_timestamp(drive_file):
    mtime = datetime.datetime.strptime(drive_file['modifiedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
    return (mtime - datetime.datetime(1970, 1, 1)).total_seconds()


def is_google_doc (drive_file):
    if re.match('^application/vnd\.google-apps\.script', drive_file['mimeType']): return False
    return True if re.match('^application/vnd\.google-apps\..+', drive_file['mimeType']) else False


def is_drive_file_modified(drive_file, local_file):
    if not os.path.exists(local_file):
        return True
    rtime = datetime.datetime.strptime(drive_file['modifiedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
    ltime = datetime.datetime.utcfromtimestamp(os.path.getmtime(local_file))
    return rtime > ltime


def is_local_file_modified(drive_file, local_file):
    rtime = datetime.datetime.strptime(drive_file['modifiedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
    ltime = datetime.datetime.utcfromtimestamp(os.path.getmtime(local_file))
    return rtime < ltime


def upload_all_reports():
    try:
        service = initialize_service()
        folder = ensure_remote_folder(service, FLAGS.remote)
        for dirpath, subdirs, files in os.walk(FLAGS.reportdir):
            upload_directory_reports(service, folder, dirpath, files)
    except oauth2client.client.AccessTokenRefreshError:
        print ("The credentials have been revoked or expired, please re-run"
               "the application to re-authorize")


def upload_directory_reports(service, folder, dirpath, files):
    folder = ensure_remote_folder(service, '/StudentReports' + dirpath[7:])
    for f in files:
        if not f.endswith('.log') and not f.endswith('.desc'):
            upload_file_report(service, folder, dirpath, f)


def upload_file_report(service, folder, dirpath, fname):
    # Solo enviar si es más nuevo
    report = os.path.join(dirpath, fname)
    update_or_insert_report(service, folder['id'], fname, report)


def update_or_insert_report(service, parent, fname, report):
    # Busca fname en folder
    q="title='%s' and '%s' in parents" % (fname, str(parent))
    result = service.files().list(q=q).execute()
    if result.has_key('items') and result['items']:
        gfile = result['items'][0]
        if not is_local_file_modified(gfile, report):
            return
        print 'Update', report
        time.sleep(.4)
        service.files().update(
            fileId = gfile['id'],
            media_body = report,
            body = {
                'mimeType': 'text/plain',
                'setModifiedDate': 'true',
                'modifiedDate': rfc3339_date_of(report),
                'parents':[ { 'id': parent } ] }).execute()
    else:
        print 'Insert', report
        time.sleep(.4)
        service.files().insert(
            media_body = report,
            body = {
                'mimeType':'text/plain',
                'modifiedDate': rfc3339_date_of(report),
                'parents':[ { 'id': parent } ],
                'title':fname }).execute()


def ensure_remote_folder(service, path):
    parent='root'
    for f in path.split(os.path.sep):
        if not f: continue
        q="title='%s' and '%s' in parents" % (f, str(parent))
        result = service.files().list(q=q).execute()
        if result.has_key('items') and result['items']:
            folder = result['items'][0]
        else:
            folder = create_remote_folder(service, f, parent)
        parent = folder['id']
    return folder

def create_remote_folder(service, fname, parent):
    return service.files().insert(body={
        'mimeType':'application/vnd.google-apps.folder',
        'parents': [ { 'id':str(parent) } ],
        'title': fname }).execute()

def rfc3339_date_of(path):
    ltime = datetime.datetime.utcfromtimestamp(os.path.getmtime(path))
    return ltime.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
