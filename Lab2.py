from random import random

totalBalls = 100
a = int(input('Number of azure balls: '))
assert a > 0, "Number of azure balls should be above 0."
c = totalBalls - a
trials = 2000

aTrials = 0 # Number of trials where last ball was azure
cTrials = 0 # Number of trials where last ball was carmine

for trial in range(trials):
    lastBall = 2 # Used to track the color of the last ball, if azure then 0, if carmine then 1. Currently set to 2 meaning nothing has been done yet
    selectedBall = 2 # Used to track the color of the selected ball, if azure then 0, if carmine then 1. Current set to 2 meaning nothing has been done yet
    trialBalls = totalBalls

    A = a # A is just a copy of a so during the trials the original value of a is kept
    C = c # C is just a copy of c so during the trials the original value of c is kept

    while (trialBalls > 0):
        
        probabilityA = A/trialBalls # Probability of choosing an azure ball
        probabilityC = 1-probabilityA # Probability of choosing carmine ball, left here just for convenience
        R = random()

        # Picks a random ball
        if R < probabilityA:
            selectedBall = 0
        else:
            selectedBall = 1

        #If previous ball was the same color as new selected ball then discard the chosen ball
        if selectedBall == lastBall:
            trialBalls -= 1
            if selectedBall == 0:
                A -= 1
            else:
                C -= 1

        lastBall = selectedBall

    #Tallies the final ball selected
    if selectedBall == 0:
        aTrials += 1
    else:
        cTrials += 1

percentageA = aTrials/trials #Frequency of times azure ball was the last picked
print("Relative frequency that last ball was azure: ", percentageA)