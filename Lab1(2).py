#Program meant to simulate Bob fliping n+1 coins and Alice fliping n coins,
#and showing that the probability that Bob flips more heads than Alice is 1/2

#Can specify loaded coins

from random import random

n = int(input('n:')) #Number of coins that will be flipped

p = float(input('p:')) #Probabily of flipping heads

trials = 1000

BobWins = 0 #Used to track how many trials where Bob flips more heads

for trial in range(trials):
    BobHeadCount = 0
    AliceHeadCount = 0

    #Flips n coins for both Bob and Alice 
    for i in range(n):
        AliceR = random()
        if AliceR < p:
            AliceHeadCount += 1

    #Do an extra flip for Bob (because Bob flips n+1 coins)
    for i in range(n+1):
        BobR = random()
        if BobR < p:
            BobHeadCount+=1

    #Compares number of heads Alice and Bob flipped and if 
    #Bob wins then it adds to the total number of times Bob
    #has won
    if BobHeadCount > AliceHeadCount:
        BobWins += 1

#Finds percentage of games that Bob won
percentageBobWins = BobWins/trials

print("Bob won:", percentageBobWins, "percent of the games.")