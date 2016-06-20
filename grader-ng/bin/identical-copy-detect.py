#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import argparse, sys, os, datetime, io, logging, shutil
import subprocess, mimetypes, configparser, pickle

parser = argparse.ArgumentParser(description="Detect identical copies of submissions")
parser.add_argument('directory', nargs='?',
                    help='Submission directory',
                    default=None)
parser.add_argument('-D', '--download',
                    help='Download directory',
                    default='download')
parser.add_argument('-R', '--report',
                    help='Report directory',
                    default='reports')
parser.add_argument('-k', '--key',
                    help='Encryption key',
                    default='8088')


ARGS = parser.parse_args(sys.argv[1:])
logging.basicConfig(filename=os.path.join(ARGS.report,'identical.log'),
                    level=logging.INFO)

def main():
    if not ARGS.directory:
        return label_directory(ARGS.download)
    
    return label_directory(ARGS.directory)


def label_directory(dir):
    for dirpath, _, files in os.walk(dir):
        for f in files:
            if f.endswith('.log') or f.endswith('.p'): continue
            label_file(os.path.join(dirpath,f))


def label_file(path):
    path, fname = os.path.split(path)
    path, assignment = os.path.split(path)
    path, course = os.path.split(path)
    label_submission(course, assignment, fname)


def label_submission(course, assignment, fname):
    logging.info ('Identity check {}/{}/{}'.format(course, assignment, fname))
    date, fileId, _, sig, _, name, _, mimetype, assignment, _ = get_meta(course, fname)
    if not is_latest(fname):
        return
    ident = get_identical(course, fname)
    dest = os.path.join(ARGS.report, course, assignment, fname)
    cfg = get_config(course, assignment)
    label_report(dest, ident, int(cfg['group_size']))


def label_report(path, ident, max_ident):
    if len(ident) <= max_ident:
        return
    logging.info ('Too many identical submissions for {}'.format(path))
    copy_mark = '{:-^70}'.format(' copy policy report ')
    with open(path + '.tmp', 'w') as to_file:
        with open(path, 'r') as from_file:
            for l in from_file:
                if l.startswith(copy_mark):
                    break
                to_file.write(l)
        to_file.write(copy_mark + '\n')
        to_file.write('''
Se han detectado coincidencias completas en las siguientes entregas:

{0}

Este ejercicio se puede realizar por un máximo de {1} personas. Por
tanto esta entrega viola la política de copias.

Si obtuviste autorización para realizarlo entre {2} personas debes
comunicarlo al equipo docente para que no lo tenga en cuenta en la
evaluación.
'''.format('\n'.join(ident), max_ident, len(ident)))
    shutil.move(path + '.tmp', path)


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
    return [ x for x in by_hash[course][h] if is_latest(x) ]


def is_latest(fname):
    return fname in latest_fileId


CONFIG = {}
def get_config(course, assignment):
    if not course in CONFIG:
        CONFIG[course] = configparser.ConfigParser()
        CONFIG[course].read(course + '.ini')
    return CONFIG[course][assignment]


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
