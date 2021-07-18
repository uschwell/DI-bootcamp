import random


str=input('Please enter 10 characters for a string\n');
if(len(str)>10):
    print("that string is too long!");
elif(len(str)<10):
    print("that string is too short");
elif(len(str)==10):
    strList=list(str);
    print("The first letter: "+strList[0]);
    print("The last lette: "+strList[len(str)-1]);
    #part 3- we print the string in steps
    x=0;
    y=0;
    while(x<len(strList)):
        while(y<=x):
            print(strList[y], end ="");
            y+=1;
        y=0;
        x+=1;
        print('\n');


random.shuffle(strList);
print(strList);
#or if you wanted a little more effort than just printing the list
x=0;
while(x<len(strList)):
    print(strList[x], end ="");
    x+=1;