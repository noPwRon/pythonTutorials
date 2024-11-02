# A generic defininte for a class


# Defining the class

from services.data_service import DataService


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def intro(self):
        print(f"Hello, my name is {self.name} and I am a {self.species}")


# Creating a pet dog
dog = Pet(name="Cin", species="Dog")
dog.intro()
# renaming the dog
dog.name = "Max"
dog.intro()
# Adding a new attribute
dog.colour = "Brindle"

dog.colour

data = DataService
