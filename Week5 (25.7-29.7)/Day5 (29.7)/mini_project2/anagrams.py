from anagram_checker import AnagramChecker
from anagram_checker import check_punctuation

import re



def menu():
    flag=True
    while(True):
        print("-----Main Menu-----")
        user_input=input("Please enter a word (Or 'quit' if you wish to quit)\n")
        if(user_input=='quit'):
            break
        else:
            #our text list is in all upperCase-we make sure to accomodate this
            clean_Input=validate_input(user_input.upper())
            flag=clean_Input
        #once we have cleaned and validated the input we can continue
        if(flag):
            myAnagram=AnagramChecker()
            anagramList=myAnagram.get_anagrams(clean_Input)
            #if the anagramList is not empty we print it 'nicely'
            if(anagramList):
                print('YOUR WORD: "'+clean_Input+'"')
                print('Anagrams for your word: ',end="")
                for i in anagramList:
                    print(i.lower(),end="")
                    print(', ',end="")
                print(".")

            else:
                print("I'm sorry, I can't find any anagrams for that word")
        else:
            print("I'm sorry, that is not a useable word. Please try again")


def validate_input(word):
    #first, we will remove excess whitespace
    tempWord=word.strip()

    #check only one word (i.e no spaces)
    if(re.search(" ", tempWord)):
        return False
        #we reuse our function to confirm no special characters (from anagram_checker)
    if(not check_punctuation(tempWord)):
        return False
    
        #if we reach this point-then the input has been validated- we can send it back
    return tempWord




# myTry=AnagramChecker()
# print(myTry.get_anagrams("ABA"))




menu()