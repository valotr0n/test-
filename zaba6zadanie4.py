n = int(input('Введите колечество значений в массив: '))
a = int(input('Введите число, которое будет умножаться: '))
d = int(input('Введите число, на которое будет умножаться: '))
changes = []
current = a
for i in range(n):
    changes.append(current)
    current *= d
print(f'Прогрессия = {changes}')