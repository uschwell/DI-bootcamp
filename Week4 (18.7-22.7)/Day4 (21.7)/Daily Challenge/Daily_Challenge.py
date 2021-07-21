
from typing import final




# def decode_clean(to_clean):
#     to_clean.replace("  ", "")
#     return to_clean

def decode_matrix(encoded):
    rows=len(encoded)
    row_sentence=''
    final=''
    #iterate through 
    for cols in range(len(encoded[0])):
        for r in range(rows):
            if(str(encoded[r][cols]).isalpha()):
                row_sentence+=str(encoded[r][cols])
                #cool note: this elif was specially built- if the row_sentence is TOO short- it fails at step 1 and NEVER even gets to the 2nd condition (which fails if it is tried on a blank string)
            elif(len(row_sentence)>0)and(row_sentence[len(row_sentence)-1]!=' '):
                row_sentence+=' '
        final+=row_sentence
        #reset the coloumn-word
        row_sentence=''
        # below is use of a function that would clean up the extra spaces in my final decoded sentence-not yet working
    # final=decode_clean(final)
    return final



mat=[
    [7,'i',3],
    ['T','s','i'],
    ['h','%','x'],
    ['i',' ','#'],
    ['s','M',' '],
    ['$','a',' '],
    ['#','t','%'],
   ['^','r','!']
]
x=decode_matrix(mat)
print(x)