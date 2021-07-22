from typing import final


alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#function that builds an encryption dictionary
def build_dict(shift):
    shift=int(shift)
    dict={}
    for letter in range(len(alphabet)):
        if(letter+shift)<len(alphabet):
            dict[alphabet[letter]]=str(alphabet[letter+shift])
        else:
            dict[str(alphabet[letter])]=str(alphabet[(letter+shift)-26])
        
    return(dict)

#function that builds a decryption dictionary
def break_dict(shift):
    shift=int(shift)
    dict={}
    for letter in range(len(alphabet)):
        if(letter-shift)>=0:
            dict[alphabet[letter]]=str(alphabet[letter-shift])
        else:
            dict[str(alphabet[letter])]=str(alphabet[26-(letter+shift)])    
    return(dict)



#uses the encrypt dictionary to encrypt a message
def encrypt_message(dict):
    message=input("what is the message you would like me to decrypt?")
    final=''
    for letter in message:
        final+=dict[letter]
    return final

#uses the encrypt dictionary to decrypt a message
def decrypt_message(dict):
    message=input("what is the message you would like me to decrypt?")
    final=''
    for letter in message:
        final+=dict[letter]
    return final




process=input("Do you want to encrypt or decrypt your message?")
shift=input("What shift value should I be using?")
#we create the relevant dictionary
#send the relevant dictionary to the relevant encrypter/decrypter
if(process=='encrypt'):
    dict=build_dict(shift)
    code=encrypt_message(dict)
elif(process=='decrypt'):
    dict=break_dict(shift)
    code=decrypt_message(dict)

print("Your final message is: ")
print(code)