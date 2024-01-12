#!/usr/bin/env python3
#
#Напишите функцию get_popular_name_from_file(filename), которая считывает файл, в котором в каждой строке записаны имя и фамилия через пробел. filename - это имя файла, в котором записаны эти имена. Вам нужно вернуть строку - самое популярное имя в файле. Если таких имен несколько, они должны быть перечислены через запятую внутри строки в алфавитном порядке.
#Формат ввода
#
#Джо Байден
#Владимир Добрый
#Владимир Злой
#Джо Буш
#Илон Маск
#Формат вывода
#
#Владимир, Джо

def get_popular_name_from_file(filename):
	f = open(filename, 'r')
	dictionary = dict()
	stroka = ''
	for line in f:
		name = line.split(" ")[0]
		if(name in dictionary):
			dictionary[name] += 1
		else:
			dictionary[name] = 1
	max_value = 0
	for i in dictionary.values():
		if max_value < i:
			max_value = i
	for i, j in dictionary.items():
		if int(j) == max_value:
			stroka += str(i)+", "
	f.close()
	return stroka[:-2]
	
print(get_popular_name_from_file("14.txt"))