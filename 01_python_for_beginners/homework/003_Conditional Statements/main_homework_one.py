# Напишите программу, которая спрашивает у пользователя его имя,
# и если оно совпадает с вашим, выдаёт определённое сообщение.

your_name = input("What is your name? ")
my_name = 'Ihor'

if your_name.upper() == my_name.upper():
    print(f"We're the same blood - {your_name.title()}")
else:
    print(f"I do not know you - {your_name.title()}")
