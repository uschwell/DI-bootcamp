########EX1

##Note: the extra spaces were added deliberatly- for aesthetics
str1='Hello world '
str2= 'I love python '
str1=str1*4;
str2=str2*4;
print(str1+str2);



########Ex2
month=input('Please enter a month (1 to 12) ');
month=int(month);
if(month<=0)or(12<month):
    print("Error!");
elif(month>=3)and(month<=5):
    print("Spring!");
elif(month>=6)and(month<=8):
    print("Summer!");
elif(month>=9)and(month<=11):
    print("Autmn!");
elif(month>=12)or(month<=2):
    print("Winter!");