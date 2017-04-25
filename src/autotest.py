#!/usr/bin/env python

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow
from env import ENV
from config import CONF
from test_case_manager import TM

class AutoTest(object):
    def __init__(self):
        pass

    def main(self):
        app=QApplication(sys.argv)
        win=MainWindow()
        win.showMaximized()
        ret=app.exec_()
        TM.destroy()
        sys.exit(ret) 

if __name__=="__main__":
    AutoTest().main()
