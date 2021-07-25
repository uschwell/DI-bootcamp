import math


###########################EX1
# class Circle():
#     def __init__(self, radius=1):
#         self.radius = int(radius)
#     def perimeter (self,):
#         perim=2*(math.pi)*self.radius
#         print("The perimeter of the circle is "+str(perim))

#     def area(self):
#         area= (math.pi)*(self.radius)*(self.radius)
#         print("The area of the circle is "+str(area))

#     def definition_circle(self):
#         print("Definition of a Circle: the set of all points on a plane that are a fixed distance from a center.")


# myTest=Circle(5)
# myTest.perimeter()
# myTest.area()
# myTest.definition_circle()





###########################EX2
class MyList():
    def __init__(self, list):
        self.list= list

    def reverse_List(self):
        temp=[]
        for item in range(len(self.list)-1, -1, -1):
            temp.append(self.list[item])
        
        return(temp)

    def sorted_list(self):
        temp=self.list
        temp.sort()
        return temp


list=MyList(['a','b','c','x','m', 'l'])
print(list.reverse_List())
print(list.sorted_list())