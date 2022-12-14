# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_2.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Console = QtWidgets.QListWidget(self.centralwidget)
        self.Console.setGeometry(QtCore.QRect(-5, 491, 1001, 71))
        self.Console.setObjectName("Console")
        self.printMatrix = QtWidgets.QPushButton(self.centralwidget)
        self.printMatrix.setGeometry(QtCore.QRect(10, 430, 171, 41))
        self.printMatrix.setObjectName("printMatrix")
        self.saveSettings = QtWidgets.QPushButton(self.centralwidget)
        self.saveSettings.setGeometry(QtCore.QRect(10, 140, 91, 41))
        self.saveSettings.setObjectName("saveSettings")
        self.variableCount = QtWidgets.QSpinBox(self.centralwidget)
        self.variableCount.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.variableCount.setMinimum(1)
        self.variableCount.setMaximum(16)
        self.variableCount.setObjectName("variableCount")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 101, 16))
        self.label_2.setObjectName("label_2")
        self.limitCount = QtWidgets.QSpinBox(self.centralwidget)
        self.limitCount.setGeometry(QtCore.QRect(10, 110, 61, 21))
        self.limitCount.setMinimum(1)
        self.limitCount.setMaximum(16)
        self.limitCount.setObjectName("limitCount")
        self.tableEquaion = QtWidgets.QTableWidget(self.centralwidget)
        self.tableEquaion.setGeometry(QtCore.QRect(310, 20, 671, 71))
        self.tableEquaion.setObjectName("tableEquaion")
        self.tableEquaion.setColumnCount(0)
        self.tableEquaion.setRowCount(0)
        self.matrixInput = QtWidgets.QTableWidget(self.centralwidget)
        self.matrixInput.setGeometry(QtCore.QRect(310, 100, 671, 311))
        self.matrixInput.setObjectName("matrixInput")
        self.matrixInput.setColumnCount(0)
        self.matrixInput.setRowCount(0)
        self.countIteration = QtWidgets.QPushButton(self.centralwidget)
        self.countIteration.setGeometry(QtCore.QRect(10, 190, 91, 31))
        self.countIteration.setObjectName("countIteration")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.printMatrix.setText(_translate("MainWindow", "?????????????? ?? ?????????????? ??????????????"))
        self.saveSettings.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "?????????? ????????????????????"))
        self.label_2.setText(_translate("MainWindow", "?????????? ??????????????????????"))
        self.countIteration.setText(_translate("MainWindow", "??????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
