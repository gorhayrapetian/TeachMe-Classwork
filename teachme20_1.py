my_dict = {x: x ** 2 for x in [1, 2, 3, 4, 5]}

print(my_dict)

myDict1 = {'milk': 1.02, 'bread': 4.75}

dollar_to_pound = 0.76

new_price = {item: value * dollar_to_pound for (item, value) in myDict1.items()}

print(new_price)

myDict2 = {'Gor': 17, 'Vardan': 22}

even_dict = {k: v for (k, v) in myDict2.items() if v % 2 == 0}

print(even_dict)

original_dict = {'Jack': 38, 'Michael': 48, 'Gvidon': 25}

new_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0 if v > 30}

print(new_dict)

other_dict = {k: 'old' if v > 40 else 'young' for (k, v) in original_dict.items()}

print(other_dict)