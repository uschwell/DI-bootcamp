###############Ex1
print('Ex1')
to_print='Hello World ';
to_print=(to_print*5);
print(to_print);


##############Ex2
print('\nEx2')
first=99;
first=(first**3);
print(first*8);


#############Ex3

#>>> 5 < 3
#False

# >>> 3 == 3
#True

# >>> 3 == "3"
#False

# >>> "3" > 3
#False

# >>> "Hello" == "hello"
#False




##########Ex4
print('\nEx4')
computer_brand ='lenovo';
#print(type(computer_brand))
print("I have a " +computer_brand +" computer")




################Ex5
print('\nEx5')
name= 'Uri Schwell'
age='28'
shoe_size= '43';
info= "Hi, my name is " +name+ " and I am "+age+" years old. I\'m not sure why you\'d care but my shoe size is "+shoe_size+".";

print(info);




######################Ex6
print('\nEx6')
a=50;
b=45;
if(a>b):
    print('Hello World');
else:
    print('sorry, b is larger');




#################Ex7
print('\nEx7')
checkNum=input('Please enter a number ');
if(checkNum.isnumeric()!=True):
    print('That\'s not a number!')
elif(int(checkNum)%2==0):
    print(checkNum+" Is an even number");
elif(int(checkNum)%2==1):
    print(checkNum+" Is an odd number");



################Ex8
print('\nEx8');
checkName=input('What\'s your name? ');
if(checkName==name):
    print("Wow! What a coincidence! That/'s my name too!");
else:
    print("What an .....interesting name you have");





################Ex9
print('\nEx9');
checkHeight=input('What\'s your height? (in inches) ');
height= int(checkHeight)*2.54;
if(height>=145):
    print("You are tall enough for this ride!");
else:
    print("You need to grow some more before you can go on this ride!");