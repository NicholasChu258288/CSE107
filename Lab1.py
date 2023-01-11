#Program meant to simulate Bob fliping n+1 coins and Alice fliping n coins,
#and showing that the probability that Bob flips more heads than Alice is 1/2

#Assuming Fair Coin

from random import random

n = input('n:') #Asks for how many n coins will be flipped

trials = 1000

BobWins = 0 #Used to track how many trials where Bob flips more heads

for trial in range(trials):
    BobHeadCount = 0
    AliceHeadCount = 0

    #Flips n coins for both Bob and Alice 
    for i in range(int(n)):
        #Random will generates random number from [0.0, 1),
        #any number below 0.5 will represent heads and any
        #number abocce it will represent tails.
        BobR = random()
        if BobR < 0.5:
            BobHeadCount += 1

        AliceR = random()
        if AliceR < 0.5:
            AliceHeadCount += 1

    #Do an extra flip for Bob (because Bob flips n+1 coins)
    BobR = random()
    if BobR < 0.5:
        BobHeadCount+=1

    #Compares number of heads Alice and Bob flipped and if 
    #Bob wins then it adds to the total number of times Bob
    #has won
    if BobHeadCount > AliceHeadCount:
        BobWins += 1

#Finds percentage of games that Bob won
percentageBobWins = BobWins/trials

print("Bob won: ", percentageBobWins, "percent of the games.")