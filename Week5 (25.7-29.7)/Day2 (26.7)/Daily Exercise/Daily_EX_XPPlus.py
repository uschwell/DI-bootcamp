#################EX1
class Family:
    myFamily=[]
    def __init__(self, members, last_name):
        self.myFamily.append(members)
        self.last_name=last_name

    def born(self, **kwargs):
        self.myFamily.append(kwargs)
        print("Congratualations!")

    def is_18(self,name):
        for person in self.members:
            if (name in person):
                tempAge=name.get('age')
                if tempAge>18:
                    return True
                else:
                    return False
    
    def print_All(self):
        for people in self.myFamily:
            print(people)


example1={'name':'Michael','age':35,'gender':'Male','is_child':False}
example2={'name':'Sarah','age':32,'gender':'Female','is_child':False}
myFamily=Family(example1,'Smith')
# print(myFamily.myFamily)
myFamily.born(**example2)
# print(myFamily.myFamily)

myFamily.print_All()



# class TheIncredibles(Family):
#     incredibleFamily=[]
#     def __init__(self, members, last_name, power, incredible_name):
#         members['power']=power
#         members['incredible_name']=incredible_name
#         self.last_name=last_name
#         self.incredibleFamily.append(members)

#     def use_power(self):
#         for heroes in self.incredibleFamily:
#             if(heroes.is_18(heroes.get[name])):
#                 print(heroes.get[name].[power])
