#-------------------------------------------------------------------------------
# Name:        haxeutils.py
# Purpose:
#
# Author:      Darcy.G
#
# Created:     04/03/2013
# Copyright:   (c) Darcy.G 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import os
import baseutils
import argparse
import re
import shutil
#import lxml.etree as etree
import string
import Global
import time

class haxetools(object):
    __cfg=object
    __mode="build"
    __target="flash"
    __proj_file="build.xml"

    def __init__(self,cfg):
        self.__cfg = cfg

    def setCfg(self,cfg):
        self.__cfg = cfg

    def getCfg(self):
        return self.__cfg;

    def getParameter(self,v):
        if type(v) == str :
            return v.strip()
        elif type(v) == list and len(v) > 0:
            return v[0].strip()

    def checkConfig(self):
        if self.__cfg.build:
            self.__mode = 'build'
        elif self.__cfg.run:
            self.__mode = 'run'
        elif self.__cfg.test:
            self.__mode = "test"
        elif self.__cfg.clean:
            self.__mode = "clean"
        else:
            self.__mode = "build"

        if self.__cfg.project_demo_file:
            self.__proj_file = self.__cfg.prefix_dir + "build-demo.xml"
        elif self.getParameter(self.__cfg.project_file) != "":
            self.__proj_file = self.getParameter(self.__cfg.prefix_dir) + \
                                self.getParameter(self.__cfg.project_file)
        else:
            self.__proj_file = self.getParameter(self.__cfg.prefix_dir) + "build.xml"

        if self.__cfg.target_android:
            self.__target = 'android'
        elif self.__cfg.target_flash:
            self.__target = 'flash'
        elif self.__cfg.target_neko:
            self.__target = "neko"
        elif self.__cfg.target_windows:
            self.__target = "windows"
        else:
            self.__target = 'flash'

    def doRun(self):
        self.checkConfig()
        print "  "+self.__cfg.description
        print "    command\t: "+self.__cfg.command
        print "    \tmode\t: "+self.__mode
        print "    \tproj\t: "+self.__proj_file
        print "    \ttarget\t: "+self.__target
        print ""
        cmdline = "openfl %s %s %s" % (self.__mode, self.__proj_file, self.__target)
        print "  Run Command\t: " + cmdline

        if not self.__cfg.no_run:
            cmdline = "haxelib run " + cmdline
            #print cmdline
            return os.system(cmdline)

