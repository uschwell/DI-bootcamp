class Farm():
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals={}

    #function input is either: (self, new_animal, amount)
    #                       or: (self, new_animal)
    #So......Total           self=argv[0], name_animal=argv[1], amount=argv[2]
    def add_animal(*argv):
        # if we got only a name, we increase the animal amount by one
        if(len(argv)<=2):
            if(argv[1] in (argv[0].animals.keys())):
                argv[0].animals[argv[1]]+=1
            else:
                argv[0].animals[argv[1]]=1
    
    # otherwise, we add however many animals we received
        if(len(argv)>2):
            if(argv[1] in (argv[0].animals.keys())):
                argv[0].animals[argv[1]]+=int(argv[2])
            else:
                argv[0].animals[argv[1]]=int(argv[2])


    def get_info(self):
        for animal in self.animals:
            print(animal+" : "+str(self.animals[animal]))
        print("E-I-E-I-0!")

    def get_animal_types(self):
        temp=[]
        for names in self.animals.keys():
            temp.append(str(names))
        temp.sort()
        return temp

    def get_short_info(self):
        myShort=self.get_animal_types()
        myString="McDonald’s farm has"
        for animal in range(len(myShort)-1):
            myString+=(" "+str(myShort[animal])+",")
        myString+=(" "+myShort[len(myShort)-1]+".")
        return myString

myFarm=Farm('macdonalds')

myFarm.add_animal('sheep')
myFarm.add_animal('sheep')
myFarm.add_animal('cow',5)
myFarm.add_animal('goat',12)
myFarm.add_animal('Aardvark',15)

myFarm.get_info()
#get and print the sorted list
print(myFarm.get_animal_types())

#print the desired sentence
print(myFarm.get_short_info())