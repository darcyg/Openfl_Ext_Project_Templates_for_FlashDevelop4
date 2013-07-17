#-------------------------------------------------------------------------------
# Name:        baseutils.py
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
import re
import pinyin
import base64
import chardet
import shutil
import platform
import argparse

def findAllChineseStr(array_str):
    result=[]
    for line in array_str:
        #print fname
        m=re.search(ur"[\u4e00-\u9fa5]+",unicode(line.decode("gbk")))
        if m:
            result.append(line)
    return result

def findAllSwfFile(array_str):
    result=[]
    for line in array_str:
        #print fname
        #(filepath,filename)=os.path.split(line)
        #(filebasename,fileext)=os.path.splitext(filename)
        #fileext = fileext.lower()
        info=fileinfo(line)
        if (info.getExt() == ".swf"):
            result.append(line)
    return result

##def getFileInfo(pathfile,root=""):
##    (filepath,filename)=os.path.split(pathfile)
##    (filebasename,fileext)=os.path.splitext(filename)
##    realpath = os.path.realpath(filepath+"/"+root)
##    realpathfile = os.path.realpath(realpath+"/"+filename)
##    fileext_u = fileext.lower()
##    result={"pathfile":pathfile,"path":filepath,"file":filename,"base":filebasename,"ext":fileext_u,"realpath":realpath,"realpathfile":realpathfile}
##    return result

class fileinfo(object):
    __src=""
    filepath=""
    root=""
    dirname=""
    pathname=""
    filename=""
    filebasename=""
    basename=""
    fileext=""
    realpath=""
    realdirname=""
    realpathname=""
    has_file=False
    has_dir=False
    has_path=False
    has_base=False
    has_ext=False
    is_cn_fix=False
    __tmp_data=[]
    __cfg=object

    def __init__(self,_file,_cfg=object,_root=""):
        self.filepath = self.__src = self.__fix_path(_file)
        self.__cfg = _cfg
        self.root = self.__fix_path(_root)
        self.__split_filepath()
        self.__split_realfilepath()

    def setCfg(self,_cfg):
        self.__cfg = _cfg

    def SrcRoot(self,is_mkdir=False):
        if isinstance(self.__cfg,argparse.Namespace):
            self.changeRoot(self.__cfg.source_dir)
        if is_mkdir:
            self.mkdirs()
        return self

    def TmpRoot(self,is_mkdir=False):
        if isinstance(self.__cfg,argparse.Namespace):
            self.changeRoot(self.__cfg.temp_dir)
        if is_mkdir:
            self.mkdirs()
        return self

    def DstRoot(self,is_mkdir=False):
        if isinstance(self.__cfg,argparse.Namespace):
            self.changeRoot(self.__cfg.target_dir)
        if is_mkdir:
            self.mkdirs()
        return self

    def DefRoot(self):
        self.changeRoot("")
        return self

    def __fix_path(self,pathf=""):
        if platform.system() == "Windows":
            return pathf.replace("/","\\")
        else:
            return pathf.replace("\\","/")

    def __split_filepath(self):
        if (self.root.strip() != ""):
            self.filepath = self.__fix_path(self.root+"/"+
                os.path.dirname(self.__src)+"/"+
                os.path.basename(self.filepath))

        self.dirname = os.path.dirname(self.filepath)
        self.filename = os.path.basename(self.filepath)
        self.filebasename,self.fileext = os.path.splitext(self.filename)
        self.pathname = self.dirname
        self.basename = self.filebasename
        self.has_path=self.has_dir = self.dirname.strip()!=""
        self.has_file = self.filename.strip()!=""
        self.has_base = self.basename.strip()!=""
        self.has_ext = self.fileext.strip()!=""

    def __split_realfilepath(self):
        self.realpath = os.path.realpath(self.filepath)
        self.realdirname = os.path.realpath(self.dirname)
        self.realpathname = self.realdirname

    def toDist(self):
        return {
            "src":self.__src,
            "filepath":self.filepath,
            "dirname":self.dirname,
            "pathname":self.pathname,
            "filename":self.filename,
            "filebasename":self.filebasename,
            "basename":self.basename,
            "fileext":self.fileext,
            "realpath":self.realpath,
            "realdirname":self.realdirname,
            "realpathname":self.realpathname
            }

    def file_exists(self):
        return os.path.isfile(self.realpath) and os.path.exists(self.realpath)

    def dir_exists(self):
        #print self.realdirname
        return os.path.isdir(self.realdirname) and os.path.exists(self.realdirname)

    def path_exists(self):
        return os.path.isdir(self.realdirname) and os.path.exists(self.realpathname)

    def mkdirs(self):
        if not self.dir_exists():
            #print self.realpathname
            os.makedirs(self.realpathname)
        return self

    def changeRoot(self,newRoot):
        self.root = self.__fix_path(newRoot)
        self.__split_filepath()
        self.__split_realfilepath()
        return self

    def changePath(self,newPath):
        prefix=""
        if self.has_file:
            prefix = "/"+self.filename
        self.filepath = self.__fix_path(newPath + prefix)
        self.__split_filepath()
        self.__split_realfilepath()
        return self

    def changeFileName(self,newFileName):
        prefix=""
        if self.has_dir:
            prefix = self.dirname
        self.filepath = self.__fix_path(prefix +"/"+ newFileName)
        self.__split_filepath()
        self.__split_realfilepath()
        return self

    def changeBaseName(self,newBaseName):
        prefix=""
        if self.has_dir:
            prefix = self.dirname
        self.filepath = self.__fix_path(prefix +"/"+ newBaseName + self.fileext)
        self.__split_filepath()
        self.__split_realfilepath()
        return self

    def changeFileExt(self,newFileExt):
        prefix=""
        if self.has_dir:
            prefix = self.dirname
        self.filepath = self.__fix_path(prefix +"/"+ self.basename + newFileExt)
        #print self.filepath
        self.__split_filepath()
        self.__split_realfilepath()
        return self

    def changeExtToLower(self):
        return self.changeFileExt(self.fileext.lower())

    def getExt(self):
        return self.fileext.lower()

    def checkCnString(self):
        m=re.search(ur"[\u4e00-\u9fa5]+",unicode(self.filepath.decode("gbk")))
        if m:
            return True
        else:
            return False

    def getCnPathToEnPath(self):
        pathfile = self.filepath
        pathfile = pathfile.replace('\\','/')
        paths = pathfile.split('/')
        py= pinyin.PinYin()
        py.load_word()
        ens=[]
        for p in paths:
            is_en = True
            en = ''
            cn = ''
            for c in p:
                if (is_cn_char(c)):
                    is_en = False
                    en = en+py.hanzi2pinyin(string=c)[0]
                    cn = cn+unicode(c)
                else:
                    en = en+c
                    #cn = cn+c
            if not(is_en):
                #print cn
                en = "["+ub64enc(cn,urlsafe)+"]_"+en
                #print b64
                #print ub64dec(b64)
            ens.append(en)
        return self.__fix_path('/'.join(ens))

    def changeCnPathToEnPath(self):
        self.filepath = self.getCnPathToEnPath()
        self.is_cn_fix = True
        self.__split_filepath()
        self.__split_realfilepath()

    def changeDefault(self):
        self.filepath = self.__src
        self.is_cn_fix = False
        self.__split_filepath()
        self.__split_realfilepath()

    def get_walk_dirs(self, topdown=True,show_file=False,show_dir=False):
        lendir=len(self.dirname)+1
        result = []
        for root, dirs, files in os.walk(self.dirname, topdown):
            for name in files:
                pathfile = self.__fix_path(os.path.join(root,name)[lendir:])
                result.append(pathfile)
                if show_file:
                    print(pathfile)
                ##fileinfo.write(os.path.join(root,name) + '\n')
            if (show_dir):
                for name in dirs:
                    pathfile = self.__fix_path(os.path.join(root,name)[lendir:])
                    print(pathfile)
                ##fileinfo.write('dir|  ' + os.path.join(root,name) + '\n')
        return result

