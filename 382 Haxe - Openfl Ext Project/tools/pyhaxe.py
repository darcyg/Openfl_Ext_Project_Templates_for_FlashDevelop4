#-------------------------------------------------------------------------------
# Name:        中文1
# Purpose:
#
# Author:      Darcy.G
#
# Created:     16/07/2013
# Copyright:   (c) Darcy.G 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import os
import argparse
#from utils.baseutils import *
import utils.baseutils as baseutils
import utils.Global
import utils.haxeutils

def main():
    p = argparse.ArgumentParser(prog="pyhaxe",description=u"Haxe openfl 工程编译工具 v0.1",version="%(prog)s 0.1")
    #p.add_argument('-C','--command', default='compile', type=str, nargs='+',
    #    choices=['compile','gitlib'],
    #    metavar='CMD', help=u'command {compile,gitlib} / 命令')
    p.add_argument('-b','--build', action='store_true', default=False, help=u'build mode/ 仅编译')
    p.add_argument('-t','--test', action='store_true', default=False, help=u'test mode/ 测试模式')
    p.add_argument('-r','--run', action='store_true', default=False, help=u'run mode/ 仅运行')
    p.add_argument('-c','--clean', action='store_true', default=False, help=u'clean mode/ 清除模式')
    p.add_argument('-p','--project-file', default='build.xml', type=str, nargs=1, help=u'project file/ 工程文件')
    p.add_argument('-d','--project-demo-file', action='store_true', default=False, help=u'demo project file/ Demo工程文件')
    p.add_argument('--prefix-dir', default='../', type=str, nargs=1, help=u'project prefix dir/ 工程文件相对目录')
    p.add_argument('-a','--target-android', action='store_true', default=False, help=u'target android/ 安卓版本')
    p.add_argument('-f','--target-flash', action='store_true', default=False, help=u'target flash/ Flash版本')
    p.add_argument('-n','--target-neko', action='store_true', default=False, help=u'target android/ Neko版本')
    p.add_argument('-w','--target-windows', action='store_true', default=False, help=u'target windows/ Windows版本')
    p.add_argument('-u','--no-run', action='store_true', default=False, help=u'not run/ 仅生成编译命令不执行')

    #p.add_argument('-d','--source-dir', default='.\\src', type=str, nargs=1, help=u'source dir / 来源目录')
    #p.add_argument('-t','--temp-dir', default='.\\tmp', type=str, nargs=1, help=u'temp dir / 临时目录')
    #p.add_argument('-o','--target-dir', default='.\\out', type=str, nargs=1, help=u'target dir / 目的目录')
    #p.add_argument('-f','--force-del',  action='store_true', default=False, help=u'force remove dir / 删除目录')
    #p.add_argument('-s','--skip', default=0, type=int, nargs=1, help=u'min file id / 跳过多少条数据')
    #p.add_argument('-m','--max', default=99999999, type=int, nargs=1, help=u'max file id / 最大处理多少条数据')
    #p.add_argument('-S','--single-file', type=str, nargs=1, help=u'single file path / 单文件处理')

    # 这个函数将认识的和不认识的参数分开放进2个变量中
    args, remaining = p.parse_known_args(sys.argv)

    args.command = 'compile'
    args.prog = p.prog
    args.description = p.description
	
    haxecmd = utils.haxeutils.haxetools(args)
    haxecmd.doRun()

if __name__ == '__main__':
    main()
