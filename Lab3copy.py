from random import random

n = int(input('Number of weeks: '))
p = float(input('Probability of playing each week: '))
q = float(input('Probability of winning: '))

trials = 100000

# Dictionary of arrays to hold frequencies of outcomes, key would correspond to x values and the array are the y
# values corresponding to the said x value
trialData = {}
for i in range(n+1):
    trialData[i] = []
    for j in range(n+1):
        trialData[i].append(0)

for trial in range(trials):
    x = 0 # Weeks played
    y = 0 # Weeks won

    # For n weeks:
    # x is the number of weeks played, the probability a game was played that week is p
    # and the chances of winning said game is q and the amount of games won is tracked by y
    for i in range(n):
        xR = random()
        if xR < p:
            x += 1
            yR = random()
            if yR < q:
                y += 1

    trialData[x][y] += 1 # Append x,y values to trial data 
        
# Finding Joint PMF pX,Y(x,y), frequency/trials
joint = {}
for i in range(n+1):
    joint[i] = []

for key in trialData:
    for element in trialData[key]:
        relativeFrequency = element/trials
        joint[key].append(relativeFrequency)

# Printing Joint PMF pX,Y(x,y)
print('')
# Set up for top of the table
print('Joint PMF of X and Y')
print('  y:', end=" ")
for i in range(n+1):
    print(i, end="      ")
print('')
line = ''
for i in range(n*9):
    line += '-'
print("x---"+line)
# Printing contents of dictionary
for key in joint:
    print(key, ' | ', end='')
    i = 0
    for element in joint[key]:
        if i <= key:
            print('%.4f' % element, end=' ')
        i+=1
    print('')


# Finding marginal PMF's of X and Y
# To get marginal X you need to sum all the values in the row from joint PMF
# Index corresponds to value of x, like x=0 when i=0
marginalX = []
for key in joint:
    sum = 0
    for element in joint[key]:
        sum += element
    marginalX.append(sum)

# To get marginal Y you need to sum all the values in the column
# Index corresponds to values of y
marginalY = []
for i in range(n+1):
    marginalY.append(0)
for key in joint:
    for i in range(len(joint[key])):
        marginalY[i] = marginalY[i] + joint[key][i]
        

# Finding Conditional PMFX|Y(x|y), PMFX|Y(x|y) = pX,Y(x,y)/pY(y)
conditionalXY = {}
for i in range(n+1):
    conditionalXY[i] = []
for key in joint:
    i = 0
    for element in joint[key]:
        conditional = element/marginalY[i]
        conditionalXY[key].append(conditional)
        i+=1

# Printing Conditional PMFX|Y(x|y)
print('')
# Set up for top of the table
print('Conditional PMF of X given Y')
print('  y:', end=" ")
for i in range(n+1):
    print(i, end="      ")
print('')
line = ''
for i in range(n*9):
    line += '-'
print("x---"+line)
# Printing contents of dictionary
for key in conditionalXY:
    print(key, ' | ', end='')
    i = 0
    for element in conditionalXY[key]:
        if i <= key:
            print('%.4f' % element, end=' ')
            i+=1
    print('')


# Finding Conditional PMFY|X(y|x), PMFY|X(y|x) = pX,Y(x,y)/pX(x)
conditionalYX = {}
for i in range(n+1):
    conditionalYX[i] = []
for key in joint:
    for element in joint[key]:
        conditional = element/marginalX[key]
        conditionalYX[key].append(conditional)

# Printing Conditional PMFY|X(y|x)
print('')
# Set up for top of the table
print('Conditional PMF of Y given X')
print('  y:', end=" ")
for i in range(n+1):
    print(i, end="      ")
print('')
line = ''
for i in range(n*9):
    line += '-'
print("x---"+line)
# Printing contents of dictionary
for key in conditionalYX:
    print(key, ' | ', end='')
    i = 0
    for element in conditionalYX[key]:
        if i <= key:
            print('%.4f' % element, end=' ')
        i+=1
    print('')