a = input()
a = a.lower()
b = a.replace(' ', '')
c = b.split(",")
words = set(c)
word = list(words)
word.sort()
res = ''
for i in word:
    res+=i
    res+=", "
print(res[:-2])