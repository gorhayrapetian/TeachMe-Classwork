class Table:
    legs = True

    def __init__(self, legs_height, legs_count):
        self.legs_height = legs_height
        self.legs_count = legs_count

    def put_my_notebook(self):
        return 'notebook is put'

new_table_1 = Table('1m', 4)
new_table_2 = Table('1.5m', 1)
print(new_table_1.legs_count)
print(new_table_2.legs)


class MyClass():
    def __init__(self, my_list):
        self.data = my_list
        
x = MyClass([1,2,3])
x.data.append(10)
print(x.data)

class Car():
    Engine = '4.4 litres'
    HorsePower = '625 hp'

my_obj = Car()
print(my_obj) 
