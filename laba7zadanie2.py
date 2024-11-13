сapitals = {
    'Россия': 'Москва',
    'США': 'Вашингтон',
    'Франция': 'Париж',
    'Германия': 'Берлин',
    'Китай': 'Пекин',
    'Япония': 'Токио',
    'Италия': 'Рим',
    'Испания': 'Мадрид',
    'Канада': 'Оттава',
    'Бразилия': 'Бразилиа'
}
country = input('Введите название страны: ')
capital = сapitals.get(country)
if country[-1] in ['я', 'й']:
    modifiedCountry = country[:-1] + 'и'
else:
    modifiedCountry = country

if capital:
    print(f'Столица {modifiedCountry} - {capital}.')
else:
    print(f'Вашей страны нету в словаре.')

