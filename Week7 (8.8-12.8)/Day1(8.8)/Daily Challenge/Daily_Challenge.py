import random
import pandas as pd
import numpy as np

def create_table(M,N):
    if M<50 and N<40:
        l=[[random.randint(1,100) for j in range(N)] for i in range(M)]
    return l



# ###Step 1###########
n=create_table(30,30)

# ###Step 2###########
# print(n[3])


# ###Step 3##########
# print(n[3])
#####a second way to print the column
## for i in range(len(n[3])):
##     print(n[3][i])





###Step 4###########
# for i in range(len(n[-1])):
#     n[-1][i]=7
# print(n[-1])

# # line break
# print("")

########Step 5############
# for i in range(len(n[1])):
#     sum_first_two=n[i][0]+n[i][1]
#     n[i][-1]=sum_first_two

# print(n)






# ########Repeat all 5 steps with NumPy###############






def create_mat(M,N):
    if M<50 and N<40:
        return np.random.randint(1,101,(M,N))

##Step 1################
m=create_mat(5,5)
print(m)

##Step 2#################
####Note: I maybe should have used m[2] instead of m[3] here- I wasn't sure what was wanted
# print(m[3])



##Step 3#################
# print(m[:,2])



##Step 4#################
m[-1,:]=7

##Step 5#################
m[:,-1]=m[:,0]+m[:,1]
print(m)