# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_project.ui'
#
# Created: Thu Apr 27 22:59:43 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_deleteProjectDialog(object):
    def setupUi(self, deleteProjectDialog):
        deleteProjectDialog.setObjectName("deleteProjectDialog")
        deleteProjectDialog.setWindowModality(QtCore.Qt.NonModal)
        deleteProjectDialog.resize(286, 323)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(deleteProjectDialog.sizePolicy().hasHeightForWidth())
        deleteProjectDialog.setSizePolicy(sizePolicy)
        deleteProjectDialog.setSizeGripEnabled(False)
        self.gridLayout_2 = QtWidgets.QGridLayout(deleteProjectDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(-1)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(deleteProjectDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(deleteProjectDialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(deleteProjectDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.projectList = QtWidgets.QListWidget(deleteProjectDialog)
        self.projectList.setObjectName("projectList")
        self.gridLayout.addWidget(self.projectList, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(deleteProjectDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteProjectButton = QtWidgets.QPushButton(deleteProjectDialog)
        self.deleteProjectButton.setObjectName("deleteProjectButton")
        self.horizontalLayout.addWidget(self.deleteProjectButton)
        self.cancelDeleteProjectButton = QtWidgets.QPushButton(deleteProjectDialog)
        self.cancelDeleteProjectButton.setObjectName("cancelDeleteProjectButton")
        self.horizontalLayout.addWidget(self.cancelDeleteProjectButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(deleteProjectDialog)
        QtCore.QMetaObject.connectSlotsByName(deleteProjectDialog)

    def retranslateUi(self, deleteProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        deleteProjectDialog.setWindowTitle(_translate("deleteProjectDialog", "删除项目"))
        self.label_2.setText(_translate("deleteProjectDialog", "项目类型:"))
        self.label.setText(_translate("deleteProjectDialog", "项目名称:"))
        self.deleteProjectButton.setText(_translate("deleteProjectDialog", "删除"))
        self.cancelDeleteProjectButton.setText(_translate("deleteProjectDialog", "取消"))

