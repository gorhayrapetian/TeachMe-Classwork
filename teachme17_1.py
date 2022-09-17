from abc import ABC

class Country(ABC):

    def action(self):
        pass

class USA(Country):

    def get_capital(self):
        return 'Washington D.C. is the capital of the USA'
         
    def get_population(self):
        return 'The USA has a population of 332 million'

    def get_language(self):
        return 'The USA has no official language'

class Armenia(Country):

    def get_capital(self):
        return 'Yerevan is the capial of Armenia'
         
    def get_population(self):
        return 'Armenia has a population of 3 million'

    def get_language(self):
        return 'The official language of Armenia is Armenian'


class Russia(Country):

    def get_capital(self):
        return 'Moscow is the capial of Russia'
         
    def get_population(self):
        return 'Russia has a population of 144 million'

    def get_language(self):
        return 'The official language of Russia is Russian'


object_usa = USA()

object_armenia = Armenia()

object_russia = Russia()

list_of_countries = [object_usa, object_armenia, object_russia,]

for country_object in list_of_countries:
    print(country_object.get_capital())
    print(country_object.get_population())
    print(country_object.get_language())