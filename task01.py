# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

#strRemove = 'абв'
#strRemove = 'арри'
strRemove = input('Введите последовательность символов, слова, содержащие которую, необходимо удалить: ')

with open('text.txt', 'r', encoding='UTF-8') as file:
    data = file.read()

data = list(data.split())
print(data)

result = []
for i in data:
    if not strRemove in i:
        result.append(i)
print(result)


