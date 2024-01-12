#!/usr/bin/env python3
import re

def check_string(string):
	pattern_num = re.compile(r'^[+]?[78]?[ ]?[-]?[ ]?[(]?[0-9]{3}[)]?[-]?[ ]?[0-9]{3}[-]?[0-9]{2}[-]?[0-9]{2}$')
	pattern_email = re.compile(r"^[a-zA-Z0-9_.+-]+@+[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]{2,})*(\.[a-zA-Z0-9-]{2,})*$")
	if(pattern_email.match(string) or pattern_num.match(string) ):
		return True
	return False

print(check_string("qwerty@qwe.qwe.qwe.qwe.qwe"))


