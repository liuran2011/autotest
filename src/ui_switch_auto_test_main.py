# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'switch_auto_test_main.ui'
#
# Created: Thu Apr 27 22:59:44 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_switchAutoTestMain(object):
    def setupUi(self, switchAutoTestMain):
        switchAutoTestMain.setObjectName("switchAutoTestMain")
        switchAutoTestMain.resize(197, 43)
        self.gridLayout = QtWidgets.QGridLayout(switchAutoTestMain)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(switchAutoTestMain)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(switchAutoTestMain)
        QtCore.QMetaObject.connectSlotsByName(switchAutoTestMain)

    def retranslateUi(self, switchAutoTestMain):
        _translate = QtCore.QCoreApplication.translate
        switchAutoTestMain.setWindowTitle(_translate("switchAutoTestMain", "Form"))
        self.label.setText(_translate("switchAutoTestMain", "交换机自动化测试,敬请期待..."))

