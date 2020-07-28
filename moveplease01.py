#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode/')   # naming path to execute the follwing script

shutil.move('raynor.obj', 'ceph_storage/')  # we created file in /mycode this will move file to /ceph_storage

xname = input('What is the new name for kerrigan.obj? ')    # saving user input as a variable

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # using concantenation to add the user input and complete the path 


