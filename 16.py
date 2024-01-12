#!/usr/bin/env python3
#Опишите класс Calculator, который будет реализовывать следующие методы и поля:
#sum(self, a, b) - сложение чисел a и b
#sub(self, a, b) - вычитание
#mul(self, a, b) - умножение
#div(self, a, b, mod=False) - деление. Если параметр mod == True, то метод должен возвращать остаток от деления вместо деления. По умолчанию mod=False.
#history(self, n) - этот метод должен возвращать строку с операцией по ее номеру относительно текущего момента (1 - последняя, 2 - предпоследняя). Формат вывода: sum(5, 15) == 20
#last - строка того же формата, что в предыдущем пункте, в которой содержится информация о последней операции по всем созданным объектам калькулятора. Т.е. это последняя операция последнего использованного объекта калькулятор. Если операций пока не было, то None.
#clear(cls) - метод, который очищает last, т.е. присваивает ему значение None.
#Формат вывода
#
#При сохранении строк в history и last нужно выводить только один знак после запятой дробного числа. При выполнении деления с mod сам параметр mod не нужно записывать в лог.
class Calculator:
	last = None
	
	def __init__(self):
		self.list = []
		
	def sum(self, a, b):
		self.list.append(f"sum({a}, {b}) == {a+b}")
		Calculator.last = (f"sum({a}, {b}) == {a+b}")
		return a + b
	
	def sub(self, a, b):
		self.list.append(f"sub({a}, {b}) == {a-b}")
		Calculator.last = (f"sub({a}, {b}) == {a-b}")
		return a - b
	
	def mul(self, a, b):
		self.list.append(f"mul({a}, {b}) == {a*b}")
		Calculator.last = (f"mul({a}, {b}) == {a*b}")
		return a * b
	
	def div(self, a, b, mod=False):
		if mod:
			f = a%b
			self.list.append(f"mod({a}, {b}) == {f:.1f}")
			Calculator.last = (f"mod({a}, {b}) == {f:.1f}")
			return a % b
		f = a/b
		self.list.append(f"mod({a}, {b}) == {f:.1f}")
		Calculator.last = (f"mod({a}, {b}) == {f:.1f}")
		return a / b
	
	def history(self, n):
		if n <= len(self.list):
			return self.list[-n]
		else:
			return None
		
	def clear(cls):
		cls.last = None
		
mua = Calculator()
print(mua.div(10, 12,mod=True))
print(mua.last)