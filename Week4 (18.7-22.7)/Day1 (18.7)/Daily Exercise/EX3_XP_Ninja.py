######EX3

    # >>> 3 <= 3 < 9
    #True

    # >>> 3 == 3 == 3
    #True

    # >>> bool(0)
    #False

    # >>> bool(5 == "5")
    #False

    # >>> bool(4 == 4) == bool("4" == "4")
    #True

    # >>> bool(bool(None))
    #False

    # x = (1 == True)
    #This makes "x=True"-- no actual output

    # y = (1 == False)
    #This makes "y=False"-- no actual output

    # a = True + 4
    #This makes "a=5"-- no actual output

    # b = False + 10
    #This makes "b=10"-- no actual output

    # print("x is", x)
    #"x is true"

    # print("y is", y)
    #"y is false"

    # print("a:", a)
    #a: 5

    # print("b:", b)
    #b: 10




    #################Ex4
longest=(-9999);
longestWord='';
checker=1;
while(checker):
    newIn=input("input the longest sentence you can without the character A (letter ""A"" will quit the program)\n");
    #first, we confirm the input is in fact longer tham anything previously entered
    #we confirm there is no "A"
    strList=list(newIn);
    length=len(strList);
    x=0;
    while(x<length):
        if(strList[x]=="A"):
            checker=0;
            break;
        x+=1;
    if(checker)and(len(newIn)>longest):
        longest=len(newIn);
        longestWord=newIn;

print("the longest word you entered was: "+longestWord+ " It was "+str(longest)+ " characters long!");