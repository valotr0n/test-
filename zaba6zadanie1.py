string = 'исаев валерий учится писать программы, студент ВМО-011'
count = 0
for char in string:
    if char == ',':
        break
    if char == 'и':
        count += 1
print(count)