import requests
import random
import string
import re
# our_url = "http://norvig.com/ngrams/sowpods.txt"
  
# # URL of the image to be downloaded is defined as image_url
# r = requests.get(our_url) # create HTTP response object
  
# # send a HTTP request to the server and save the HTTP response in response object-> r
# with open("anagram.txt",'wb') as f:
#     # write the contents of the response (r.content) to a new file in binary mode.
#     f.write(r.content)





# #The above code lines(1-13) will access the website and download the desired (text) file
# #we now write (completely independent) code that will re-open the saved file and make use of it.
# #Note: this separation was both for writing 'good' code. AND to avoid downloading again for each new test
# #Note II!!!!: If you comment out the above code (lines 5-13) the code runs MUCH faster since you remove the HTTP request (as you can see I did)



    #I use the below code to access my locally saved text file (MUCH faster than an HTTP request each time- you can edit this out and use the 'download' code above if you want)
def get_words_from_file():
    word_list=[]
    #we will add every line in the text document to an Array (a list). This will give us the easiest access to the contents as needed
    for line in open('anagram.txt'):
        #since we are saving the words in a list, we can remove the (now unneeded) \n from the end of each word
        temp=line.rstrip('\n')
        word_list.append(temp)
    return(word_list)


def check_punctuation(word):
    "This function will check if our word contains any 'special' characters"
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  
    if(regex.search(word) == None):
        return True
        
    else:
        return False


def is_anagram(word1, word2):
    tempWord1=string_to_list(word1)
    tempWord2=string_to_list(word2)
    #check length, if yes, sort them, if they match->Anagram!
    if(len(tempWord1)==len(tempWord2)):
        tempWord1.sort()
        tempWord2.sort()
        if(tempWord1==tempWord2):
            return True
        else:
            return False
    else:
        return False

def string_to_list(string):
    list=[]
    list[:0]=string
    return list




class AnagramChecker:

    def __init__(self):
        #our constructor takes the entire text file, and saves it as an ARRAY (list) of individual words
        #(that have all had their trailing \n removed)
        self.textFile=get_words_from_file()



    def is_valid_word(self,word):
        #first, we confirm no 'special characters are in the received word
        if(check_punctuation(word)):
            return True
        else:
            return False

    def get_anagrams(self,word):
        all_Anagrams=[]
        for allWords in self.textFile:
            if(is_anagram(word,allWords)):
                check=True
                #we make sure we haven't already added this word-if not, we add it
                for i in all_Anagrams:
                    if(i==allWords):
                        check=False

                if(check):
                    all_Anagrams.append(allWords)
        return all_Anagrams





# myTest=AnagramChecker()

# # print(myTest.is_valid_word())
# # is_anagram('olleh','hello')
# print(myTest.get_anagrams('MEAT'))