# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ceni_auto_test_main.ui'
#
# Created: Sun Apr 23 17:26:19 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ceniAutoTestMain(object):
    def setupUi(self, ceniAutoTestMain):
        ceniAutoTestMain.setObjectName("ceniAutoTestMain")
        ceniAutoTestMain.resize(187, 43)
        self.gridLayout = QtWidgets.QGridLayout(ceniAutoTestMain)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(ceniAutoTestMain)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(ceniAutoTestMain)
        QtCore.QMetaObject.connectSlotsByName(ceniAutoTestMain)

    def retranslateUi(self, ceniAutoTestMain):
        _translate = QtCore.QCoreApplication.translate
        ceniAutoTestMain.setWindowTitle(_translate("ceniAutoTestMain", "Form"))
        self.label.setText(_translate("ceniAutoTestMain", "CENI自动化测试,敬请期待..."))

