# from typing import overload


# num1=5;
# num2=10
# num3=num1+num2;
# print(num1)
# print(num2)
# # print(num3)
# print('hello world')
# my_age=28;
# old_age=my_age+123879;
# print(old_age);

# first_name='Uri';
# last_name='Schwell'
# full_name=first_name+' '+last_name;
# print(full_name)




#For example,  
# my_name = "Frank"  this line creates a name variable type: string 
#print("My name is {}".format(my_name))

cars = 100;
space_in_a_car = 4.0
drivers = 30

passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


# print("There are {}".format(cars) ,"cars available.")
# print("There are only", drivers, "drivers available.")
# print("There will be", cars_not_driven, "empty cars today.")
# print("We can transport", carpool_capacity, "people today.")
# print("We have", passengers, "to carpool today.")
# print("We need to put about", average_passengers_per_car,"in each car.")

print('hello');
temp=input('please enter a number ')
temp=int(temp);
if((temp%3 == 0)and(temp%5 == 0)):
    print('FizzBuzz');
elif((temp%3) == 0):
    print('Fizz');
elif((temp%5) == 0):
    print("Buzz");

