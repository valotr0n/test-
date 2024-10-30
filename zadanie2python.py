n = int(input('Введите значение n: '))
x = float(input('Введите значение x: '))
s = 0
fact = 1
for i in range(1, n+1):
    fact *= i
    calculate = (x**i)/fact
    s += calculate
print(f'Сумма = {s}')
