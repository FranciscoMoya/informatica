#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

# client_secrets.json, file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs Console:
# http://code.google.com/apis/console

import argparse, sys, os, datetime, io, logging
import oauth2client, oauth2client.tools, oauth2client.file
import httplib2, apiclient.discovery, apiclient.http
import subprocess, mimetypes, pickle

parser = argparse.ArgumentParser(description="Download files from Upload script",
                                 parents=[oauth2client.tools.argparser])
parser.add_argument('sheet', nargs='?',
                    help='Google Sheets Id for the metadata spreadsheet',
                    default='1xQ5SF7drtCH6m8GKf-1Gi78pCPMz6kHcMh8EmDTHmiY')
parser.add_argument('-D', '--dest',
                    help='Destination directory',
                    default='download')
parser.add_argument('-k', '--key',
                    help='Encryption key for personal data',
                    default='8088')

ARGS = parser.parse_args(sys.argv[1:])
logging.basicConfig(filename=os.path.join(ARGS.dest,'download.log'),
                    level=logging.INFO)

def main():
    try:
        download_spreadsheet(ARGS.dest, ARGS.sheet)
    except oauth2client.client.AccessTokenRefreshError:
        logging.error ('The credentials have been revoked or expired, please re-run'
                       'the application to re-authorize')

def download_spreadsheet(dest, sid):
    ''' Assumes dest and id strings.
        Downloads submissions to all assignments in the ssheet with
        the supplied Google id (sid) into the directory specified in dest.
    '''
    sheets = initialize_sheets_service()
    ss = sheets.spreadsheets().get(spreadsheetId=sid).execute()
    dest = makedirs_spreadsheet(dest, ss)
    
    drive = initialize_drive_service()
    metadata = drive.files().list(q="name='{}'".format(sid)).execute()
    if not 'files' in metadata or not metadata['files']:
        raise NameError('Submissions not found')
    if len(metadata['files']) > 1:
        logging.info ('More than one submission record, taking the first one.')
        logging.info (metadata)
    sid = metadata['files'][0]['id']
    ss = sheets.spreadsheets().get(spreadsheetId=sid).execute()
    rows = ss['sheets'][0]['properties']['gridProperties']['rowCount']
    if rows <= 1:
        raise ValueError('No submissions')
    submissions = sheets.spreadsheets().values().get(spreadsheetId=sid,
                    range='A2:J{}'.format(rows)).execute()
    download_submissions(dest, submissions, drive)


def download_submissions(dest, submissions, drive):
    logging.info ('Download submissions to {}'.format(dest))
    with io.FileIO(os.path.join(dest, 'submissions.p'), 'wb') as f:
        pickle.dump(submissions, f)
    for s in submissions['values']:
        download_single_submission(dest, s, drive)


def download_single_submission(dest, submission, drive):
    ( date, fileId, folder, _,
      lis_outcome_service_url, lis_person_name_full, lis_result_sourcedid,
      mime_type, s, sid ) = submission[:10]
    download_drive_file(os.path.join(dest, s), fileId, drive)
    name = decrypt_field(lis_person_name_full, ARGS.key)
    logging.info ('File {}/{}/{} from {}'.format(dest, s, fileId, name))


def download_drive_file(dest, fileId, drive):
    fpath = os.path.join(dest, fileId)
    if os.path.exists(fpath):
        return

    req = drive.files().get_media(fileId=fileId)
    target = io.FileIO(fpath, mode='wb')
    downloader = apiclient.http.MediaIoBaseDownload(target, req)
    done = False
    while done is False:
        status, done = downloader.next_chunk()


def makedirs_spreadsheet(dest, spreadsheet):
    ''' Assumes dest a directory, spreadsheet a valid Google spreadsheet.
        Make destination directories for all assignments in spreadsheet.
        Returns destination directory.
    '''
    title = spreadsheet['properties']['title']
    sheets = spreadsheet['sheets']
    dest = os.path.join(dest, sstr(title))
    ensure_dir(dest)
    for sheet in sheets:
        title = sheet['properties']['title']
        sheetdest = os.path.join(dest, sstr(title))
        ensure_dir(sheetdest)
    return dest

def initialize_sheets_service():
    http = initialize_http_service()
    return apiclient.discovery.build("sheets", "v4", http=http)


def initialize_drive_service():
    http = initialize_http_service()
    return apiclient.discovery.build("drive", "v3", http=http)
    
def initialize_http_service():
    storage = oauth2client.file.Storage('drive.db')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = renew_credentials(storage)
    return credentials.authorize(httplib2.Http())


def renew_credentials(storage):
    flow = oauth2client.client.flow_from_clientsecrets(
        'client_secrets.json',
        scope = 'https://www.googleapis.com/auth/drive',
        message = '''Configura client_secrets.json usando 
                     http://code.google.com/apis/console''')
    return oauth2client.tools.run_flow(flow, storage, ARGS)


def ensure_dir(directory, silent=False):
    if not os.path.exists(directory):
        os.makedirs(directory)


def decrypt_field(encrypted, passphrase):
    cmd_openssl = 'openssl enc -d -aes-256-cbc -base64 -pass pass:{}'
    return subprocess.check_output(cmd_openssl.format(passphrase),
                                   input=(encrypted+'\n').encode('utf8'),
                                   shell=True).decode('utf8')


def sstr(s):
    '''Assumes s a string.
       Returns a safe string (string without conflictive chars)
    '''
    transtab = { 'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u',
                 'Á':'A', 'É':'E', 'Í':'I', 'Ó':'O', 'Ú':'U',
                 'ñ':'n', 'Ñ':'N', 'ü':'u', 'Ü':'U',
                 ' ':'_', '/':'_'}
    for k in transtab:
        s = s.replace(k, transtab[k])
    return s


main()
sys.exit(0)
