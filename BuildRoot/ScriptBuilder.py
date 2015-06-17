import os
import sys
from stat import *

class ScriptBuilder:
    def generate_buildscript(self, config_obj, dest_file):
        build_root = os.path.abspath(config_obj.get_output_link() + os.sep + "..")
        build_script_path = os.path.abspath(build_root + os.sep + "scripts/build_system.py")
        buildroot_path = config_obj.get_buildroot_top()
        project_ini_path = config_obj.get_project_config()
        output_name = config_obj.get_output_name()
        #print "---===--*********************"
        #print build_script_path
        #print buildroot_path
        #print project_ini_path
        #print output_name
        #print "---===--*********************"
        #print 'SAVE to ' + dest_file
        if os.path.exists(dest_file):
            return

        f = open(dest_file, 'w')
        line = ''
        line += '#!/bin/bash'
        line += os.linesep
        line += 'if [ "$#" -ne 1 ]; then'
        line += os.linesep
        line += 'PARAM="HELP"'
        line += os.linesep
        line += 'else'
        line += os.linesep
        line += 'PARAM=$1'
        line += os.linesep
        line += 'fi'
        line += os.linesep
        line += build_script_path + ' ' + buildroot_path + ' ' + project_ini_path + ' ' + output_name + ' $PARAM'
        line += os.linesep
        f.write(line)
        f.close()
        os.chmod(dest_file, S_IWUSR | S_IRUSR | S_IXUSR | S_IXGRP | S_IXOTH)
