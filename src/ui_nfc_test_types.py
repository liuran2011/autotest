# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nfc_test_types.ui'
#
# Created: Fri Apr 28 09:17:27 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_nfcTestTypes(object):
    def setupUi(self, nfcTestTypes):
        nfcTestTypes.setObjectName("nfcTestTypes")
        nfcTestTypes.resize(96, 43)
        self.gridLayout = QtWidgets.QGridLayout(nfcTestTypes)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(nfcTestTypes)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(nfcTestTypes)
        QtCore.QMetaObject.connectSlotsByName(nfcTestTypes)

    def retranslateUi(self, nfcTestTypes):
        _translate = QtCore.QCoreApplication.translate
        nfcTestTypes.setWindowTitle(_translate("nfcTestTypes", "Form"))
        self.groupBox.setTitle(_translate("nfcTestTypes", "测试类型"))

