# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_project.ui'
#
# Created: Sat Apr 22 17:35:48 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_deleteProjectDialog(object):
    def setupUi(self, deleteProjectDialog):
        deleteProjectDialog.setObjectName("deleteProjectDialog")
        deleteProjectDialog.setWindowModality(QtCore.Qt.NonModal)
        deleteProjectDialog.resize(282, 315)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(deleteProjectDialog.sizePolicy().hasHeightForWidth())
        deleteProjectDialog.setSizePolicy(sizePolicy)
        deleteProjectDialog.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(deleteProjectDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(-1)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(deleteProjectDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(deleteProjectDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.projectList = QtWidgets.QListWidget(deleteProjectDialog)
        self.projectList.setObjectName("projectList")
        self.verticalLayout.addWidget(self.projectList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteProjectButton = QtWidgets.QPushButton(deleteProjectDialog)
        self.deleteProjectButton.setObjectName("deleteProjectButton")
        self.horizontalLayout.addWidget(self.deleteProjectButton)
        self.cancelDeleteProjectButton = QtWidgets.QPushButton(deleteProjectDialog)
        self.cancelDeleteProjectButton.setObjectName("cancelDeleteProjectButton")
        self.horizontalLayout.addWidget(self.cancelDeleteProjectButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(deleteProjectDialog)
        QtCore.QMetaObject.connectSlotsByName(deleteProjectDialog)

    def retranslateUi(self, deleteProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        deleteProjectDialog.setWindowTitle(_translate("deleteProjectDialog", "删除项目"))
        self.label.setText(_translate("deleteProjectDialog", "请输入项目:"))
        self.deleteProjectButton.setText(_translate("deleteProjectDialog", "删除"))
        self.cancelDeleteProjectButton.setText(_translate("deleteProjectDialog", "取消"))

