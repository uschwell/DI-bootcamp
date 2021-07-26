from Daily_EX_XP_ex2 import Dog
import random

class PetDog(Dog):

    def __init__(self, name, age, weight, trained=False):
        self.name=name
        self.age=age
        self.weight=weight
        self.trained=trained

    def train(self):
        print(self.bark())
        self.trained=True
    
    def play(self, *args):
        print(str(self.name)+", ",end="")
        for names in args:
            print(str(names)+", ",end="")
        print(" are all playing together")

    def do_a_trick(self):
        rand=random.randint(0, 3)
        if(rand==1):
            print(self.name+" does a barrel roll")
        elif (rand==2):
            print(self.name+" stands on his back legs")
        elif (rand==3):
            print(self.name+" shakes your hand")
        else:
            print(self.name+" plays dead")

        
myPet=PetDog("aa",10,15)
# print(myPet.name)
# print(myPet.bark())
# print(myPet.trained)

myPet.train()

petNames=['spot','Bbb','Ccc']
myPet.play(petNames)
myPet.do_a_trick()