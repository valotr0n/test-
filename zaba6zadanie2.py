text = "Нужно удалить    лишние пробелы  . ЗАчем? я сам не знаю."
new_text = ""
previous_char = ""
for char in text:
    if not (char == " " and previous_char == " "):
        new_text += char
    previous_char = char
print("Текст без лишних пробелов:", new_text)
