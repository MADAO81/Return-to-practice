# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = ("Lorem ipsum dolor sit amet consectetur adipiscing elit "
        "Integer porttitor bibendum nisi ut convallis ante")
# Примечание: для генерации текста можете воспользоваться
# сайтом: https://ru.lipsum.com/

words = text.split(" ")
num_long_words = 0
for word in words:
    if len(word) > 5:
        num_long_words +=1
print(num_long_words)
