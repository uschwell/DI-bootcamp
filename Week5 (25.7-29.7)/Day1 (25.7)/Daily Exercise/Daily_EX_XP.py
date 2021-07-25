#######EX1

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#we create 3 cats
cat1= Cat('Aaa', 15)
cat2= Cat('Bbb', 20)
cat3= Cat('Ccc', 25)

# print(cat1.age)
# print(cat2.age)
# print(cat3.age)
catList=[cat1, cat2, cat3]
# print(catList)

#function receives a list of "Cat" objects and  returns the object with the oldest cat
def oldest_cat(tempCatList):
    oldestAge=-99
    oldestCatObject=[]
    for c in tempCatList:
        if(int(c.age)>oldestAge):
            oldestAge=c.age
            oldestCatObject=c
    return oldestCatObject

toPrint=oldest_cat(catList)
print("The oldest cat is "+str(toPrint.name)+ " who is "+str(toPrint.age)+" years old")




#############EX2

class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(self.name+" goes woof!")
    def jump(self):
        print(self.name+" jumps "+str(self.height*2)+" centimeters in the air! (That's twice his own height, WOW!)")

#steps 1-4
goodBoy=Dog('spot', 100)
goodBoy.bark()
goodBoy.jump()


#steps 5-6
davids_dog=Dog('Rex',50)
print("Davids dog is named "+str(davids_dog.name)+" and he is "+str(davids_dog.height)+" centimeters tall")
davids_dog.bark()
davids_dog.jump()

#steps 7-8
sarahs_dog=Dog('Teacup',20)
print("Sarah's dog is named "+str(sarahs_dog.name)+" and he is "+str(sarahs_dog.height)+" centimeters tall")
sarahs_dog.bark()
sarahs_dog.jump()

#step 9
#function receives two 'Dog' objects and returns the object with the larger dog
def bigger_Dog(dog1, dog2):
    if(dog1.height>dog2.height):
        return dog1
    else:
        return dog2

larger=bigger_Dog(davids_dog, sarahs_dog)
print(larger.name+ " is the The bigger dog")



#############EX3
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()




#######################EX4
class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals=[]
    def add_animal(self, new_animal):
        self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()

myZoo=Zoo('NationalZoo')
myZoo.add_animal('lion')
myZoo.add_animal('tiger')
myZoo.add_animal('bear')

#print all the animals we placed in the zoo
myZoo.get_animals()


#sell the lion
myZoo.sell_animal('lion')
#print the zoo without the lion
myZoo.get_animals()

#sort the list alphabetically
myZoo.sort_animals()
#print the alphebatized zoo list
myZoo.get_animals()