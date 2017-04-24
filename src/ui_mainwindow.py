# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Apr 24 18:30:57 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 429)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuProject = QtWidgets.QMenu(self.menuBar)
        self.menuProject.setObjectName("menuProject")
        self.menuCase = QtWidgets.QMenu(self.menuBar)
        self.menuCase.setObjectName("menuCase")
        self.menuSetting = QtWidgets.QMenu(self.menuBar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menu_L = QtWidgets.QMenu(self.menuBar)
        self.menu_L.setObjectName("menu_L")
        self.menu_V = QtWidgets.QMenu(self.menuBar)
        self.menu_V.setObjectName("menu_V")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.dockWidgetContents)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.gridLayout_2.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
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
        self.menuBar.addAction(self.menu_L.menuAction())
        self.menuBar.addAction(self.menu_V.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "自动化测试平台"))
        self.menuProject.setTitle(_translate("MainWindow", "项目(&P)"))
        self.menuCase.setTitle(_translate("MainWindow", "用例(&U)"))
        self.menuSetting.setTitle(_translate("MainWindow", "设置(&S)"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.menu_L.setTitle(_translate("MainWindow", "测试日志(&L)"))
        self.menu_V.setTitle(_translate("MainWindow", "视图(&V)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
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

