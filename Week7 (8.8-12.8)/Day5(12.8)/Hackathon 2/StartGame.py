import random
from array import *







# def newGame(self):
#     # myStats = open("stats.txt", "w")
#     # gameStats=[]



# generate a 3x3 board with 2 hidden mines
def startGame(size, mineNum):
    board=[]
    for r in range(size):
        for c in range(size):
            print(c,end = " ")


    for r in board:
        for c in r:
            print(c,end = " ")
        print()

    print(random.choice(board))
    print(random.choice(board))
    mines=[[],[]]







startGame(3,2)