#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode/')

shutil.move('raynor.obj', 'ceph_storage/')  # we created file in /mycode this will move file to /ceph_storage

xname = input('What is the new name for kerrigan.obj? ')    # renameing the file with user input

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # move the newly named file to ceph_storage


