#################part 1



# a template for creating objects


# a new 'creation' (every time we create a new 'class', or a new 'thing' [almost always an 'object'] we can refer to it as an 'instance')


# combining the methods relevant to a class within that same class. Also helps us restrict access to any data to whatever specific methods (functions) we want
# (i.e- I can only make changes to "self.value" with the use of "def value_changer"- [getters/setters]. this helps us limit our classes to behaving in specific ways


# making our functions as "non-specific" as possible. and only making them "final" at the last moment. This is a major
# factor for SOLID porgramming methods- because it helps leave our classes open for 'extension'
# (i.e it lets us use the same functions for more and braoder things)


# attributes and methods that are received from a 'parent'. similar to abstraction. You can have a generic "car", and 
# then a bunch of more specific details in 'children' classes. any methods/functions in the parents will be inherited (useable)
# in the children. i.e all vehicles have a "liscence plate" attribute (along with methods for getting/manipulating it) but any
# specific attributes to a "vehicle" can be added by the children


# inheritance from more than one parent. with our previous example, maybe our class "motorcylce" could inherit attributes from
# two parents: "car" AND "bicycle" it will thus share traits from both of thesem, and can have specific methods/attributes of its O_WRONLY


# similar to "abstraction", polymorphism is about using/the ability to use an overarching interface (or even class) for many, many different types and classes
# to continue our example. maybe all cars could belong to a class/interface called "vehicle". All a vehicle would need is several VERY basic attributes.
# We could then apply vehicle to give an overall structure to ANY type of vehicle that we would want. (I.e, cars, bikes, trucks, planes, boats, etc)


# the order in which our compiler looks for methods/functions via inheritance. I.e our "motorcycle" might look to "car" OR to "bicycle"
# or eventually even "vehicle" in order to find a method or attribute called "movement". MRO is the order in which our compiler does this search.



############################PART 2

class Card:
    def __init__(self,suit, value):
        self.suit=suit
        self.value=value
        print("made card")


def is_Same(card1,card2):
    if((card1.value==card2.value)and(card1.suit==card2.suit)):
        return True
    else:
        return False


class Deck(Card):
    wholeDeck=[]
    def __init__(self, card):
        self.card=card
        print("huh")

        #make sure we don't already have the card in our deck- if not, add it to our deck
        flag=False
        for i in self.wholeDeck:
            if(is_Same(self.card,i)):
                print("same")
                flag=True
        if(not flag):
            self.wholeDeck.append(self.card)


    def shuffle(self):
        #first, we check that we have 52 cards
        if(len(self.wholeDeck)==52):
            pass
        else:
            print("some cards are missing!")


    def printMe(self):
        print("print-me")
        for i in self.wholeDeck:
            print(i)



print("hello")
card1=Card('Heart',10)
card2=Card('Heart',9)
card3=Card('Heart',8)
card4=Card('Heart',7)
deck=Deck(card1)
deck=Deck(card2)
deck=Deck(card3)
deck.printMe()

# print(is_Same(card1,card1))