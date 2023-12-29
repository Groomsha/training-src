"""
Запросити у користувача введення індексу (числа) через input. Якщо за введеним
індексом можна вивести слово зі списку words, вивести його. Якщо індекс більший
за допустимий, вивести повідомлення "У списку words немає такого індексу".


Приклад роботи завдання
$ python task_07.py
Введіть індекс: 0
word1

$ python task_07.py
Введіть індекс: 2
word3

$ python task_07.py
Введіть індекс: 5
У списку words немає такого індексу

Завдання можна ускладнити, додавши підтримку негативних індексів:

$ python task_07.py
Введіть індекс: -1
word3

$ python task_07.py
Введіть індекс: -3
word1

$ python task_07.py
Введіть індекс: -4
У списку words немає такого індексу
"""
words = ["word1", "word2", "word3"]
target: int = int(input("Введіть індекс: "))

if target == 0 or target == -3:
    print(words[0])
elif target == 1 or target == -2:
    print(words[1])
elif target == 2 or target == -1:
    print(words[2])
else:
    print("У списку words немає такого індексу")
