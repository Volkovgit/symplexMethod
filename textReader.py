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


print(originalEquation)
print(matrix)