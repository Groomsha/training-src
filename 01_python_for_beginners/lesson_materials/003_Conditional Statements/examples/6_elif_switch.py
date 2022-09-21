print('''\nМеню:\n\t1. Файл\n\t2. Вид\n\t3. Выход\n''')

choice = int(input('Ваш выбор: '))

if choice == 1:
    print('Вы выбрали пункт меню "Файл"')
elif choice == 2:
    print('Вы открыли меню "Вид"')
elif choice == 3:
    print('Завершение.')
else:
    print('Некорректный выбор')
