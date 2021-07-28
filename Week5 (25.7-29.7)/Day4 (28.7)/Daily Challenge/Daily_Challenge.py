import requests
import random
import string
# our_url = "https://raw.githubusercontent.com/devtlv/theStranger_text_W5D4PY/master/the_stranger.txt"
  
# # URL of the image to be downloaded is defined as image_url
# r = requests.get(our_url) # create HTTP response object
  
# # send a HTTP request to the server and save the HTTP response in response object-> r
# with open("the_stranger.txt",'wb') as f:
#     # write the contents of the response (r.content) to a new file in binary mode.
#     f.write(r.content)





#The above code lines(1-12) will access the website and download the desired (text) file
#we now write (completely independent) code that will re-open the saved file and make use of it.
#Note: this separation was both for writing 'good' code. AND to avoid downloading again for each new test
#Note II!!!!: If you comment out the above code (lines 4-12) the code runs MUCH faster since you remove the HTTP request (as you can see I did)



    #I use the below code to access my locally saved text file (MUCH faster than an HTTP request each time- you can edit this out and use the 'download' code above if you want)
def get_file():
    with open("the_stranger.txt",'r') as f:
    # save the contents of the file locally
        text = f.read()
    return text



def remove_punctuation(wordList):
    "we receive a list of words and remove all punctuation from said words"
    temp=wordList
    temp = [''.join(c for c in s if c not in string.punctuation) for s in temp]
    return temp






class Test:

    def __init__(self, fileText):
        self.content=fileText




    def word_frequency(self, word):
        counter=0
            #we split the content into words (by whitespace)
        checker=self.content.split(' ')
            #now we remove all excess punctuation
        checker=remove_punctuation(checker)
        for words in checker:
            #we compare the words (case insensitive)
            if(words.lower()==word.lower()):
                counter+=1
            
        if(counter==0):
            print("None")
        else:
            print("The word " +word+" appears "+str(counter)+" times in the text")



fileText=get_file()
myTest=Test(fileText)
myTest.word_frequency('French')