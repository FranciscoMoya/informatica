#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import argparse, sys, os, datetime, io, logging
import subprocess, mimetypes, configparser

parser = argparse.ArgumentParser(description="Evaluate assignment running test suites")
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
                    help='Evaluate a single assignment')

ARGS = parser.parse_args(sys.argv[1:])
logging.basicConfig(filename=os.path.join(ARGS.report,'report.log'),
                    level=logging.INFO)

CONFIG = {}

def main():
    if ARGS.single:
        _ , course, assignment, fname = ARGS.single.split('/')
        eval_submission(course, assignment, fname)
    elif ARGS.config:
        course, _ = os.path.splitext(ARGS.config)
        eval_course(course)
    else:
        dirpath, subdirs, files = next(os.walk(ARGS.download))
        for course in subdirs:
            eval_course(course)


def eval_course(course):
    logging.info ('Eval course {}'.format(course))
    orig = os.path.join(ARGS.download, course)
    dirpath, subdirs, files = next(os.walk(orig))
    for assignment in subdirs:
        eval_assignment(course, assignment)


def eval_assignment(course, assignment):
    logging.info ('Eval assignment {}/{}'.format(course, assignment))
    orig = os.path.join(ARGS.download, course, assignment)
    dest = os.path.join(ARGS.report, course, assignment)
    dirpath, subdirs, files = next(os.walk(orig))
    for f in files:
        eval_submission(course, assignment, f)


def eval_submission(course, assignment, fname):
    logging.info ('Eval submission {}/{}/{}'.format(course, assignment, fname))
    dest = os.path.join(ARGS.report, course, assignment, fname)
    ensure_dir(os.path.dirname(dest))
    if os.path.exists(dest):
        logging.info ('  Already available {}'.format(dest))
        return
    run_tests(course, assignment, fname)

        
def run_tests(course, assignment, fname):
    orig = os.path.join(ARGS.download, course, assignment, fname)
    dest = os.path.join(ARGS.report, course, assignment, fname)
    config = get_config(course, assignment)
    with io.FileIO(dest, 'w') as f:
        input = eval(config['input']) if 'input' in config else ''
        print('Testing {}...'.format(orig),end='')
        logging.info('Running tests for {}'.format(orig))
        if 'pre' in config:
            subprocess.run(config['pre' ].format(orig),
                           shell=True)
        if 'test' in config:
            subprocess.run(config['test'].format(orig),
                           shell=True, stderr=f,
                           input=input)
        if 'post' in config:
            subprocess.run(config['post'].format(orig),
                           shell=True)
        print('Done')


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
