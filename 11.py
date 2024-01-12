def lists_sum(*data, unique=False):
    if unique:
        all_numbers = set()
        for numbers in data:
            all_numbers.update(numbers)
        return sum(all_numbers)
    else:
        total_sum = 0
        for numbers in data:
            total_sum += sum(numbers)
        return total_sum

print(lists_sum([1, 1], [1], [1, 2, 3]))
print(lists_sum([1, 1, 1], [1, 1], unique=True))
print(lists_sum([1, 1, 1], unique=False))
