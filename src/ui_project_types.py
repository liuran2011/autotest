# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_types.ui'
#
# Created: Sun Apr 23 16:31:54 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_projectTypes(object):
    def setupUi(self, projectTypes):
        projectTypes.setObjectName("projectTypes")
        projectTypes.resize(139, 62)
        self.gridLayout_2 = QtWidgets.QGridLayout(projectTypes)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(projectTypes)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(projectTypes)
        QtCore.QMetaObject.connectSlotsByName(projectTypes)

    def retranslateUi(self, projectTypes):
        _translate = QtCore.QCoreApplication.translate
        projectTypes.setWindowTitle(_translate("projectTypes", "Form"))
        self.groupBox.setTitle(_translate("projectTypes", "请选择项目类型:"))

