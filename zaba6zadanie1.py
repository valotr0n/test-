sentence = "Исаев Валерий, студент ВМО-011"
count_i = 0
for char in sentence:
    if char == ',':
        break
    if char == 'и':
        count_i += 1
print("Количество букв 'И' перед первой запятой:", count_i)
