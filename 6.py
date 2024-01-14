res =  []

for i in range(5):
    input_string = int(input(""))
    res.append(input_string)
res.sort(reverse = True)
for j in res:
    print(j)