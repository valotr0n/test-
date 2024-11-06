text = "Нужно удалить    лишние пробелы  . ЗАчем? я сам не знаю."
newTxt = ''
proshliyChar = ''
for char in text:
    if not(char == ' ' and proshliyChar == ' '):
        newTxt += char
    proshliyChar = char
print('Текст без лишних пробелов: ', newTxt)