def walk_dir(dir,fileinfo,topdown=True):
    lendir=len(dir)+1
    result = []
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            pathfile = os.path.join(root,name)[lendir:]
            #print(pathfile)
            result.append(pathfile)
            fileinfo.write(os.path.join(root,name) + '\n')
        for name in dirs:
            pathfile = os.path.join(root,name)[lendir:]
            #print(pathfile)
            fileinfo.write('dir|  ' + os.path.join(root,name) + '\n')
    return result

def saveFile(pathfile,data,isxml=False,isunix=True):
    f = open(pathfile,"w")
    if isunix:
        rn = '\n'
    else:
        rn = '\r\n'
    if isxml :
        f.write('<?xml version="1.0" encoding="UTF-8" ?>'+rn)
    if type(data)==list:
        #print data
        for item in data:
            #print type(item),item
            if type(item) == str:
                f.write(item+rn)
            elif type(item) == unicode:
                f.write(item.encode("gbk")+rn)
            elif type(item) == int:
                line = "%i" % (item)
                f.write(line+rn)
            elif type(item) == float:
                line = "%.6f" % (item)
                f.write(line+rn)
    elif type(data)==str:
        f.write(data)
    elif type(data) == int:
        f.write("%i" % (data))
    elif type(data) == float:
        f.write("%.6f" % (data))
    f.close()


def is_cn_char(i):
    return 0x4e00<=ord(i)<0x9fa6

def is_cn_or_en(i):
    o = ord(i)
    return o<128 or 0x4e00<=o<0x9fa6

def ub64enc(s,urlsafe=False,utf8=True):
    if utf8:
        ss = s.encode("utf-8")
    else:
        ss = s
    if urlsafe:
        return base64.urlsafe_b64encode(ss)
    else:
        return base64.b64encode(ss)

def ub64dec(s,urlsafe=False,utf8=True):
    if urlsafe:
        ss = base64.urlsafe_b64decode(s)
    else:
        ss = base64.b64decode(s)
    if (utf8):
        return ss.decode("utf-8")
    else:
        return ss

def checkPath(pathfile,root):
    if (os.path.exists(root+'\\'+pathfile)):
        return True
    #elif (pathfile.find('\\')>=0 or pathfile.find('/')>=0 or pathfile.find('.')>=0):
    #    return True
    else:
        return False

def fixChinesePath(pathfile,urlsafe=True):
    pathfile = pathfile.replace('\\','/')
    paths = pathfile.split('/')
    py= pinyin.PinYin()
    py.load_word()
    ens=[]
    for p in paths:
        is_en = True
        en = ''
        cn = ''
        for c in p:
            if (is_cn_char(c)):
                is_en = False
                en = en+py.hanzi2pinyin(string=c)[0]
                cn = cn+unicode(c)
            else:
                en = en+c
                #cn = cn+c
        if not(is_en):
            #print cn
            en = "["+ub64enc(cn,urlsafe)+"]_"+en
            #print b64
            #print ub64dec(b64)
        ens.append(en)
    return '/'.join(ens)

def changeFileExt(pathfile,ext):
    return os.path.splitext(pathfile)[0]+ext;

def initlog(logfile="dbug.log"):
    import logging
    logger = logging.getLogger()
    hdlr = logging.FileHandler(logfile)
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.NOTSET)
    return logger