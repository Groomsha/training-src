# Создайте модуль для получения простых чисел. Импортируйте его из другого модуля. Импортируйте отдельные его имена.

from prime_numbers.getting_a_number import GettingANumber


if __name__ == '__main__':
    numbers = GettingANumber()

    for n in numbers.primes():
        if n > 100:
            break
        print(n)
