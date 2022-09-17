lst1 = [x[0] for x in ['python', 'ruby', 'javascript']]

print(list)

lst2 = [x ** 2 for x in range(1, 11) if x % 2 == 1]

print(lst2)

lst3 = [x for x in ['python', 'javascript', 'ruby'] if 't' not in x]

print(lst3)

obj1 = [True if i % 2 == 0 else False for i in range(10)]

print(obj1)

obj2 = ['Yes' if i % 2 == 0 else 'No' for i in range(10)]

print(obj2)

obj3 = ['Yes' if x % 2 == 0 else 'No' for x in range(10) if x != 3]  # does not try the number 3

print(obj3)

obj4 = [f"{i} = Yes" if i % 2 == 0 else f"{i} = No" for i in range(10)]

print(obj4)