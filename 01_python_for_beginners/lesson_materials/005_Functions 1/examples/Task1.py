def menu():
    print('МЕНЮ:\n\t1. Предметы\n\t2. Расписание звонков\n\t3. Преподавательский состав\n\t4. Контактные данные\n\t0. Выход\n')


def subjects():
    print('1. Математика\n2. Русский язык\n3. Литература\n4. Физика\n')


def bells_schedule():
    print('1. 08:30-09:15\n2. 08:30-09:15\n3. 08:30-09:15\n4. 08:30-09:15\n')


def teachers():
    print('1. Иванова М.Н.\n2. Петрова О.В.\n3. Николаенко В.А.\n4. Сидоров И.И.\n')


def contacts():
    print('1. 123321\n2. 123123\n3. 123432\n4. 123678\n')


def error():
    print('Выберите корректный пункт меню!\n')


menu()
n = int(input('Выберите пункт меню (0 - стоп): '))
while n != 0:
    if n == 1:
        subjects()
        menu()
    elif n == 2:
        bells_schedule()
        menu()
    elif n == 3:
        teachers()
        menu()
    elif n == 4:
        contacts()
        menu()
    else:
        error()
        menu()
    n = int(input('Выберите пункт меню (0 - стоп): '))
print('Благодарим Вас за использование нашего продукта=)')