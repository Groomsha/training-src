class GettingANumber:
	def __init__(self):
		pass

	@staticmethod
	def isprime(n):
		if n == 2:
			return False
		for x in range(2, n):
			if n % x == 0:
				return False
			else:
				return True

	def primes(self, n=1):
		while (True):
			if self.isprime(n):
				yield n
			n += 1
