import re

input_string = input()


input_string = input_string.strip()


input_string = re.sub(r'\s+', '*', input_string)

print(input_string)
