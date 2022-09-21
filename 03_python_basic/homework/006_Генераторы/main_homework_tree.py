# Напишите функцию-генератор для получения n первых простых чисел.

if __name__ == '__main__':
	def isprime(n):
		if n == 2:
			return False
		for x in range(2, n):
			if n%x == 0:
				return False
			else:
				return True

	def primes(n=1):
		while (True):
			if isprime(n):
				yield n
			n += 1


	for n in primes():
		if n > 100:
			break
		print(n)
