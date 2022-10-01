import copy

from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from Matrix import Matrix
from interface import Ui_MainWindow
from test import changeFreeAndBazisMethod, countRows, countSupportRow, deleteColumn




class App(QtWidgets.QMainWindow, Matrix):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.matr = Matrix()
        self.UI()

        self.drawMatrix()
        self.drawEquation()

    def UI(self):

        variableCount = self.ui.variableCount
        limitCount = self.ui.limitCount

        # Окно ввода коэфф. уравнения
        equation = self.ui.tableEquaion
        equation.setRowCount(1)
        # Окно матрицы ограничений
        matrInput = self.ui.matrixInput
        # Кнопка печати матрицы в консоли
        printMatrix = self.ui.printMatrix

        # Сохранение всего
        saveSettings = self.ui.saveSettings
        # iteration count button
        iterationCount = self.ui.countIteration

        # Отслеживаем изменения ограничений и динамически меняем матрицу
        variableCount.valueChanged.connect(self.setMatrixColumnCount)
        limitCount.valueChanged.connect(self.setMatrixRowCount)
        variableCount.valueChanged.connect(self.setEquationColumnCount)
        # при каждом изменении отрисовываем таблицу заново
        variableCount.valueChanged.connect(self.drawMatrix)
        variableCount.valueChanged.connect(self.drawEquation)
        limitCount.valueChanged.connect(self.drawMatrix)

        # Отслеживаем ввод коэф. пользователем, проверяем, вносим в матрицу
        matrInput.itemChanged.connect(self.checkNewItem)
        equation.itemChanged.connect(self.checkNewItem)

        # сохраняем то что ввел пользователь и запрещаем новый ввод
        saveSettings.clicked.connect(self.setMatrix)
        saveSettings.clicked.connect(self.setEquationItems)
        saveSettings.clicked.connect(self.blockInput)
        saveSettings.clicked.connect(self.hideEquation)
        saveSettings.clicked.connect(self.countSevedTable)

        # печать данных в консоль
        printMatrix.clicked.connect(self.drawMatrixConsole)

        # print item on click
        matrInput.itemClicked.connect(self.printItemClick)
        equation.itemClicked.connect(self.printItemClick)


        # считаем итерацию метода базиса
        # iterationCount.clicked.connect(self.matrCount)

    def printNewMatrix(self):
        self.drawMatrix()
        for i in range(0,len(self.matr.getMatr())):
            for j in range(0,len(self.matr.getMatr()[0])):
                self.ui.matrixInput.setItem(i,j,QtWidgets.QTableWidgetItem(str(self.matr.getMatr()[i][j])))

    def countSevedTable(self):
        self.matr.setNewMatrix(self.matr.countBRow())
        self.matr.countBazisElem()
        self.matr.countFreeElem()
        print(self.matr.bazisElem)
        print(self.matr.freeElem)
        self.printNewMatrix()

    def hideEquation(self):
        self.ui.tableEquaion.hide()

    def printItemClick(self,item):
        print(item.text())

    def blockInput(self):
        self.ui.matrixInput.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableEquaion.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

    def checkNewItem(self, item):
        text = item.text()
        if (len(text) != 0):
            try:
                int(text)
                self.ui.saveSettings.setEnabled(True)
            except ValueError:
                self.ui.Console.addItem(
                    "Вы ввели не число \"" + text + "\"")
                self.ui.saveSettings.setEnabled(False)

    def checkAllItems(self):
        try:
            for i in range(self.ui.matrixInput.rowCount()):
                for j in range(self.ui.matrixInput.columnCount()):
                    if (self.ui.matrixInput.item(i, j) != None):
                        int(self.ui.matrixInput.item(i, j).text())
                    else:
                        self.ui.Console.addItem(
                            "Есть незаполненный элемент")
                        return False
        except ValueError:
            self.ui.Console.addItem(
                "В матрице есть не число")
            return False
        return True

    def setMatrixRowCount(self, value):
        self.matr.setRowCount(value)

    def setMatrixColumnCount(self, value):
        self.matr.setColumnCount(value)

    def drawMatrix(self):
        matrInput = self.ui.matrixInput
        matrInput.setRowCount(len(self.matr.getMatr()))
        matrInput.setColumnCount(len(self.matr.getMatr()[0]))

    def drawEquation(self):
        equationInput = self.ui.tableEquaion
        equationInput.setColumnCount(len(self.matr.getMatr()[0]))

    def setEquationColumnCount(self, value):
        print(value)
        self.matr.setEquationColumn(value)

    def checkEquationItems(self):
        equationInput = self.ui.tableEquaion
        try:
            for i in range(equationInput.rowCount()):
                for j in range(equationInput.columnCount()):
                    if (equationInput.item(i, j) != None):
                        int(equationInput.item(i, j).text())
                    else:
                        self.ui.Console.addItem(
                            "Есть незаполненный элемент")
                        return False
        except ValueError:
            self.ui.Console.addItem(
                "Есть не число")
            return False
        return True

    def setEquationItems(self):
        equationInput = self.ui.tableEquaion
        if (self.checkEquationItems()):
            for i in range(equationInput.rowCount()):
                for j in range(equationInput.columnCount()):
                    self.matr.setEquationValue(
                        j, equationInput.item(i, j).text())

    def setMatrix(self):
        if (self.checkAllItems()):
            for i in range(self.ui.matrixInput.rowCount()):
                for j in range(self.ui.matrixInput.columnCount()):
                    self.matr.setMatrValue(
                        i, j, self.ui.matrixInput.item(i, j).text())

    def drawMatrixConsole(self):
        print(self.matr.getEquation())
        print(self.matr.getMatr())









app = QtWidgets.QApplication([])
application = App()
application.show()

sys.exit(app.exec())
