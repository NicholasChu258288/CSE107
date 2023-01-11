from random import random

p = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] #Probability of flipping heads with Coin 1 
q = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] #Probability of flipping heads with Coin 2
trials = 10000

#Array of arrays to represent table for results
#Each array is a row and each elemenet is in its own column
#Eg. mean[0][0] is when p = 0.1 and q = 0.1
mean = [] 
variance = []

for probP in p:
    #Lists to hold results of tirals which will be appended to mean and variance
    #for each p to create tables
    meanRow = []
    varianceRow = []
    
    for probQ in q:
        
        trialResults = [] #Stores results of each trial which is used for caluclation later
        
        for trial in range(trials):
            N = 0 #Number of flips needed to get first head using Coin 1
            Y = 0 #Number of heads when flipping Coin 2 N times

            Nside = 2 #Used to track which side Coin 1 landed on, 0 for tails and 1 for heads (2 because nothing was flipped yet)
            
            #Flips Coin 1 until first heads, tracking N which is number of flips needed before first heads
            while (Nside != 1):
                NR = random()
                if NR < probP:
                    Nside = 1
                else:
                    Nside = 0
                N+=1

            for flip in range(N):
                YR = random()
                if YR < probQ:
                    Y+=1
            
            trialResults.append(Y)
        
        #Calculating mean of sample space
        trialMean = 0
        for result in trialResults:
           trialMean += result
        trialMean = trialMean/trials
        #Append result to meanRow
        meanRow.append(trialMean)

        #Calculating variance of sample space
        trialVariance = 0
        for result in trialResults:
            v = result-trialMean
            v = v*v
            trialVariance += v
        trialVariance = trialVariance/(trials-1)
        varianceRow.append(trialVariance)
    
    mean.append(meanRow)
    variance.append(varianceRow)

#Printing mean table
print('mean')
print("    q:  ", end='')
for element in q:
    print(element, "    ", end ='')
print('')

line = ''
for i in range(len(q)*9):
    line += '-'
print("p  ", line)

row = 0
for element in p:
    print(element, "| ", end='  ')
    for element in mean[row]:
        print('%.4f' % element, end='  ')
    row += 1
    print('')

print('')



#Printing variance table
print('variance')
print("    q:  ", end='')
for element in q:
    print(element, "    ", end ='')
print('')

line = ''
for i in range(len(q)*9):
    line += '-'
print("p  ", line)

row = 0
for element in p:
    print(element, "| ", end='  ')
    for element in variance[row]:
        print('%.4f' % element, end='  ')
    row += 1
    print('')
