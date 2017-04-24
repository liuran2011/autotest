# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nfc_setting.ui'
#
# Created: Mon Apr 24 09:07:56 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_nfcProjectSetting(object):
    def setupUi(self, nfcProjectSetting):
        nfcProjectSetting.setObjectName("nfcProjectSetting")
        nfcProjectSetting.resize(209, 157)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(nfcProjectSetting.sizePolicy().hasHeightForWidth())
        nfcProjectSetting.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(nfcProjectSetting)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayoutTest = QtWidgets.QVBoxLayout()
        self.verticalLayoutTest.setObjectName("verticalLayoutTest")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(nfcProjectSetting)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(nfcProjectSetting)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayoutTest.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(nfcProjectSetting)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(nfcProjectSetting)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayoutTest.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(nfcProjectSetting)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(nfcProjectSetting)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayoutTest.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.okButton = QtWidgets.QPushButton(nfcProjectSetting)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_4.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(nfcProjectSetting)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_4.addWidget(self.cancelButton)
        self.verticalLayoutTest.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayoutTest, 0, 0, 1, 1)

        self.retranslateUi(nfcProjectSetting)
        QtCore.QMetaObject.connectSlotsByName(nfcProjectSetting)

    def retranslateUi(self, nfcProjectSetting):
        _translate = QtCore.QCoreApplication.translate
        nfcProjectSetting.setWindowTitle(_translate("nfcProjectSetting", "NFC"))
        self.label_4.setText(_translate("nfcProjectSetting", "<html><head/><body><p>项目:</p></body></html>"))
        self.label.setText(_translate("nfcProjectSetting", "租户:"))
        self.label_2.setText(_translate("nfcProjectSetting", "密码:"))
        self.okButton.setText(_translate("nfcProjectSetting", "确定"))
        self.cancelButton.setText(_translate("nfcProjectSetting", "取消"))

