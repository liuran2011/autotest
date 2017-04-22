# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_project.ui'
#
# Created: Sat Apr 22 21:32:41 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settingProjectDialog(object):
    def setupUi(self, settingProjectDialog):
        settingProjectDialog.setObjectName("settingProjectDialog")
        settingProjectDialog.resize(282, 326)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settingProjectDialog.sizePolicy().hasHeightForWidth())
        settingProjectDialog.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(settingProjectDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(settingProjectDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.projectInput = QtWidgets.QLineEdit(settingProjectDialog)
        self.projectInput.setObjectName("projectInput")
        self.gridLayout.addWidget(self.projectInput, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(settingProjectDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(settingProjectDialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.settingProjectList = QtWidgets.QListWidget(settingProjectDialog)
        self.settingProjectList.setObjectName("settingProjectList")
        self.verticalLayout.addWidget(self.settingProjectList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.settingProjectButton = QtWidgets.QPushButton(settingProjectDialog)
        self.settingProjectButton.setObjectName("settingProjectButton")
        self.horizontalLayout.addWidget(self.settingProjectButton)
        self.cancelSettingButton = QtWidgets.QPushButton(settingProjectDialog)
        self.cancelSettingButton.setObjectName("cancelSettingButton")
        self.horizontalLayout.addWidget(self.cancelSettingButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(settingProjectDialog)
        QtCore.QMetaObject.connectSlotsByName(settingProjectDialog)

    def retranslateUi(self, settingProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        settingProjectDialog.setWindowTitle(_translate("settingProjectDialog", "设置项目"))
        self.label.setText(_translate("settingProjectDialog", "项目名称:"))
        self.label_2.setText(_translate("settingProjectDialog", "项目类型:"))
        self.settingProjectButton.setText(_translate("settingProjectDialog", "设置"))
        self.cancelSettingButton.setText(_translate("settingProjectDialog", "取消"))

