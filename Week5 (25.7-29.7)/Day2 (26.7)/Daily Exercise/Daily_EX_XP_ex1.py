##################EX1


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


#My own 'Breed'
class Tabby(Cat):
    def sing(self, sounds):
        return f'{sounds}'


cat1=Tabby('thing1', 10)
cat2=Bengal('thing2',5)
cat3=Chartreux('kitty',2)
myCats=[cat1,cat2,cat3]
# print(myCats)

myPets=Pets(myCats)
myPets.walk()