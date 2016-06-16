#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import argparse, sys, os, datetime, io, logging, pickle, configparser, getpass, base64
from campusvirtual import cv_authenticate, cv_submit_mark

parser = argparse.ArgumentParser(description="Grade assignment based on nosetests report")
parser.add_argument('config', nargs='?',
                    help='Configuration file',
                    default=None)
parser.add_argument('-D', '--download',
                    help='Download directory',
                    default='download')
parser.add_argument('-R', '--report',
                    help='Report directory',
                    default='reports')
parser.add_argument('-1', '--single',
                    help='Grade a single assignment')
parser.add_argument('-u', '--user',
                    help='UCLM user name',
                    default='francisco.moya')
parser.add_argument('-p', '--password',
                    help='UCLM password',
                    default=None)
parser.add_argument('-k', '--key',
                    help='OAuth client key',
                    default='clave')
parser.add_argument('-s', '--secret',
                    help='OAuth shared secret',
                    default='shared')

ARGS = parser.parse_args(sys.argv[1:])
logging.basicConfig(filename=os.path.join(ARGS.report,'grade.log'),
                    level=logging.INFO)

CONFIG = {}

def main():
    if not ARGS.password:
        ARGS.password = getpass.getpass()
    cv_authenticate(ARGS.user, ARGS.password)
    if ARGS.single:
        _ , course, assignment, fname = ARGS.single.split('/')
        grade_report(course, assignment, fname)
    elif ARGS.config:
        course, _ = os.path.splitext(ARGS.config)
        grade_course(course)
    else:
        dirpath, subdirs, files = next(os.walk(ARGS.report))
        for course in subdirs:
            grade_course(course)


def grade_course(course):
    with io.FileIO(os.path.join(ARGS.download, course, 'submissions.p'), 'rb') as f:
        submissions = pickle.load(f)
        for s in submissions['values']:
            grade_submission(course, s)


def grade_submission(course, submission):
    ( date, fname, folder, _,
      lis_outcome_service_url, lis_person_name_full, lis_result_sourcedid,
      mime_type, assignment, sid ) = submission[:10]
    if lis_result_sourcedid.startswith('b64:'):
        lis_result_sourcedid = base64.b64decode(lis_result_sourcedid[4:]).decode('utf8')
    logging.info ('Grading submission {}/{}/{}'.format(course, assignment, fname))
    orig = os.path.join(ARGS.report, course, assignment, fname)
    mark = parse_mark(orig)*get_config(course,assignment).getfloat('points')
    print ('Grade submission {}/{}/{}: {}'.format(course, assignment, fname, mark))
    if cv_submit_mark(lis_outcome_service_url, lis_result_sourcedid, mark,
                      ARGS.key.encode('utf8'), ARGS.secret.encode('utf8')):
        logging.info ('Grading {}/{}/{}: {}'.format(course, assignment, fname, mark))
    else:
        logging.info ('Failed grading {}/{}/{}: {}'.format(course, assignment, fname, mark))
        raise SystemError('Failed')


def parse_mark(path):
    print('Report {}'.format(path))
    with io.FileIO(path, 'r') as f:
        result = next(f).decode('utf8').strip()
        return result.count('.')/len(result)

        
def get_config(course, assignment):
    if not course in CONFIG:
        CONFIG[course] = configparser.ConfigParser()
        CONFIG[course].read(course + '.ini')
    return CONFIG[course][assignment]
    

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
