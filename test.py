
import copy

matrix = [[1, 1, 2, 0, 0, 6], [0, 2, 2, -1, 1, 6], [1, -1, 6, 1, 1, 12]]
originalEquation = [-1, -1, -1, -1, -1]




# Функции для просчета матрицы

# Считаем нижнюю линию матрицы


def countBRow(matrix):
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


def countSupportRow(matrix, i, j):
    deepCopyMatr = copy.deepcopy(matrix)
    deepCopyMatrRow = copy.deepcopy(matrix[i])
    supportElem = copy.copy(deepCopyMatr[i][j])
    deepCopyMatr[i] = [x/supportElem if index !=
                       j else x for index, x in enumerate(deepCopyMatrRow)]
    deepCopyMatr[i][j] = copy.copy(supportElem)
    return deepCopyMatr

# Считаем опорный столбец


def countSupportColumn(matrix, i, j):
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


def countRows(matrix, i, j):
    deepCopyMatr = copy.deepcopy(matrix)
    supportRow = copy.copy(matrix[i])
    for a in range(len(matrix)):
        if (a != i):
            supportElem = copy.copy(matrix[a][j])

            deepCopyMatr[a] = [x-(supportElem * supportRow[index]) if index !=
                               j else x for index, x in enumerate(deepCopyMatr[a])]
    return deepCopyMatr

# Удаляем столбец из матрицы


def deleteColumn(matrix, i, j):
    deepCopyMatrix = copy.deepcopy(matrix)
    for index in range(len(matrix)):
        deepCopyMatrix[index].pop(j)
    return deepCopyMatrix


def changeFreeAndBazisMethod(bazisElem, freeElem, i, j):
    copyFreeElems = copy.deepcopy(freeElem)
    copyBazisElems = copy.deepcopy(bazisElem)
    iElem = copy.copy(copyBazisElems[j])
    jElem = copy.copy(copyFreeElems[i])
    copyBazisElems[j] = jElem
    copyFreeElems[i] = iElem
    copyBazisElems.pop(j)
    return copyBazisElems, copyFreeElems


def filenameGenerate(originalEquation):
    filename = [str(elem)+'x'+str(index) for index,elem in enumerate(originalEquation)]
    filename = 'F(x)='+''.join(filename)+'.txt'
    return filename
    

def logs(matrix,bazisElem,freeElem,originalEquation,i,j):
    filename= filenameGenerate(originalEquation)
    strMatrix ='Choosed element i:'+str(i)+' j:'+str(j)+' = '+str(matrix[i][j])
    strMatrix += '\nMatrix after counting: \n'
    strMatrix += '\n | '+' | '.join([str(elem) for elem in bazisElem]) + ' |'
    for index, elem in enumerate(matrix):
        strMatrix += "\n"+str(freeElem[index])+"| "+ ' | '.join([str(e) for e in elem])
    with open(filename, 'a') as the_file:
        the_file.write(strMatrix+'\n')

def iterationMethodBazis(matrix, i, j, bazisElem, freeElem):
    deepCopyMatrix = copy.deepcopy(matrix)
    deepCopyMatrix = countSupportRow(deepCopyMatrix, i, j)
    deepCopyMatrix = countRows(deepCopyMatrix, i, j)
    deepCopyMatrix = countSupportColumn(deepCopyMatrix, i, j)
    bazisElem, freeElem = changeFreeAndBazisMethod(bazisElem, freeElem, i, j)
    deepCopyMatrix = deleteColumn(deepCopyMatrix, i, j)
    logs(deepCopyMatrix,bazisElem,freeElem,originalEquation,i,j)
    return deepCopyMatrix, bazisElem, freeElem


matrix = countBRow(matrix)
bazisElem = [number+1 for number in range(0, len(matrix[0])-1)]
freeElem = [len(matrix[0])+number for number in range(len(matrix))]
freeElem[len(matrix)-1]="B"
bazisElem.append("P")



print('   ', bazisElem)
print("Исходная таблица:")
for index, elem in enumerate(matrix):
    print(freeElem[index], "|", elem)
print('---')
print("Проверка, 3 шага метода искусственного базиса")
firstIter, bazisElem, freeElem = iterationMethodBazis(
    matrix, 0, 0, bazisElem, freeElem)

