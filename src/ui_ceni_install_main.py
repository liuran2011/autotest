# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ceni_install_main.ui'
#
# Created: Thu Apr 27 22:59:44 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ceniInstallMain(object):
    def setupUi(self, ceniInstallMain):
        ceniInstallMain.setObjectName("ceniInstallMain")
        ceniInstallMain.resize(200, 43)
        self.gridLayout = QtWidgets.QGridLayout(ceniInstallMain)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(ceniInstallMain)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(ceniInstallMain)
        QtCore.QMetaObject.connectSlotsByName(ceniInstallMain)

    def retranslateUi(self, ceniInstallMain):
        _translate = QtCore.QCoreApplication.translate
        ceniInstallMain.setWindowTitle(_translate("ceniInstallMain", "Form"))
        self.label.setText(_translate("ceniInstallMain", "CENI自动安装测试,敬请期待..."))

