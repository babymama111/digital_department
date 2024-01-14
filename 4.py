input_string = input()
substring = input()

words = input_string.split()

matching_words = [word for word in words if substring.lower() in word.lower()]
for word in matching_words:
    print(word)
