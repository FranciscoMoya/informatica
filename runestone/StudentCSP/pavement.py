import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys

from sphinxcontrib import paverutils

sys.path.append(os.getcwd())

home_dir = os.getcwd()
master_url = 'http://127.0.0.1:8000'
master_app = 'runestone'
serving_dir = "./build/StudentCSP"

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/StudentCSP",
        sourcedir="_sources",
        outdir="./build/StudentCSP",
        confdir=".",
        project_name = "StudentCSP",
        template_args={'course_id': 'CSP',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel': 10,
                       'course_url':master_url,
                       'use_services': 'true',
                       'python3': 'true',
                       'basecourse': 'studentcsp'
                        }
    )
)

from runestone import build  # build is called implicitly by the paver driver.

