A = [[1 , 2 , 3],
     [4 , 6 , 1],
     [5 , 8 , 6]]

print("Матрица A:")
for value in A:
    print(value)

sumMain = 0
for i in range(len(A)):
    sumMain += A[i][i]
sumSec = 0

n = len(A)
for i in range(n):
    sumSec += A[i][n-1-i]
print(f'Сумма элементов основной диагонали: {sumMain}')
print(f'Сумма элементов побочной диагонали: {sumSec}')
