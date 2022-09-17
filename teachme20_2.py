# 1 done
lst1 = [x for x in range(1, 999)]
other_lst = [x ** 3 for x in lst1 if x % 2 != 0]

print(other_lst)

# 2 done
lst2 = ['*' * x for x in range(0, 6)]

print('\n'.join(lst2))

# 3 done
dict3 = {k: k / 100 for k in range(100, 160, 10)}

print(dict3)

# 4 done
dict4 = {'NFLX': 4950, 'TREX': 2400, 'FIZZ': 1800, 'XPO': 1700}

dict5 = {k: v for (k, v) in dict4.items() if v > 2000}

print(dict5)

# 5 extra exercise
dict6 = {k: v for (k, v) in dict4.items() if k == 'TREX'}

print(dict6)
