import re


def isCyrillic(word):
    return bool(re.search('[а-яА-Я]', word))    #проверка на кириллицу взята с просторов интернета


english_dictionary = dict()
english_dictionary[1] = 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'
english_dictionary[2] = 'D', 'G'
english_dictionary[3] = 'B', 'C', 'M', 'P'
english_dictionary[4] = 'F', 'H', 'V', 'W', 'Y'
english_dictionary[5] = 'K'
english_dictionary[8] = 'J', 'X'
english_dictionary[10] = 'Q', 'Z'
russian_dictionary = dict()
russian_dictionary[1] = 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'
russian_dictionary[2] = 'Д', 'К', 'Л', 'М', 'П', 'У'
russian_dictionary[3] = 'Б', 'Г', 'Ё', 'Ь', 'Я'
russian_dictionary[4] = 'Й', 'Ы'
russian_dictionary[5] = 'Ж', 'З', 'Х', 'Ц', 'Ч'
russian_dictionary[8] = 'Ш', 'Э', 'Ю'
russian_dictionary[10] = 'Ф', 'Щ', 'Ъ'
word = input('Введите слово: ').upper()
print(word)
scrabble = []
if isCyrillic(word):
    for i in word:
        for k, v in russian_dictionary.items():
            if i in v:
                scrabble.append(k)
    print(sum(scrabble))
else:
    for i in word:
        for k, v in english_dictionary.items():
            if i in v:
                scrabble.append(k)
    print(sum(scrabble))