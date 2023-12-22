# -*- coding: utf-8 -*-
"""
Завдання 19.3

Створити функцію send_command_to_devices, яка надсилає різні команди show на
різні пристрої у паралельних потоках, а потім записує вивід команд у файл. Вивід
із пристроїв у файлі може бути у будь-якому порядку.

Параметри функції:
* devices - список словників з параметрами підключення до пристроїв
* commands_dict - словник у якому зазначено який пристрій відправляти яку
  команду. Приклад словника - commands
* filename - ім'я файлу, до якого будуть записані висновки всіх команд
* limit – максимальна кількість паралельних потоків (за замовчуванням 3)

Функція нічого не повертає.

Вивід команд має бути записане у файл у такому форматі (перед виводом команди
треба написати ім'я хоста і саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh int desc
Interface                      Status         Protocol Description
Et0/0                          up             up
Et0/1                          up             up
Et0/2                          admin down     down
Et0/3                          admin down     down
Lo9                            up             up
Lo19                           up             up
R3#sh run | s ^router ospf
router ospf 1
 network 0.0.0.0 255.255.255.255 area 0


Для виконання завдання можна створювати додаткові функції.

Перевірити роботу функції на пристроях із файлу devices.yaml.

У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до ваших пристроїв відрізняються,
потрібно змінити параметри у файлі devices.yaml.
"""

commands = {
    "192.168.100.3": "sh run | s ^router ospf",
    "192.168.100.1": "sh ip int br",
    "192.168.100.2": "sh int desc",
}
