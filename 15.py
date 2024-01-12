#!/usr/bin/env python3

#Задачи, аналогичные этой, часто встречаются в реальной веб-разработке. Будем получать и отдавать JSONы. К вам поступают данные в виде json-строки, в которых содержится список людей. Для каждого человека описаны различные его параметры, но вам нужно посчитать просто средний возраст всех людей из списка. Напишите функцию mean_age(json_string), которая принимает json строку, считает средний возраст людей из входных данных и возвращает новую json-строку в том формате, который указан ниже.
#Формат ввода
#
a =''
#Формат вывода
#
#{"mean_age": 23.5}
import json

def mean_age(json_string):
	my_json = json.loads(json_string)
	count = 0
	average_age = 0
	for i in my_json:
		average_age += int(i["age"])
		count += 1
	result_str = json.dumps({"mean_age": average_age/count})
	return result_str
	
	
print(mean_age(a))