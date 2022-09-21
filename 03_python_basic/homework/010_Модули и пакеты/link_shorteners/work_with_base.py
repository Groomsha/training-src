import shelve


class WorkWithBase:
	@staticmethod
	def work_to_db(*args, work: bool = True) -> str:
		with shelve.open('temp_db') as db:
			if work:
				db[args[0]] = args[1]
			else:
				return db.get(args[0], "В базе нет такой ссылки!")
