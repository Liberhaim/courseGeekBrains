"""
 Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества
 слов в каждой строке.
"""
with open("les_5.6_input.txt", 'r', encoding='utf_8') as f:
    text = f.read()
count = 0
for line in text:
    count += 1

number_of_words_per_line = (text.count(" ") + 1)
number_of_lines = text.count("\n") + 1
print(f'Количество строк: {number_of_lines}, количество слов в строке: {number_of_words_per_line}')
