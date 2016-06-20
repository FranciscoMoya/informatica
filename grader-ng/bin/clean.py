#!/usr/bin/python3
# -*- coding: utf-8; mode: python -*-

import argparse, sys, os, datetime, io, logging, shutil

parser = argparse.ArgumentParser(description="Remove plagiarism annotations from reports")
parser.add_argument('directory', nargs='?',
                    help='Submission directory',
                    default=None)
parser.add_argument('-R', '--report',
                    help='Report directory',
                    default='reports')


ARGS = parser.parse_args(sys.argv[1:])
logging.basicConfig(filename=os.path.join(ARGS.report,'clean.log'),
                    level=logging.INFO)


def main():
    if not ARGS.directory:
        return clean_directory(ARGS.report)
    
    if os.path.isfile(ARGS.directory):
        return clean_file(ARGS.directory)

    return clean_directory(ARGS.directory)


def clean_directory(dir):
    logging.info ('clean_directory (dir={})'.format(dir))
    for dirpath, _, files in os.walk(dir):
        for f in files:
            if f.endswith('.log') or f.endswith('.p'): continue
            clean_file(os.path.join(dirpath,f))


def clean_file(path):
    logging.info ('clean_file (path={})'.format(path))
    mark1 = '{:-^70}'.format(' copy policy report ')
    mark2 = '{:-^70}'.format(' MOSS report ')
    with open(path + '.tmp', 'w') as to_file:
        with open(path, 'r') as from_file:
            for l in from_file:
                if l.startswith(mark1) or l.startswith(mark2):
                    break
                to_file.write(l)
    shutil.move(path + '.tmp', path)
    

main()
sys.exit(0)
