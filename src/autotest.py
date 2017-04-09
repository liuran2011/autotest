#!/usr/bin/env python

import sys
from utils import *

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUiType

app=QApplication(sys.argv)
form_class,base_class=loadUiType(uipath(MAIN_WINDOW_UI))

class MainWindow(QMainWindow,form_class):
    def __init__(self,*args):
        super(QMainWindow,self).__init__(*args)

        self.setupUi(self)

window=MainWindow()
window.show()
sys.exit(app.exec_())
