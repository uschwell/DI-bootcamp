import requests
import random
our_url = "http://norvig.com/ngrams/sowpods.txt"
  
# URL of the image to be downloaded is defined as image_url
r = requests.get(our_url) # create HTTP response object
  
# send a HTTP request to the server and save the HTTP response in response object-> r
with open("word_doc.txt",'wb') as f:
    # write the contents of the response (r.content) to a new file in binary mode.
    f.write(r.content)





#The above code lines(1-10) will access the website and download the desired (text) file
#we now write (completely independent) code that will re-open the saved file and make use of it.
#Note: this separation was both for writing 'good' code. AND to avoid downloading again for each new test
#Note II!!!!: If you comment out the above code (lines 3-12) the code runs MUCH faster since you remove the HTTP request


def get_words_from_file():
    word_list=[]
    #we will add every line in the text document to an Array (a list). This will give us the easiest access to the contents as needed
    for line in open('word_doc.txt'):
        word_list.append(line)

    return(word_list)



def get_random_sentence(length):
    full_list=get_words_from_file()
    sentence=""
    for i in range(length):
        rand=random.randint(0, len(full_list))
            #this step removes the unwanted \n attacged to each word (useful)
        temp= full_list[rand].rstrip("\n")
        sentence=f'{sentence} {temp}'
    #for our final step, we add our ONE desired \n to the end of our sentence
    return f'{sentence}\n'


def print_lowerCase_sentence(sentence):
     print (sentence.lower())




    #this will print the (raw) randomly generated sentence (still uppercase-removed the extra \n)
# print(get_random_sentence(5))

    #this will print the randomly generated sentence (in lowerCase)
# print_lowerCase_sentence(get_random_sentence(10))


def main():
    length=input("How long would you like the sentence to be? (between 2 and 20 words\n")
    #confirm that we received an integer as inout
    try:
        if(int(length)):
            if((int(length)>=2)and(int(length)<=20)):
                #we reach here ONLY if the input was valid
                print(length)
                print_lowerCase_sentence(get_random_sentence(int(length)))

            else:
                if((int(length)>20)):
                    size='large'
                elif(int(length)<2):
                    size='small'

                print(f'Im sorry, that number is too {size} for our program')

    #if they didn't enter an integer
    except:
        print("I'm sorry, you need to enter a NUMBER, please try again")







#we call our "main" to begin the program
main()