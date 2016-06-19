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

parser = argparse.ArgumentParser(description="Upload reports for Upload script",
                                 parents=[oauth2client.tools.argparser])
parser.add_argument('-R', '--report',
                    help='Report directory',
                    default='reports')
parser.add_argument('-D', '--dest',
                    help='Destination directory in Google Drive',
                    default='UploadReports')
parser.add_argument('-f', '--force', action='append',
                    help='Force upload of the given files',
                    default=[])

ARGS = parser.parse_args(sys.argv[1:])
logging.basicConfig(filename=os.path.join(ARGS.report,'upload.log'),
                    level=logging.INFO)

def main():
    try:
        upload_files()
    except oauth2client.client.AccessTokenRefreshError:
        logging.error ('The credentials have been revoked or expired, please re-run'
                       'the application to re-authorize')


def upload_files():
    folderId = None
    drive = initialize_drive_service()
    folderId = drive_destination_folder(drive)
    forceFiles = [ os.path.basename(f) for f in ARGS.force ]
    already_in_drive = [x for x in drive_list_folder(drive, folderId) if x not in forceFiles]
    
    for dirpath, subdirs, files in os.walk(ARGS.report):
        for f in files:
            if f.endswith('.log') or f.endswith('.p') or f in already_in_drive:
                continue
            upload_file(dirpath, f, folderId, drive)


def drive_destination_folder(drive):
    folder = drive.files().list(q="name='{}'".format(ARGS.dest)).execute()
    if not 'files' in folder or not folder['files']:
        data = {
            'name' : ARGS.dest,
            'mimeType' : 'application/vnd.google-apps.folder'
        }
        folder = drive.files().create(body=data, fields='id').execute()
        return folder['id']

    if len(folder['files']) > 1:
        logging.info ('More than one {} folder, taking the first one.'.format(ARGS.dest))
        logging.info (folder)
    return folder['files'][0]['id']


def drive_list_folder(drive, folderId):
    contents = []
    pageToken = None
    while True:
        folder_contents = drive.files().list(q="'{}' in parents".format(folderId),
                                             pageToken=pageToken).execute()
        pageToken = folder_contents.get('nextPageToken')
        contents += [i['name'] for i in folder_contents['files'] if i['kind'] == 'drive#file']
        if not pageToken:
            return contents


def upload_file(dirpath, f, folderId, drive):
    print('Uploading {}/{}'.format(dirpath,f))
    logging.info('Uploading {}/{}'.format(dirpath,f))
    media = apiclient.http.MediaFileUpload(os.path.join(dirpath,f),
                                           mimetype='text/plain',
                                           resumable=True)
    drive.files().create(media_body = media,
                         body={'name': f,
                               'parents': [ folderId ]}).execute()


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


if __name__ == "__main__":
    main()
    sys.exit(0)
