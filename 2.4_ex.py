words = input('Введите несколько слов через пробел: ').split()
for i, word in enumerate(words):
    print(f'{i + 1} - {word[:10]}')
