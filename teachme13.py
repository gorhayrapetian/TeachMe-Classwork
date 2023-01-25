import random
import math
import calendar

userAnswer = int(input("Enter a number: "))

# 1 done
def func(userResponse):
    g = random.randint(0, 10)
    if userResponse == g:
        return True
    else:
        return False


x = func(userAnswer)
print(x)


# 2 done
def big(userResponse):
    g = random.randint(10, 100)
    if userResponse >= g:
        return True
    elif userResponse <= g:
        return False


y = big(userAnswer)
print(y)

# 3 done


x = int(input('Enter a year: '))
y = int(input('Enter a month: '))
print(calendar.month(x, y))

# 4 done

r = int(input('Enter a radius: '))


def radius(r):
    area = math.pi * r ** 2
    return area


print(radius(r))
