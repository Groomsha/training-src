class Hero:   # конструктор класса
    def __init__(self, name, health, armor, power, weapon):
        # строка
        self.name = name
        # число
        self.health = health
        # строка
        self.armor = armor
        # число
        self.power = power
        # строка
        self.weapon = weapon

    # печать инфо о персонаже
    def print_info(self):
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon, '\n')

    # нанесение удара:
    def strike(self, enemy):
        print('-> УДАР! ' + self.name + ' атакует ' + enemy.name + ' с силой ' + str(self.power) +
              ', используя ' + self.weapon + '\n')
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(enemy.name + ' покачнулся(-ась).\nКласс брони упал до ' + str(enemy.armor) +
              ', а уровень здоровья до ' + str(enemy.health) + '\n')


knight = Hero('Ричард', 50, 25, 20, 'меч')
rascal = Hero('Хелен', 20, 5, 5, 'лук')
knight.print_info()
rascal.print_info()
knight.strike(rascal)
rascal.strike(knight)
