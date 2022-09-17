# words = ('Gor', 'iPhone', 'laptop', 'Robot')

# result = filter(lambda x: x[0].isupper(), words)

# print(list(result))

num = (214, 243, 65, 875, 88, 34)

even = lambda x: x % 2 == 0

even_count = 0
odd_count = 0

for i in num:
    if even(i):
        even_count += 1
    else:
        odd_count += 1

print("there are", even_count, "even numbers")
print("there are", odd_count, "odd numbers")