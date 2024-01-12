#!/usr/bin/env python3
transactions = [
	{"name": "Василий", "amount": 500},
	{"name": "Петя", "amount": 100},
	{"name": "Василий", "amount": -800},
	{"name": "Василий", "amount": -800},
	{"name": "Василий", "amount": -800},
	{"name": "Василий", "amount": -800},
	{"name": "Василий", "amount": -800}
]
def get_balance(name, transactions):
	balance = 0
	for i in transactions:
		if i["name"] == name: 
			balance += i["amount"]
#	print(balance)
	return(balance)

def count_debts(names, amount, transactions):
	a = dict()
	for microchel in names:
		balance = get_balance(microchel, transactions);
		if(amount <= balance):
			a[microchel] = 0
		else:
			a[microchel] = amount - balance
	print(a)
	
print(get_balance("Василий", transactions))
count_debts(["Василий", "Петя", "Вова"], 150, transactions)