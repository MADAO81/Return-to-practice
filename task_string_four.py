# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = ("Lorem ipsum dolor sit amet consectetur adipiscing elit "
        "Integer porttitor bibendum nisi ut convallis ante")
# Примечание: для генерации текста можете воспользоваться
# сайтом: https://ru.lipsum.com/

res = text.split(" ")
print(res)