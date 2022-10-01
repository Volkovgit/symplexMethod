import copy
class Matrix():
    def __init__(self):
        self.matr = [[""]]
        self.equation = [1]
        self.currentItem = []
        self.bazisElem = []
        self.freeElem = []

    def setNewMatrix(self,matrix):
        deepCopyMatr = copy.deepcopy(matrix)
        self.matr = deepCopyMatr

    def getMatr(self):
        return self.matr

    def getEquation(self):
        return self.equation

    def crateMatrix(self, n=0, m=0):
        self.matr = [["" for i in range(m)] for j in range(n)]

    def setRowCount(self, count):
        self.matr = [["" for i in range(len(self.matr[0]))]
                     for j in range(count)]

    def setColumnCount(self, count):
        self.matr = [["" for i in range(count)] for j in range(len(self.matr))]

    def setMatrValue(self, i, j, number):
        self.matr[i][j] = int(number)

    def setEquationColumn(self, count):
        self.equation = ["" for i in range(count)]

    def setEquationValue(self, i, number):
        self.equation[i] = int(number)

    def setCurrentItem(self, i , j):
        self.currentItem = [i,j]
    def getCurrentItem(self):
        return self.currentItem

    def countBazisElem(self):
        self.bazisElem = [number+1 for number in range(0, len(self.matr[0]))]
        self.bazisElem.append("P")

    def countFreeElem(self):
        self.freeElem = [len(self.matr[0])+number for number in range(len(self.matr))]
        self.freeElem[len(self.matr)-1]="B"

    def countBRow(self):
        matrix = self.matr
        deepCopyMatr = copy.deepcopy(matrix)
        summArr = []
        for b in range(0, len(matrix[0])):
            summ = 0
            for a in range(0, len(matrix)):
                summ = summ + copy.copy(matrix[a][b])
            summArr.append(summ * -1)
            summ = 0
        deepCopyMatr.append(summArr)
        return deepCopyMatr

    # Считаем опорную строку

    def countSupportRow(self, matrix, i, j):
        deepCopyMatr = copy.deepcopy(matrix)
        deepCopyMatrRow = copy.deepcopy(matrix[i])
        supportElem = copy.copy(deepCopyMatr[i][j])
        deepCopyMatr[i] = [x/supportElem if index !=
                           j else x for index, x in enumerate(deepCopyMatrRow)]
        deepCopyMatr[i][j] = copy.copy(supportElem)
        return deepCopyMatr

    # Считаем опорный столбец

    def countSupportColumn(self, matrix, i, j):
        deepCopyMatr = copy.deepcopy(matrix)
        supportElem = copy.copy(deepCopyMatr[i][j])
        # print([[ind,x] for ind,x in enumerate(deepCopyMatr)])
        for a in range(0, len(matrix)):
            if (a != i):
                if (deepCopyMatr[a][j]/(supportElem * -1) == -0):
                    deepCopyMatr[a][j] = 0
                else:
                    deepCopyMatr[a][j] = deepCopyMatr[a][j]/(supportElem * -1)
        return deepCopyMatr

        return copy.deepcopy(matrix[i][j])

    # Считаем все остальные строки

    def countRows(self, matrix, i, j):
        deepCopyMatr = copy.deepcopy(matrix)
        supportRow = copy.copy(matrix[i])
        for a in range(len(matrix)):
            if (a != i):
                supportElem = copy.copy(matrix[a][j])

                deepCopyMatr[a] = [x-(supportElem * supportRow[index]) if index !=
                                   j else x for index, x in enumerate(deepCopyMatr[a])]
        return deepCopyMatr

    # Удаляем столбец из матрицы

    def deleteColumn(self, matrix, i, j):
        deepCopyMatrix = copy.deepcopy(matrix)
        for index in range(len(matrix)):
            deepCopyMatrix[index].pop(j)
        return deepCopyMatrix

    def changeFreeAndBazisMethod(self, bazisElem, freeElem, i, j):
        copyFreeElems = copy.deepcopy(freeElem)
        copyBazisElems = copy.deepcopy(bazisElem)
        iElem = copy.copy(copyBazisElems[j])
        jElem = copy.copy(copyFreeElems[i])
        copyBazisElems[j] = jElem
        copyFreeElems[i] = iElem
        copyBazisElems.pop(j)
        return copyBazisElems, copyFreeElems

    def filenameGenerate(self, originalEquation):
        filename = [str(elem)+'x'+str(index)
                    for index, elem in enumerate(originalEquation)]
        filename = 'F(x)='+''.join(filename)+'.txt'
        return filename

    # def iterationMethodBazis(self, matrix, i, j, bazisElem, freeElem):
    #     deepCopyMatrix = copy.deepcopy(matrix)
    #     deepCopyMatrix = countSupportRow(deepCopyMatrix, i, j)
    #     deepCopyMatrix = countRows(deepCopyMatrix, i, j)
    #     deepCopyMatrix = countSupportRow(deepCopyMatrix, i, j)
    #     bazisElem, freeElem = changeFreeAndBazisMethod(
    #         bazisElem, freeElem, i, j)
    #     deepCopyMatrix = deleteColumn(deepCopyMatrix, i, j)
    #     # logs(deepCopyMatrix, bazisElem, freeElem, originalEquation, i, j)
    #     return deepCopyMatrix, bazisElem, freeElem
