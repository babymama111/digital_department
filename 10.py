#!/usr/bin/env python3
import datetime
birthdays = {"Катя": datetime.date(1989, 1, 1), "Петров Петр Петрович": datetime.date(1998, 1, 6)}

def gift_count(budget, month, birthdays):
    s = "Именинники в месяце "+ str(month) +": "
    count = 0
    for name, date in birthdays.items():
        if date.month == month:
            count +=1
            s += name
            s+= " ("+ date.strftime("%d.%m.%Y") + "), "
    if count != 0:
        s = s[:-2]
        s += ". " + "При бюджете " + str(budget) + " они получат по " + str(int(budget / count)) + " рублей."
    else:
        s = "В этом месяце нет именинников."
    print(s)
	
gift_count(budget=20000, month=5, birthdays=birthdays)
result = gift_count(budget=20000, month=1, birthdays=birthdays)
print(result)