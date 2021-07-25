class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self):
        print("Hello my name is " + self.name)
# add a method of check_over_18 that will return True or False 
# based on the persons age
# create two differently aged person objects and test your code!!!

personA=Person('Aaa',25)
personB=Person('Bbb',30)
personA.show_details()
personB.show_details()

#checkA
if(personA.age<28):
    print(personA.name +' is too young')
else:
    print(personA.name +' is too old')