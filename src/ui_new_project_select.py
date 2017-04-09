# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_project_select.ui'
#
# Created: Sun Apr  9 23:32:23 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newProjectSelect(object):
    def setupUi(self, newProjectSelect):
        newProjectSelect.setObjectName("newProjectSelect")
        newProjectSelect.resize(186, 229)
        self.gridLayout_2 = QtWidgets.QGridLayout(newProjectSelect)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(newProjectSelect)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okButton = QtWidgets.QPushButton(newProjectSelect)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(newProjectSelect)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(newProjectSelect)
        QtCore.QMetaObject.connectSlotsByName(newProjectSelect)

    def retranslateUi(self, newProjectSelect):
        _translate = QtCore.QCoreApplication.translate
        newProjectSelect.setWindowTitle(_translate("newProjectSelect", "项目类型"))
        self.groupBox.setTitle(_translate("newProjectSelect", "请选择项目类型:"))
        self.radioButton.setText(_translate("newProjectSelect", "NFC安装"))
        self.radioButton_2.setText(_translate("newProjectSelect", "NFC自动化测试"))
        self.radioButton_3.setText(_translate("newProjectSelect", "CENI安装"))
        self.radioButton_4.setText(_translate("newProjectSelect", "CENI自动化测试"))
        self.radioButton_5.setText(_translate("newProjectSelect", "交换机自动化测试"))
        self.okButton.setText(_translate("newProjectSelect", "确定"))
        self.cancelButton.setText(_translate("newProjectSelect", "取消"))

