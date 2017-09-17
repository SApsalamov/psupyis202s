'''
formal - обычный аргумент
*arguments - позиционные аргументы, содержаться в кортеже
**keywords - формальный параметр, содержащий словарь значений именованных аргументов
Запись **name должна сле довать после записи *name
'''
def example(formal, *arguments, **keywords):
	print("Колличество пользователей: ", formal)
	print("-" * 40)
	for arg in arguments:
		print(arg)
		print("-" * 40)
		for kw in keywords.keys():
			print(kw, ":", keywords[kw])

example(100000, 'Это очень много', 'Это действительно очень много ...',
			language='Python', author='Guido van Rossum')
