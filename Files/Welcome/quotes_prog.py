#напиши здесь свою программу
with open('quotes.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)

author = input('Введите автора данного отрывка:')

with open('quotes.txt', 'a', encoding='utf-8') as file:
    text = '\n(' + author + ')\n'
    file.write(text)

enter = input('Хотите ли добавить цитату?')
while enter == 'да':
    with open('quotes.txt', 'a', encoding='utf-8') as file:
        lyrics = input('Введите цитату:')
        author = input('Введите автора:')
        text = lyrics + '\n(' + author + ')\n'
        file.write(text)
    enter = input('Хотите ли добавить цитату?')