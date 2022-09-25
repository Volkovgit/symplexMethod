f = open('example.txt', 'r')
lines = f.readlines()
lines = [line.rstrip() for line in lines]


def readEquation(lines):
    originalEquation = lines[0].split(' ')
    del originalEquation[len(originalEquation)-1]
    originalEquation = [int(el) for el in originalEquation]
    return originalEquation


def readMatrix(lines):
    matrix = lines[1:]
    matrix =[elem.split(' ') for elem in matrix]
    for index,elements in enumerate(matrix):
        elements = [int(e) for e in elements]
        matrix[index]=elements
    return matrix


originalEquation = readEquation(lines)
matrix = readMatrix(lines)

f.close()
print(originalEquation)
# print(''.join(originalEquation))
print(matrix)



def logs(matrix,bazisElem,freeElem,originalEquation,i,j):
    strElem_format = 'Выбран элемент i:{i},j:{j}'
    strMatrix ='Базисные иксы после расчетов:'
    strMatrix += '\n| '+' | '.join([str(elem) for elem in bazisElem]) + ' |'
    strMatrix += '\nСвободные иксы после расчетов:'
    for index, elem in enumerate(matrix):
        print(freeElem[index], "|", elem)
    print('---')


bazisElem = [number+1 for number in range(0, len(matrix[0])-1)]
freeElem = [len(matrix[0])+number for number in range(len(matrix))]
strMatrix ='Базисные иксы после расчетов:'
strMatrix += '\n | '+' | '.join([str(elem) for elem in bazisElem]) + ' |'
for index, elem in enumerate(matrix):
    strMatrix += "\n"+str(freeElem[index])+"| "+ ' | '.join([str(e) for e in elem])
print(strMatrix)


