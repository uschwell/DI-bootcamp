##################Ex2
class Dog():
    is_lazy = True

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight=weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return ((self.weight/self.age)*10)

    def fight (self, other_dog):
        myDog=self.run_speed()*self.weight
        otherDog=other_dog.run_speed()*other_dog.weight
        if(myDog>otherDog):
            return f'{self.name} has won the fight'
        else:
            return f'{other_dog.name} has won the fight'





# dog1=Dog('spot',10, 10)
# dog2=Dog('sam', 10, 15)
# dog3=Dog('sally',20, 50)
# print(dog1.fight(dog2))
# print(dog3.fight(dog2))
# print(dog1.bark())
# print(dog2.bark())
# print(dog3.bark())