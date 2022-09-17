class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        print(self.fname, self.lname)

class President(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

p = President('Joe', 'Biden', 2023)

print(p.year)