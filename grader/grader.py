#!/usr/bin/env python
# -*- coding: utf-8; mode: python -*-
"""Simple grader application for Python programs

Heavily based on drive.py application by Vignesh Nandha Kumar,
available on https://github.com/vikynandha/google-drive-backup.git
"""

__author__ = 'fco.moya@gmail.com (Francisco Moya)'

import gflags, sys, Grader
import logging, httplib2

FLAGS = gflags.FLAGS

gflags.DEFINE_enum('logging_level', 'ERROR',
                   ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                   'Set the level of logging detail.')
gflags.DEFINE_string('remote', 'StudentFiles', 'Remote folder location')
gflags.DEFINE_string('local', 'downloaded', 'Local folder location')
gflags.DEFINE_string('testdir', 'tests', 'Directory where tests are located')
gflags.DEFINE_string('reportdir', 'reports', 'Directory where evaluation reports will be stored')
gflags.DEFINE_string('cheaters', 'tests/cheaters.txt', 'File with students which were caught while cheating')
gflags.DEFINE_string('cheater_template', 'tests/cheater_template.txt', 'Common report for all cheaters')
gflags.DEFINE_boolean('debug', False, 'Log folder contents as being fetched')
gflags.DEFINE_string('logfile', 'drive.log', 'Location of file to write the log')
gflags.DEFINE_boolean('download', False, 'Download StudentFiles folder')
gflags.DEFINE_boolean('upload', False, 'Upload reports to GDrive')
gflags.DEFINE_boolean('eval', False, 'Evaluate assignments')
gflags.DEFINE_boolean('grade', False, 'Send grades to LMS')
gflags.DEFINE_string('user', '', 'UCLM User (required for grading)')
gflags.DEFINE_string('password', '', 'UCLM Password (required for grading)')
gflags.DEFINE_string('key', 'clave', 'LTI Consumer key')
gflags.DEFINE_string('secret', 'shared', 'LTI Shared secret')

def main(argv):
    try:
        argv = FLAGS(argv)
    except gflags.FlagsError, e:
        print '%s\nUsage: %s ARGS\n%s' % (e, argv[0], FLAGS)
        sys.exit(1)

    Grader.initialize()
    if FLAGS.debug:
        logging.basicConfig(filename='grader.log',level=logging.DEBUG)
        httplib2.debuglevel=4
    if FLAGS.download:
        Grader.download_folders(FLAGS.remote, FLAGS.local)
    if FLAGS.eval:
        Grader.evaluate_all_assignments()
    if FLAGS.upload:
        # Correct default remote path
        if FLAGS.remote == 'StudentFiles':
            FLAGS.remote = 'StudentReports'
        Grader.upload_all_reports()
    if FLAGS.grade:
        Grader.update_all_grades()

if __name__ == '__main__':
    main(sys.argv)
