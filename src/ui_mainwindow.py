# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Apr 22 17:35:48 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 385)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 466, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuProject = QtWidgets.QMenu(self.menuBar)
        self.menuProject.setObjectName("menuProject")
        self.menuCase = QtWidgets.QMenu(self.menuBar)
        self.menuCase.setObjectName("menuCase")
        self.menuSetting = QtWidgets.QMenu(self.menuBar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNewProject = QtWidgets.QAction(MainWindow)
        self.actionNewProject.setObjectName("actionNewProject")
        self.actionDeleteProject = QtWidgets.QAction(MainWindow)
        self.actionDeleteProject.setObjectName("actionDeleteProject")
        self.actionSettingProject = QtWidgets.QAction(MainWindow)
        self.actionSettingProject.setObjectName("actionSettingProject")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNewUseCase = QtWidgets.QAction(MainWindow)
        self.actionNewUseCase.setObjectName("actionNewUseCase")
        self.actionDeleteUseCase = QtWidgets.QAction(MainWindow)
        self.actionDeleteUseCase.setObjectName("actionDeleteUseCase")
        self.actionNFCProject = QtWidgets.QAction(MainWindow)
        self.actionNFCProject.setObjectName("actionNFCProject")
        self.actionCENIProject = QtWidgets.QAction(MainWindow)
        self.actionCENIProject.setObjectName("actionCENIProject")
        self.actionSwitchProject = QtWidgets.QAction(MainWindow)
        self.actionSwitchProject.setObjectName("actionSwitchProject")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuProject.addAction(self.actionNewProject)
        self.menuProject.addAction(self.actionDeleteProject)
        self.menuProject.addAction(self.actionSettingProject)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionExit)
        self.menuCase.addAction(self.actionNewUseCase)
        self.menuCase.addAction(self.actionDeleteUseCase)
        self.menuSetting.addAction(self.actionNFCProject)
        self.menuSetting.addAction(self.actionCENIProject)
        self.menuSetting.addAction(self.actionSwitchProject)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuProject.menuAction())
        self.menuBar.addAction(self.menuCase.menuAction())
        self.menuBar.addAction(self.menuSetting.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuProject.setTitle(_translate("MainWindow", "项目(&P)"))
        self.menuCase.setTitle(_translate("MainWindow", "用例(&U)"))
        self.menuSetting.setTitle(_translate("MainWindow", "设置(&S)"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.actionNewProject.setText(_translate("MainWindow", "新建"))
        self.actionDeleteProject.setText(_translate("MainWindow", "删除"))
        self.actionSettingProject.setText(_translate("MainWindow", "设置"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionNewUseCase.setText(_translate("MainWindow", "新建"))
        self.actionDeleteUseCase.setText(_translate("MainWindow", "删除"))
        self.actionNFCProject.setText(_translate("MainWindow", "NFC项目"))
        self.actionCENIProject.setText(_translate("MainWindow", "CENI项目"))
        self.actionSwitchProject.setText(_translate("MainWindow", "交换机项目"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))

