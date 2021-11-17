'''
Created on 03.11.2021

@author: Paul Buda

'''

from numpy import array, meshgrid
from time import time
import numpy

start = time()

#read the weights
weights = open("gewichtsstuecke.txt", "r")
#get the number of weights
numberWeights = int(weights.readline())

calcs = 1
weightsList = []
amounts = []
for r in range(numberWeights):
    weight, amount = weights.readline().split()
    
    weightsList.append(int(weight))
    
    amounts.append([r * int(weight) for r in range(int(amount) * -1, int(amount) + 1)])
    calcs *= int(amount) * 2 + 1

#from : https://stackoverflow.com/questions/1208118
exec("meshgrid = meshgrid(" + str(amounts)[1:-1] + ")")
combs = array(meshgrid).T.reshape(-1, numberWeights)
combs = combs[:len(combs) // 2]
combsSum = list(numpy.sum(combs, axis = 1))

print(time() - start)
#calculate all possible sums
possibleWeights = list(zip(combs, [multiplier for multiplier in combsSum if(abs(multiplier) < 11000)]))
print(time() - start)

#sort in ascending order according to the weights and the number of weights required
possibleWeights.sort(key = lambda w: (abs(w[1]), sum(abs(x) for x in w[0])), reverse = True)

#Reverse the sign if the sum of the weight is negative
possibleWeights = [([-w if (weight[1] < 0) else w for w in weight[0]], abs(weight[1])) for weight in possibleWeights]

last = possibleWeights[-1]
possibleWeights = [(possibleWeights[r]) for r in range(len(possibleWeights) - 1) if(possibleWeights[r + 1][1] != possibleWeights[r][1])]
possibleWeights.append(last)

for r in range(10, 10010, 10):
    mini = min(possibleWeights, key = lambda x:abs(x[1] - r))
    weightsRight = [(str(int(mini[0][r] / weightsList[r])) + "*" + str(weightsList[r]) + "g") for r in range(len(weightsList)) if(mini[0][r] > 0)]
    weightsLeft = [(str(int(abs(mini[0][r] / weightsList[r]))) + "*" + str(weightsList[r]) + "g") for r in range(len(weightsList)) if(mini[0][r] < 0)]
    print(str(r) + "g -> " + str(mini[1]) + "g\nRechts: " + str(weightsRight)[1:-1].replace("'", "") + "\nLinks: " + str(weightsLeft)[1:-1].replace("'", ""))
    
print(time() - start)
