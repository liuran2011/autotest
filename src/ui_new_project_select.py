# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_project_select.ui'
#
# Created: Mon Apr 24 21:45:43 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newProjectSelect(object):
    def setupUi(self, newProjectSelect):
        newProjectSelect.setObjectName("newProjectSelect")
        newProjectSelect.resize(282, 284)
        self.gridLayout = QtWidgets.QGridLayout(newProjectSelect)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(newProjectSelect)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(newProjectSelect)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okButton = QtWidgets.QPushButton(newProjectSelect)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(newProjectSelect)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(newProjectSelect)
        QtCore.QMetaObject.connectSlotsByName(newProjectSelect)

    def retranslateUi(self, newProjectSelect):
        _translate = QtCore.QCoreApplication.translate
        newProjectSelect.setWindowTitle(_translate("newProjectSelect", "项目类型"))
        self.label.setText(_translate("newProjectSelect", "请选择项目类型:"))
        self.okButton.setText(_translate("newProjectSelect", "确定"))
        self.cancelButton.setText(_translate("newProjectSelect", "取消"))

