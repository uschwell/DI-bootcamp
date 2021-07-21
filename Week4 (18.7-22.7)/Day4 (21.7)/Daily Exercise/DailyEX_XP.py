import random;



##############EX1
def display_message():
    print("In this course I am learning to code in Python");




display_message();



###########EX2

def favorite_book(book_title):
    print("One of my favorite books is "+book_title);

favorite_book('Way of Kings')




################Ex3

def describe_city(city_name='Reykjavik ', country='Iceland'):
    print(city_name+" is in "+country);


describe_city('Tel-Aviv','Israel');
#describe_city();


#####################Ex4
def random_num_compare(input):
    if(int(input)<=100)and(int(input)>0):
        rand=random.randint(1, 100);
        #print("generated random number: "+str(rand))

        if(rand==int(input)):
            print("Sucess the numbers match!");
        else:
            print("Im sorry, those numbers dont match");


random_num_compare(5);





#######################Ex5
def make_shirt(size="Large", shirt_text="I love Python"):
    print("The shirt should be size "+str(size));
    print("and should have the text \"" +shirt_text+" \" printed on it");


#make_shirt('Large',"Hello World")
make_shirt()
make_shirt("Medium")
make_shirt("Small", "Hello World")



#################Ex6

magicians_names=["Sam","Bob","Billy","Riki","Jenny"]

def make_great(magicians_names):
    for i in range(len(magicians_names)):
        alteration=" the Great "
        magicians_names[i]=(magicians_names[i]+alteration)

def show_magicians(list_names):
    for names in list_names:
        print(names);


make_great(magicians_names)
show_magicians(magicians_names)