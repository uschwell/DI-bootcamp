############Ex1
my_fav_numbers={1,2,3,4};
my_fav_numbers.add(5);
my_fav_numbers.add(6);
print(my_fav_numbers);
my_fav_numbers.remove(6);
#print(my_fav_numbers);

friend_fav_numbers={22,23,24};

our_fav_numbers=my_fav_numbers.union(friend_fav_numbers);
print(our_fav_numbers);

############Ex2
#Answer: sort of. Once you have created a tuple, you cannot change it.
#However:If you use (for example:) the "+" function between two TUPLES python will automatically create a NEW tuple that contains
#all of the relevant data from both the original tuples


############Ex3
for i in range(20):
    print(i+1, end=" ");
print("\n");



############Ex4
tempFloat=1.5;
x=range(1,5)
for x in range(1,5):
    print(x, end=".");
    print(5, end=", ");
    print(x+1, end=", ");
print("\n");


#############Ex5
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.remove("Banana");
basket.remove("Blueberries");
# print(basket);

basket.insert(len(basket),'Kiwi');
basket.insert(0,'Apples');
# print(basket);
temp= basket.count('Apples');
print("there are "+str(temp)+" Apples in the basket");

#empty the basket
while(len(basket)>0):
    basket.remove(basket[0]);
#print the (now empty) basket
print(basket);


#################Ex6
my_name='Uriel'
flag=True;
while(flag):
    input_Name=input("what is your name? ");
    if(input_Name==my_name):
        flag=False;


#################Ex7
check_List=['a','b','c','d','e','f','g','h','i','j'];
for num, content in enumerate(check_List):
    if(num%2)==0:
        print(content, end=" ");
print("\n");



#################Ex8
x=range(1500,2500);
divides_seven=[];
divides_five=[];
for i in x:
    if(i%5)==0:
        divides_five.append(i);
    if(i%7)==0:
        divides_seven.append(i);
print("The following Numbers divide by 5: "+str(divides_five));
print("The following Numbers divide by 7: "+str(divides_seven));

#note: It is pretty simple to just PRINT the numbers as they divide by either 5 or 7. But this method leads to a more readable output, it is simple to change if you wanted the output printed differently



#################Ex9
fruit_input=input("Please input your favorite fruit/s (separate all fruits with a space please")
#this will separate the input by the default (whitespaces)
fruit_list=fruit_input.split();
print(fruit_list);
user_input=input("Please enter a fruit ");
if(fruit_list.count(user_input)):
    print("You chose one of your favorite fruits! Enjoy!");
else:
    print("You chose a new fruit. I hope you enjoy");


#################Ex10
flag2=True;
toppings=[];
while(flag2):
    top_add=input("What toppings would you like on your pizza? ");
    if(top_add=='quit'):
        flag2=False;
    else:
        print("adding "+top_add+ " to your pizza");
        toppings.append(top_add);
print("I have added the following toppings to your pizza ");
print(toppings);
print("Your pizza will cost you "+str(10+2.5*len(toppings))+" shekels in total");


#################Ex11
flagFamily=True
baby=0;
child=0;
adult=0;
while(flagFamily):
    familyMember=input("Please enter the age of the person who the ticket is for (enter 'done' if no more tickets)");
    #note: I am assuming correct input- if the family wants to enter a (-2) year old- the ticket is still free
    #(whether or not I should alert the media to this medical miracle is beyond the scope of this program :D !!)
    if familyMember=='done':
        flagFamily=False;
        break;
    elif(int(familyMember)<3):
        baby+=1;
    elif(3<=int(familyMember))and (int(familyMember)<=12):
        child+=1;
    elif(12<int(familyMember)):
        adult+=1;

total=(child*10)+(adult*15);
print("Your total cost is: $"+str(total));

#alternate method: first ask the family how many ticket they want, then have the while loop iterate that many times (counter--).
#I did not use this method- I DID use it for the part two.....

old_group=[];
group=input("Good Afternoon, how many people are you? ");
group=int(group);
while(group):
    name=input("What is your name? ");
    age=input("Hello, "+name+" how old are you? ");
    if(int(age)<=21)and(16<=int(age)):
        old_group.append(name);
    group-=1;
if(len(old_group)>0):
    print("The following people are allowed to see the movie");
    print(old_group);
    #I added just because
    print("The total price will be: $"+str(len(old_group)*15));
else:
    print("I'm sorry, none of you are allowed to see this movie");




#################Ex12

nameList=['aa','bb','cc','dd','ee','ff','gg'];
i=0;
while (i<len(nameList)):
    tempAge=input("Hello, "+nameList[i]+" how old are you? ");
    if(int(tempAge)<16):
        nameList.remove(nameList[i]);
    else:
        i+=1;

print(nameList);





#################Ex13
###############  AND Ex14
sandwich_orders=['tuna', 'egg salad','deli','pastrami','chicken','pastrami','pastrami','ham'];
finished_sandwiches=[];

#if I understood correctly, this code only needs to run IF there are 3 or more pastrami sandwiches-otherwise there is enough pastrami to serve everyone who wants
#note: IF there are very few pastrami sandwiches (i.e-2 or less) then they will be made (and printed/added to finished_sandwiches as normal)
if(sandwich_orders.count('pastrami')>=3):
    print("hello!)");
    print("I'm sorry, the deli has run out of pastrami, please order something else");
    while(sandwich_orders.count('pastrami')>0):
        sandwich_orders.remove('pastrami');


while(len(sandwich_orders)):
    finished=input("Cooks: press Enter every time you complete a sandwhich");
    finished_sandwiches.append(sandwich_orders.pop());
    print("ding! service up!");
#note I don't quite understand why you'd want me to only print the sandwhiches AFTER they are ALL done. Wouldn't it make more sense to announce each sandwich as it is ready?
#p.s- I did this, by adding a "ding! foods ready!" every time the cook finishes a sandwich
for i in finished_sandwiches:
    print("I made your "+i+ " sandwich");







