#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import argparse, sys, os, datetime, io, logging
import subprocess, mimetypes, configparser, pickle

parser = argparse.ArgumentParser(description="Get information on given submissions")
parser.add_argument('directory', nargs='?',
                    help='Submission directory',
                    default=None)
parser.add_argument('-D', '--download',
                    help='Download directory',
                    default='download')
parser.add_argument('-k', '--key',
                    help='Encryption key',
                    default='8088')

ARGS = parser.parse_args(sys.argv[1:])
logging.basicConfig(filename=os.path.join(ARGS.download,'info.log'),
                    level=logging.INFO)

def main():
    if not ARGS.directory:
        return info_directory(ARGS.download)
    
    if os.path.isfile(ARGS.directory):
        return info_file(ARGS.directory)

    return info_directory(ARGS.directory)


def info_directory(dir):
    for dirpath, _, files in os.walk(dir):
        for f in files:
            if f.endswith('.log') or f.endswith('.p'): continue
            info_file(os.path.join(dirpath,f))


def info_file(path):
    path, fname = os.path.split(path)
    path, assignment = os.path.split(path)
    path, course = os.path.split(path)
    info_submission(course, fname)


def info_submission(course, fname):
    logging.info ('Info submission {}/{}'.format(course, fname))
    date, fileId, _, _, _, name, _, mimetype, assignment, _ = get_meta(course, fname)
    print ('{:>20} {} {}'.format(date, fileId, name))

        
CONFIG = {}
def get_config(course, assignment):
    if not course in CONFIG:
        CONFIG[course] = configparser.ConfigParser()
        CONFIG[course].read(course + '.ini')
    return CONFIG[course][assignment]
    

META = {}
def get_meta(course, fname):
    orig = os.path.join(ARGS.download, course, 'submissions.p')
    if not course in META:
        with open(orig, 'rb') as f:
            META[course] = pickle.load(f)
            decrypt_fields(META[course])
    for line in META[course]['values']:
        if line[1] == fname:
            return line
    raise ValueError('Unknown submission {}'.format(fname))


def decrypt_fields(meta):
    for v in meta['values']:
        decrypt_row(v)

def decrypt_row(v):
    v[5] = decrypt_field(v[5], ARGS.key)

def decrypt_field(encrypted, passphrase):
    try:
        cmd_openssl = 'openssl enc -d -aes-256-cbc -base64 -pass pass:{}'
        return subprocess.check_output(cmd_openssl.format(passphrase),
                                       input=(encrypted+'\n').encode('utf8'),
                                       shell=True).decode('utf8')
    except:
        return encrypted


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
