#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import argparse, sys, os, datetime, io, logging, shutil
import subprocess, mimetypes, configparser, pickle
import urllib.request, re
import lxml.etree as ET

parser = argparse.ArgumentParser(description="Use MOSS to detect plagiarism")
parser.add_argument('directory', nargs='?',
                    help='Submission directory',
                    default=None)
parser.add_argument('-D', '--download',
                    help='Download directory',
                    default='download')
parser.add_argument('-R', '--report',
                    help='Report directory',
                    default='reports')
parser.add_argument('-M', '--moss',
                    help='MOSS directory',
                    default='moss')
parser.add_argument('-k', '--key',
                    help='Encryption key',
                    default='8088')


ARGS = parser.parse_args(sys.argv[1:])
logging.basicConfig(filename=os.path.join(ARGS.report,'moss.log'),
                    level=logging.INFO)


def main():
    if not ARGS.directory:
        moss_directory(ARGS.download)    
    else:
        moss_directory(ARGS.directory)


def moss_directory(dir):
    copy_directory(dir)
    assert(dir.startswith(ARGS.download))
    moss_run(ARGS.moss + dir[len(ARGS.download):])


def copy_directory(dir):
    for dirpath, _, files in os.walk(dir):
        for f in files:
            if f.endswith('.log') or f.endswith('.p'): continue
            copy_file(os.path.join(dirpath,f))


def copy_file(path):
    path, fname = os.path.split(path)
    path, assignment = os.path.split(path)
    path, course = os.path.split(path)
    copy_submission(course, assignment, fname)


def copy_submission(course, assignment, fname):
    date, fileId, _, sig, _, name, _, mimetype, assignment, _ = get_meta(course, fname)
    if not is_latest(fname):
        return
    ident = get_identical(course, fname)
    if fname != ident[0]:
        return
    orig = os.path.join(ARGS.download, course, assignment, fname)
    dest = os.path.join(ARGS.moss, course, assignment, '_'.join(ident))
    d = os.path.dirname(dest)
    if not os.path.exists(d):
        os.makedirs(d)
    config = get_config(course, assignment)
    cmd = config['moss_copy']
    try: subprocess.run(cmd.format(orig, dest), input='', shell=True)
    except: pass


def moss_run(dir):
    course, assignment = None, None
    for dirpath, subdirs, files in os.walk(dir):
        components = dirpath.split(os.path.sep)
        if len(components) < 3:
            continue
        n = len(files) + len(subdirs)
        subdirs[:] = []
        # At least there must be two different submissions
        if n < 2:
            continue
        course, assignment = components[1:3]
        moss_assignment(course, assignment)


def moss_assignment(course, assignment):
    config = get_config(course, assignment)
    cmd = config['moss_command'].format(os.path.join(ARGS.moss, course, assignment))
    print ('Running', cmd)
    out = subprocess.check_output(cmd, shell=True).decode('utf8').strip().split('\n')
    url = out[-1]
    print ('Results available in', url)
    logging.info ('MOSS for {}/{} ({})'.format(course, assignment, url))
    moss_parse_report(url)


def moss_parse_report(url):
    f = urllib.request.urlopen(url)
    encoding = f.headers['content-type'].split('charset=')[-1]
    report = ET.HTML(f.read().decode(encoding))
    path_re = re.compile(r'moss/(.+)/(.+)/([^/ ]+)/? \((.+)%\)')
    for td in report.iter('td'):
        for a in td.iter('a'):
            course, assignment, submission, percent = path_re.match(a.text).groups()
            percent = float(percent)
            print (course, assignment, submission, percent)
            config = get_config(course, assignment)
            thr = float(config['moss_threshold'])
            if percent < thr:
                continue
            for f in submission.split('_'):
                moss_annotate_file(os.path.join(ARGS.report, course, assignment, f), url)


def moss_annotate_file(path, url):
    copy_mark = '{:-^70}'.format(' MOSS report ')
    with open(path + '.tmp', 'w') as to_file:
        with open(path, 'r') as from_file:
            for l in from_file:
                if l.startswith(copy_mark):
                    break
                to_file.write(l)
        to_file.write(copy_mark + '\n')
        to_file.write('''
MOSS ha detectado coincidencias significativas con otras entregas. Consulta
la siguiente URL para más detalles:

{0}

Comunica tus alegaciones por escrito mediante un mensaje en CampusVirtual al 
equipo docente para que las tenga en cuenta en la evaluación.
'''.format(url))
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
