#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

import gflags, os, traceback
FLAGS = gflags.FLAGS

def normalize_sub(fname):
    return fname.split('/')[-2]

def report_correct(f, fname):
    f.write('CORRECTO ' + normalize_sub(fname) + '\n\n')

def report_wrong(f, fname, expected, actual):
    f.write('ERROR ' + normalize_sub(fname) + '\n')
    f.write('    Se esperaba: ' + expected + '\n')
    f.write('    Se obtuvo:   ' + actual + '\n\n')

def report_exception(f, fname, expected):
    f.write('ERROR ' + normalize_sub(fname) + '\n')
    f.write('    Se esperaba: ' + expected + '\n')
    f.write('    Ocurrió una excepción\n')
    traceback.print_exc(file=f)
    f.write('\n')

def report_open(fname):
    reportpath = fname.replace(FLAGS.destination, FLAGS.reportdir, 1)
    try:
        os.makedirs(os.path.dirname(reportpath))
    except:
        pass
    return open(reportpath, 'w')
