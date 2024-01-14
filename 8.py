a = input()
a = a.lower()
b = a.replace(' ', '')
c = b.split(",")
dictionary = dict()
for i in c:
    if(i in dictionary):
        dictionary[i] +=1
    else:
	    dictionary[i] = 1

sorted_dictionary = sorted(dictionary.items(), key=lambda item: item[1], reverse = True)
for i in sorted_dictionary[:3]:
    print(i[0]+ ": " + str(i[1]))