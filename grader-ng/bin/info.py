#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import argparse, sys, os, datetime, io, logging
import subprocess, mimetypes, configparser, pickle, base64

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
parser.add_argument('-l', '--latest', action='store_true',
                    help='Show only latest submission',
                    default=False)


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

    date, fileId, _, sig, _, name, _, mimetype, assignment, _ = get_meta(course, fname)
    if ARGS.latest and not is_latest(fname):
        return

    print ('[{}] {} {:>20} {} {}'.format(assignment, fileId, date, sig, name))
    ident = get_identical(course, fname)
    if len(ident) <= 1:
        return
    for i in ident:
        if ARGS.latest and not is_latest(i): continue
        if i == fname: continue
        _, _, _, _, _, name2, _, _, _, _ = get_meta(course, i)
        if name2 == name: continue
        print('    Identical to {} ({})'.format(i, name2))


CONFIG = {}
def get_config(course, assignment):
    if not course in CONFIG:
        CONFIG[course] = configparser.ConfigParser()
        CONFIG[course].read(course + '.ini')
    return CONFIG[course][assignment]
    

META = {}
by_hash = {}
by_fileId = {}
latest_fileId = set()


def get_meta(course, fname):
    global latest_fileId
    orig = os.path.join(ARGS.download, course, 'submissions.p')
    if not course in META:
        with open(orig, 'rb') as f:
            meta = pickle.load(f)
            META[course] = meta
            decrypt_fields(meta)
            hashes = { s[3] for s in meta['values'] }
            by_hash[course] = { k:[s[1] for s in meta['values'] if s[3] == k] for k in hashes }
            by_fileId[course] = { s[1]:s[3] for s in meta['values'] }
            latest = { (s[8],s[5]):s[1] for s in meta['values'] }
            latest_fileId = { i for i in latest.values() }
    for line in META[course]['values']:
        if line[1] == fname:
            return line
    raise ValueError('Unknown submission {}'.format(fname))


def get_identical(course, fname):
    assert(course in by_hash)
    h = by_fileId[course][fname]
    return by_hash[course][h]


def is_latest(fname):
    return fname in latest_fileId


def decrypt_fields(meta):
    for v in meta['values']:
        decrypt_row(v)

        
def decrypt_row(v):
    v[5] = decrypt_field(v[5], ARGS.key)

    
def decrypt_field(encrypted, passphrase):
    try: 
        with open(os.devnull, 'w') as devnull:
            encrypted = base64.b64decode(encrypted)
            cmd_openssl = 'openssl enc -d -aes-256-cbc -pass pass:{}'
            return subprocess.check_output(cmd_openssl.format(passphrase),
                            input=encrypted,
                            stderr=devnull,
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
