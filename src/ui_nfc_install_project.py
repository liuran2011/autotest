# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nfc_install_project.ui'
#
# Created: Thu Apr 27 09:21:37 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_nfcInstallProjectDialog(object):
    def setupUi(self, nfcInstallProjectDialog):
        nfcInstallProjectDialog.setObjectName("nfcInstallProjectDialog")
        nfcInstallProjectDialog.resize(267, 289)
        self.gridLayout = QtWidgets.QGridLayout(nfcInstallProjectDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(nfcInstallProjectDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.projectName = QtWidgets.QLineEdit(nfcInstallProjectDialog)
        self.projectName.setObjectName("projectName")
        self.horizontalLayout.addWidget(self.projectName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(nfcInstallProjectDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.projectType = QtWidgets.QLineEdit(nfcInstallProjectDialog)
        self.projectType.setEnabled(False)
        self.projectType.setObjectName("projectType")
        self.horizontalLayout_2.addWidget(self.projectType)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(nfcInstallProjectDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.tenantName = QtWidgets.QLineEdit(nfcInstallProjectDialog)
        self.tenantName.setObjectName("tenantName")
        self.horizontalLayout_4.addWidget(self.tenantName)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(nfcInstallProjectDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.password = QtWidgets.QLineEdit(nfcInstallProjectDialog)
        self.password.setObjectName("password")
        self.horizontalLayout_5.addWidget(self.password)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(nfcInstallProjectDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.keystoneURL = QtWidgets.QLineEdit(nfcInstallProjectDialog)
        self.keystoneURL.setObjectName("keystoneURL")
        self.horizontalLayout_6.addWidget(self.keystoneURL)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(nfcInstallProjectDialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.regionName = QtWidgets.QLineEdit(nfcInstallProjectDialog)
        self.regionName.setObjectName("regionName")
        self.horizontalLayout_7.addWidget(self.regionName)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(nfcInstallProjectDialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.publicNetwork = QtWidgets.QLineEdit(nfcInstallProjectDialog)
        self.publicNetwork.setObjectName("publicNetwork")
        self.horizontalLayout_8.addWidget(self.publicNetwork)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.okButton = QtWidgets.QPushButton(nfcInstallProjectDialog)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_3.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(nfcInstallProjectDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(nfcInstallProjectDialog)
        QtCore.QMetaObject.connectSlotsByName(nfcInstallProjectDialog)

    def retranslateUi(self, nfcInstallProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        nfcInstallProjectDialog.setWindowTitle(_translate("nfcInstallProjectDialog", "NFC安装测试"))
        self.label.setText(_translate("nfcInstallProjectDialog", "项目名称:"))
        self.label_2.setText(_translate("nfcInstallProjectDialog", "项目类型:"))
        self.label_3.setText(_translate("nfcInstallProjectDialog", "租户:"))
        self.label_4.setText(_translate("nfcInstallProjectDialog", "密码:"))
        self.label_5.setText(_translate("nfcInstallProjectDialog", "keystone URL:"))
        self.label_6.setText(_translate("nfcInstallProjectDialog", "区域:"))
        self.label_7.setText(_translate("nfcInstallProjectDialog", "外部网络:"))
        self.okButton.setText(_translate("nfcInstallProjectDialog", "确定"))
        self.cancelButton.setText(_translate("nfcInstallProjectDialog", "取消"))

