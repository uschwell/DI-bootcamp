import math
import turtle

class Circle:
    def __init__(self, method, value):
        #if we build with radius
        if(method=='r'):
            self.radius=int(value)
            self.diameter=(int(value)*2)
        #if we build via diameter
        elif(method=='d'):
            self.radius=(int(value)/2)
            self.diameter=int(value)


    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return self.diameter

    def get_area(self):
        return ((self.radius)*(self.radius)*(math.pi))

    def add_circ(self, other):
        "We get two circles, and add the radius of the 'other' to itself"
        self.radius+=other.radius
        self.diameter+=other.diameter

    def circs_are_equal(self, other):
        if(self.radius==other.radius):
            return True
        else:
            return False

    def compare_circ(self, other):
        if(self.radius>other.radius):
            print("The current circle is bigger")
        elif(self.radius<other.radius):
            print("The second circle is bigger")
        elif (circs_are_equal(self, other)):
            print("The Circles are the same size!")
        else:
            print("something here seems wrong....")


    def print_circ(self):
        "I commented out my own attempts at circle drawing when I found a module that did the job for me-the below still works, just not as well as 'turtle' "

        # pow(2,2)
        # for col in range(1,self.radius+1,1):
        #     for row in range(1,self.radius+1,1):
        #         #reminder radius=squareRoot(a^2 + b^2)
        #         if(self.radius>(math.sqrt(pow(col+1,2)+pow(row+1,2)))):
        #             print("x",end="")
        #         else:
        #             print(" ",end="")
        #     print("")
        t = turtle.Turtle()
        t.circle(self.radius)

    
def circle_sort(self,**args):
    "Receives a list of circles. Sorts them by size"
    return args.sort()







value=input("Give a value (integer)")
print("Define A Circle. You may use 'Diameter' (d) or 'Radius' (r) ")
text=input("(d)/(r)")

myCircle=Circle(text,value)
print(myCircle.get_area())


myCircle.print_circ()
input("press Enter to continue")

circle2=Circle('r', 100)
circle3=Circle('r', 5)
circle4=Circle('r', 50)

# myList=[myCircle,circle2,circle3,circle4]
# print(circle_sort(myList))

