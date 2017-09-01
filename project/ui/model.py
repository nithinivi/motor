# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1339, 733)
        MainWindow.setMaximumSize(QtCore.QSize(3840, 2160))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(450, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.serialTab = QtWidgets.QWidget()
        self.serialTab.setLocale(
            QtCore.QLocale(QtCore.QLocale.English,
                           QtCore.QLocale.UnitedKingdom))
        self.serialTab.setObjectName("serialTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.serialTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comPort = QtWidgets.QComboBox(self.serialTab)
        self.comPort.setCurrentText("")
        self.comPort.setObjectName("comPort")
        self.gridLayout_2.addWidget(self.comPort, 0, 0, 1, 2)
        self.serialBrowser = QtWidgets.QTextBrowser(self.serialTab)
        self.serialBrowser.setObjectName("serialBrowser")
        self.gridLayout_2.addWidget(self.serialBrowser, 1, 0, 1, 2)
        self.tabWidget.addTab(self.serialTab, "")
        self.generalTAb = QtWidgets.QWidget()
        self.generalTAb.setObjectName("generalTAb")
        self.tabWidget.addTab(self.generalTAb, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 4, 1)
        self.plotCtrl = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.plotCtrl.sizePolicy().hasHeightForWidth())
        self.plotCtrl.setSizePolicy(sizePolicy)
        self.plotCtrl.setMinimumSize(QtCore.QSize(0, 150))
        self.plotCtrl.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.plotCtrl.setFlat(True)
        self.plotCtrl.setObjectName("plotCtrl")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.plotCtrl)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addWidget(self.plotCtrl, 2, 2, 1, 1)
        self.plot = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.plot.sizePolicy().hasHeightForWidth())
        self.plot.setSizePolicy(sizePolicy)
        self.plot.setMinimumSize(QtCore.QSize(0, 500))
        self.plot.setObjectName("plot")
        self.gridLayout.addWidget(self.plot, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1339, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.serialTab),
            _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.generalTAb),
            _translate("MainWindow", "Tab 1"))
        self.plotCtrl.setTitle(_translate("MainWindow", "Plot Control"))


from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
