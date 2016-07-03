#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import argparse, sys, os, datetime, io, logging
import subprocess, mimetypes, configparser
import pickle, shutil

parser = argparse.ArgumentParser(description="Evaluate assignment running test suites")
parser.add_argument('directory', nargs='?',
                    help='Submission directory',
                    default=None)
parser.add_argument('-D', '--download',
                    help='Download directory',
                    default='download')
parser.add_argument('-R', '--report',
                    help='Report directory',
                    default='reports')

ARGS = parser.parse_args(sys.argv[1:])
logging.basicConfig(filename=os.path.join(ARGS.report,'eval.log'),
                    level=logging.INFO)


def main():
    if not ARGS.directory:
        return eval_directory(ARGS.download)
    
    if os.path.isfile(ARGS.directory):
        return eval_file(ARGS.directory)

    return eval_directory(ARGS.directory)


def eval_directory(dir):
    logging.info ('eval_directory (dir={})'.format(dir))
    for dirpath, _, files in os.walk(dir):
        for f in files:
            if f.endswith('.log') or f.endswith('.p'): continue
            eval_file(os.path.join(dirpath,f))


def eval_file(path):
    logging.info ('eval_file (path={})'.format(path))
    path, fname = os.path.split(path)
    path, assignment = os.path.split(path)
    path, course = os.path.split(path)
    
    eval_submission(course, assignment, fname)


def eval_submission(course, assignment, fname):
    logging.info ('Eval submission {}/{}/{}'.format(course, assignment, fname))
    dest = os.path.join(ARGS.report, course, assignment, fname)
    ensure_dir(os.path.dirname(dest))
    if os.path.exists(dest):
        logging.info ('  Already available {}'.format(dest))
        return

    for f in get_identical(course, fname):
        orig = os.path.join(ARGS.report, course, assignment, f)
        if os.path.exists(orig):
            logging.info ('  Copying report from {}'.format(orig))
            shutil.copyfile(orig, dest)
            return

    run_tests(course, assignment, fname)
        

        
def run_tests(course, assignment, fname):
    orig = os.path.join(ARGS.download, course, assignment, fname)
    dest = os.path.join(ARGS.report, course, assignment, fname)
    config = get_config(course, assignment)
    with io.FileIO(dest, 'w') as f:
        input = eval(config['input']) if 'input' in config else ''
        print('Testing {} into {} ...'.format(orig, dest),
              end='',flush=True)
        logging.info('Running tests for {}'.format(orig))
        if 'pre' in config:
            try: subprocess.run(config['pre' ].format(orig), shell=True)
            except: pass
        if 'test' in config:
            try: subprocess.run(config['test'].format(orig),
                                shell=True, stderr=f,
                                input=input)
            except: pass
        if 'post' in config:
            try: subprocess.run(config['post'].format(orig),
                                shell=True)
            except: pass
    print('Done')


by_hash = {}
by_fileId = {}

def get_identical(course, fname):
    if course not in by_hash:
        load_course_metadata(course)
    if fname in by_fileId[course]:
        h = by_fileId[course][fname]
        return by_hash[course][h]
    return fname


def load_course_metadata(course):
    orig = os.path.join(ARGS.download, course)
    with open(os.path.join(orig, 'submissions.p'), 'rb') as f:
        sub = pickle.load(f)
        hashes = { s[3] for s in sub['values'] }
        by_hash[course] = { k:[s[1] for s in sub['values'] if s[3] == k] for k in hashes }
        by_fileId[course] = { s[1]:s[3] for s in sub['values'] }


CONFIG = {}
def get_config(course, assignment):
    if not course in CONFIG:
        CONFIG[course] = configparser.ConfigParser()
        CONFIG[course].read(course + '.ini')
    return CONFIG[course][assignment]
    

def ensure_dir(directory, silent=False):
    if not os.path.exists(directory):
        os.makedirs(directory)


main()
sys.exit(0)
