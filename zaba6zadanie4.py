n = 5
a = 2
d = 3
changes = []
current = a
for i in range(n):
    changes.append(current)
    current *= d
print(f'Прогрессия = {changes}')