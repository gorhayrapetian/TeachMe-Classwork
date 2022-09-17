# 1 done
try:
    with open('ds.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('There is no such file')

# 2 done
try:
    num = 10
    result = num / 0
    print(result)
except ZeroDivisionError:
    print('You can\'t divide number by zero')

# 3
def func(name):
    if name[0].islower():
        raise FileNotFoundError('The name of the file must start with uppercase letter')
    else:
        with open(name, 'r') as file:
            print(file.read())


print(func('story.txt'))