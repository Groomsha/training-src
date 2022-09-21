def concentration(V, sugar):
    percent = sugar / V * 100
    print('На', V, 'мл воды', sugar, 'ч.л. сахара.')
    if 0 <= percent <= 15:
        print('Низкое содержание сахара в растворе.')
    elif 16 <= percent <= 50:
        print('Среднее содержание сахара в растворе.')
    elif 51 <= percent <= 100:
        print('Сироп=).')


n_V = int(input('Введите V воды, мл: '))
n_sugar = int(input('Введите количество сахара, ч.л.: '))
concentration(n_V, n_sugar)
