# -*- encoding: utf-8 -*-
"""Simple grader application for Python programs

Heavily based on drive.py application by Vignesh Nandha Kumar,
available on https://github.com/vikynandha/google-drive-backup.git
"""

__author__ = 'fco.moya@gmail.com (Francisco Moya)'

import gflags, httplib2, logging, os, sys, re, time, datetime

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError, flow_from_clientsecrets
from oauth2client.tools import run


FLAGS = gflags.FLAGS

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


gflags.DEFINE_enum('logging_level', 'ERROR',
                   ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                   'Set the level of logging detail.')
gflags.DEFINE_string('destination', 'downloaded', 'Destination folder location')
gflags.DEFINE_string('testdir', 'tests', 'Directory where tests are located')
gflags.DEFINE_boolean('debug', False, 'Log folder contents as being fetched')
gflags.DEFINE_string('logfile', 'drive.log', 'Location of file to write the log')
gflags.DEFINE_string('download', None, 'Folder Id to be fetched (if any)')
gflags.DEFINE_boolean('eval', False, 'Evaluate assignments')
gflags.DEFINE_boolean('grade', False, 'Send grades to LMS')


def main(argv):
    try:
        argv = FLAGS(argv)
    except gflags.FlagsError, e:
        print '%s\nUsage: %s ARGS\n%s' % (e, argv[0], FLAGS)
        sys.exit(1)

    initialize_logfile()
    if FLAGS.download:
        download_folder(FLAGS.download, FLAGS.destination)
    if FLAGS.eval:
        evaluate_all_assignments()
    if FLAGS.grade:
        update_all_grades()


def initialize_logfile():
    if not re.match('^/', FLAGS.logfile):
        ensure_dir(FLAGS.destination)
        FLAGS.logfile = os.path.join(FLAGS.destination, FLAGS.logfile)
    global LOG_FILE
    LOG_FILE = open(FLAGS.logfile, 'w+')
    logging.getLogger().setLevel(getattr(logging, FLAGS.logging_level))


def download_folder(id, dest):
    try:
        service = initialize_service()
        folder = service.files().get(fileId = id).execute()
        print 'Downloading drive folder', folder['title']
        get_folder_contents(service, folder, dest)
    except AccessTokenRefreshError:
        print ("The credentials have been revoked or expired, please re-run"
               "the application to re-authorize")


def evaluate_all_assignments():
    for dirpath, subdirs, files in os.walk(FLAGS.destination):
        evaluate_directory(dirpath, files)


def evaluate_directory(dirpath, files):
    for f in files:
        if not f.endswith('.log'):
            evaluate_file(dirpath, f)


def evaluate_file(dirpath, filename):
    testpath = dirpath.replace(FLAGS.destination, FLAGS.testdir, 1)
    for dp, sd, tests in os.walk(testpath):
        run_tests(dp, tests, os.path.join(dirpath, filename))


def run_tests(testdir, tests, submission):
    for t in tests:
        run_single_test(os.path.join(testdir, t), submission)


def run_single_test(test, submission):
    log('Running %s for %s' % (test, submission))
    execfile(test)


def initialize_service():
    storage = Storage('drive.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = renew_credentials(storage)
    return build("drive", "v2",
                 http = credentials.authorize(httplib2.Http()))


def renew_credentials(storage):
    flow = flow_from_clientsecrets(CLIENT_SECRETS,
                                   scope = 'https://www.googleapis.com/auth/drive',
                                   message = MISSING_CLIENT_SECRETS_MESSAGE)
    return run(flow, storage)


def get_folder_contents(service, folder, base_path='./', depth=0):
    if FLAGS.debug:
        log('  ' * depth + "Getting contents of folder %s" % folder['title'])

    try:
        folder_contents = service.files().list(q="'%s' in parents" % folder['id']).execute()
        items = folder_contents['items']
        dest_path = os.path.join(base_path, folder['title'].replace('/', '_'))

        ensure_dir(dest_path)
        get_gdrive_folder_files(service, items, dest_path, depth)
        get_gdrive_subfolders(service, items, dest_path, depth)

    except:
        log("ERROR: Couldn't get contents of folder %s. Retrying..." % folder['title'])
        get_folder_contents(service, folder, base_path, depth)


def get_gdrive_subfolders(service, items, dest_path, depth):

    for item in filter(is_gdrive_folder, folder_contents):
        if FLAGS.debug:
            log('  ' * depth + "[] " + item['title'])
        get_folder_contents(service, item, dest_path, depth+1)


def get_gdrive_files(service, items, dest_path, depth):

    for item in filter(is_gdrive_file, items):
        if FLAGS.debug:
            log('  ' * depth + "-- " + item['title'])

        full_path = os.path.join(dest_path, item['title'].replace('/', '_'))
        if not is_file_modified(item, full_path):
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


def ensure_dir(directory):
    if not os.path.exists(directory):
        log("Creating directory: %s" % directory)
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
        save_gdrive_content_to_local(drive_file, content)
        return True
    except:
        log("Could not write to file %s. Please check permissions." % file_location)
        return False


def save_gdrive_content_to_local(drive_file, content):
    file_location = os.path.join(dest_path, drive_file['title'].replace('/', '_'))
    target = open(file_location, 'w+')
    target.write(content)
    target.close()
    os.utime(file_location, (-1, get_gdrive_timestamp(drive_file)))


def get_gdrive_timestamp(drive_file):
    mtime = datetime.datetime.strptime(drive_file['modifiedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
    return (mtime - datetime.datetime(1970, 1, 1)).total_seconds()


def is_google_doc (drive_file):
    if re.match('^application/vnd\.google-apps\.script', drive_file['mimeType']): return False
    return True if re.match('^application/vnd\.google-apps\..+', drive_file['mimeType']) else False


def is_file_modified(drive_file, local_file):
    if os.path.exists(local_file):
        rtime = datetime.datetime.strptime(drive_file['modifiedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
        ltime = datetime.datetime.utcfromtimestamp(os.path.getmtime(local_file))
        return rtime > ltime
    else:
        return True


if __name__ == '__main__':
    main(sys.argv)
