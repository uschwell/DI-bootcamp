def __abs__(self):
    "Receives a number and returns the absolute of said number"
    print(str(abs(self)))
    # return self.model.capitalize()


def abs(self):
    "More like the original abs(), takes a number and returns the absolute value (the no-recursion method)"
    if(self<0):
        print(str((-1)*(self)))
    else:
        print(str(self))
    return

#created two separate ways to invoke "abs()"- not sure which one you guys wanted

# abs(-5)
# __abs(-10)__


# def int(self):
#     "Receives an input (of some integer) and immedietly prints it to the terminal (Input will always be received as a string)"
#     "Note: wasn't sure if I should include a checker- I assume legal/correct input- this WILL print string as 'ok' integers"
#     print(self)       


# int(10)

def __input__():
    "When this function is invoked- request for an input. then immedietly print that input to the terminal"
    temp=input("Please enter a number")
    print(str(temp))

# __input__()


# print(__abs__.__doc__)



###########################EX2

class Currency:

    def __init__(self, name, amount):
        self.name=name
        self.amount=int(amount)


    # def string(self):
    #     return self.name

    def __add__(self, other):
        #if 'other' is an integer we add it to the value. Otherwise we check and add the two vlaues (if compatible)
        if(type(other)==type(self)):
            if(str(self.name)!=str(other.name)):
                print("TypeError: Cannot add between Currency type "+self.name+" and "+other.name)
            else:
                self.amount+=other.amount
                return (self.amount)
        if(type(other)==type(5)):
            self.amount=(self.amount+ other)
            return (self.amount)

    def __iadd__(self, other):
        return (self+other)

    def __pos__(self, other):
        return (self+other)



    def __str__(self):
        "Wasn't sure if you wanted me to Print this locally or not"
        #print (f'{self.amount} {self.name}s')
        return f'{self.amount} {self.name}s'

    def __repr__(self):
        return (f'{self.amount} {self.name}s')


    def __int__(self):
        print("aa")
        return self.amount



c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
c5=Currency('tester',500)
str(c1)
# print(str(c1))
c1+=12
# print(str(c1))
# c1+=5
# print(str(c1))
# print(str(c1))
str(c2)
str(c3)
#c1+c3
x=int(c5)
print(x)