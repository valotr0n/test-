import random
def findMinElement(matrix):
    minElement = float('inf')
    pos = (0,0)
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val < minElement:
                minElement = val
                pos = (i,j) 
    return minElement, pos

A = [[random.randint(0,100) for i in range(10)] for j in range(5)]
B = [[random.randint(0,100) for i in range(4)] for j in range(10)]
minElement_A, pos_A = findMinElement(A)
print(f'Минимальный элемент в матрице А: {minElement_A}, на позиции {pos_A}')
minElement_B, pos_B = findMinElement(B)
print(f'Минимальный элемент в матрице B: {minElement_B}, на позиции {pos_B}')