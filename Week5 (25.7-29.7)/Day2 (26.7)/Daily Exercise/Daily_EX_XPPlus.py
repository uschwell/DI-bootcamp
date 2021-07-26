#################EX1
class Family:
    def __init__(self, members, last_name):
        self.members=members
        self.last_name=last_name

    def born(self, **kwargs):
        print("Whatup")
        print(kwargs)
        self.members.append(kwargs)
        print("Congratulations!")

    def is_18(self,name):
        for person in self.members:
            if (name in person):
                tempAge=name.get('age')
                if tempAge>18:
                    return True
                else:
                    return False

        print("error, that person isnt part of THIS family")



######Note: there is some sort of error here that neither me nor the instructor could solve before our time was up-for some reason Family
#           Will not accept the given initating input


example1={'name':'Michael','age':35,'gender':'Male','is_child':False}
example2={'name':'Sarah','age':32,'gender':'Female','is_child':False}
myFamily=Family(example1,'Smith')
print(myFamily.members)
myFamily.born(**example2)
print(myFamily.members)