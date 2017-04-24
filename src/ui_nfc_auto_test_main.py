# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nfc_auto_test_main.ui'
#
# Created: Mon Apr 24 10:41:22 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_nfcAutoTestMain(object):
    def setupUi(self, nfcAutoTestMain):
        nfcAutoTestMain.setObjectName("nfcAutoTestMain")
        nfcAutoTestMain.resize(209, 43)
        self.gridLayout = QtWidgets.QGridLayout(nfcAutoTestMain)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(nfcAutoTestMain)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(nfcAutoTestMain)
        QtCore.QMetaObject.connectSlotsByName(nfcAutoTestMain)

    def retranslateUi(self, nfcAutoTestMain):
        _translate = QtCore.QCoreApplication.translate
        nfcAutoTestMain.setWindowTitle(_translate("nfcAutoTestMain", "Form"))
        self.label.setText(_translate("nfcAutoTestMain", "NFC自动化测试项目,敬请期待..."))

