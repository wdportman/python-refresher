def double_numbers(iterable):
    for i in iterable:
        yield i + i

for i in double_numbers(range(1, 900000000)):  # `range` is a generator.
    print(i)
    if i >= 30:
        break