firstIter, bazisElem, freeElem = iterationMethodBazis(
    firstIter, 2, 3, bazisElem, freeElem)

firstIter, bazisElem, freeElem = iterationMethodBazis(
    firstIter, 1, 0, bazisElem, freeElem)
print('---')
print('   ', bazisElem)
for index, elem in enumerate(firstIter):
    print(freeElem[index], "|", elem)
print('---')





def countKoeffBline(bazis,free):
  bazisElem = copy.deepcopy(bazis)
  freeElem = copy.deepcopy(free)
  bazisElem.pop(len(bazisElem)-1)
  freeElem.pop(len(freeElem)-1)
  summArr = [originalEquation[e-1] for index,e in enumerate(bazisElem)]
  for bInd,bElem in enumerate(bazisElem):
    summ = 0
    for fInd,fElem in enumerate(freeElem):
      summ = summ+(firstIter[fInd][bInd]*originalEquation[fElem-1])
    summ = originalEquation[bElem-1]-summ
    summArr[bInd] = summ

  C=0
  for fInd,fElem in enumerate(freeElem):
    C = C-(firstIter[fInd][len(firstIter[0])-1]*originalEquation[fElem-1])
  summArr.append(C)
  return summArr



def iterationMethodOriginal(matrix, i, j, bazisElem, freeElem):
    deepCopyMatrix = copy.deepcopy(matrix)
    deepCopyMatrix = countSupportRow(deepCopyMatrix, i, j)
    deepCopyMatrix = countRows(deepCopyMatrix, i, j)
    deepCopyMatrix = countSupportColumn(deepCopyMatrix, i, j)
    bazisElem, freeElem = changeFreeAndOriginal(bazisElem, freeElem, i, j)
    logs(deepCopyMatrix,bazisElem,freeElem,originalEquation,i,j)
    return deepCopyMatrix, bazisElem, freeElem


def changeFreeAndOriginal(bazisElem, freeElem, i, j):
    copyFreeElems = copy.deepcopy(freeElem)
    copyBazisElems = copy.deepcopy(bazisElem)
    iElem = copy.copy(copyBazisElems[j])
    jElem = copy.copy(copyFreeElems[i])
    copyBazisElems[j] = jElem
    copyFreeElems[i] = iElem
    return copyBazisElems, copyFreeElems



print('Переход к начальной задаче')
print('   ', bazisElem)
for index, elem in enumerate(firstIter):
    print(freeElem[index], "|", elem)
print('---')

firstIter[len(firstIter)-1]=countKoeffBline(bazisElem,freeElem)

firstIter,bazisElem,freeElem = iterationMethodOriginal(firstIter,0,1,bazisElem,freeElem)

print('   ', bazisElem)
for index, elem in enumerate(firstIter):
    print(freeElem[index], "|", elem)
print('---')



# тут формируем ответ
# answer = [0 for e in originalEquation]
# bazisElem.pop(len(bazisElem)-1)
# freeElem.pop(len(freeElem)-1)
# for i in range(len(firstIter)-1):
#   answer[freeElem[i]-1] = firstIter[i][len(firstIter[0])-1]


def createAnswer():
  originalEquation
  bazisElem
  freeElem
  firstIter

  answer = [0 for e in originalEquation]
  bazisElem.pop(len(bazisElem)-1)
  freeElem.pop(len(freeElem)-1)
  for i in range(len(firstIter)-1):
    answer[freeElem[i]-1] = firstIter[i][len(firstIter[0])-1]
  return answer




def createSummF():
  summ = 0
  for i in range(0,len(originalEquation)):
    summ = summ + (originalEquation[i]*answer[i])
  return summ

# Считаю исходное уравнение
# summ = 0
# for i in range(0,len(originalEquation)):
#   summ = summ + (originalEquation[i]*answer[i])

answer = createAnswer()
summ = createSummF()


print('Ответ : ',answer,"F(x)=",summ)

answer = [str(el) for el in answer]
strA = '('+','.join(answer)+')'+'  F(x)='+str(summ)

filename= filenameGenerate(originalEquation)
with open(filename, 'a') as the_file:
        the_file.write('Answer:+'+strA )