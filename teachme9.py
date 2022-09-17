# 1
for i in range(0, 11):
    print(i)

print('****************')

# 3
for i in range(0, 11):
    i = i ** 2
    print(i)

print('****************')

# 5
for i in range(0, 7):
    if i == 3:
        continue
    elif i == 6:
        continue
    print(i)

print('****************')

even = 0
odd = 0

# 4
for i in range(10, 35):
    if i % 2 ==0:
        even = even + 1
    else:
        odd = odd + 1 

print(f'There are  {even} even numbers and  {odd} odd numbers')

print('****************')

# to do: write the same numbers in two ranges using nested loops

# while loop 1
for i in range(11):
    print(i,' I love Python')

print('****************')

# 3
i = 0

while i < 10:
    i += 1
    if i == 6:
        continue
    print(i)

print('****************')

# 4
i = 0
while i < 50:
    i += 1
    if i % 5 == 0:
        print(i)
    else:
        continue

print('****************')