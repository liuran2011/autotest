#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow
from env import ENV
from config import CONF

class AutoTest(object):
    def __init__(self):
        pass

    def main(self):
        app=QApplication(sys.argv)
        win=MainWindow()
        win.showMaximized()
        sys.exit(app.exec_()) 

if __name__=="__main__":
    AutoTest().main()
