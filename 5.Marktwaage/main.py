'''
Created on 03.11.2021

@author: Paul Buda
'''

from numpy import array
from numpy import meshgrid
import time

start = time.time()

#read the weights
weights = open("gewichtsstuecke.txt")
#get the number of weights
numberWeights = int(weights.readline())

calcs = 1
weightsList = []
amounts = []
for r in range(numberWeights):
    all = weights.readline()
    
    weight = int(all.split()[0])
    weightsList.append(weight)
    
    amount = int(all.split()[1])
    amounts.append([r for r in range(amount * -1, amount + 1)])
    calcs *= amount * 2 + 1
    
print(weightsList)
print("Needed Calculations: " + str(int((calcs - 1) / 2)))
print("Needed Time: " + str(int((calcs - 1) / 2) / 30000) + "s")

#from : https://stackoverflow.com/questions/1208118
exec("meshgrid = meshgrid(" + str(amounts)[1:-1] + ")")
combs = array(meshgrid).T.reshape(-1, numberWeights)
combs = combs[:len(combs) // 2]

#calculate all possible sums
possibleWeights = [([m for m in multiplier], sum([w * m for w, m in zip(weightsList, multiplier)])) for multiplier in combs]

#sort in ascending order according to the weights and the number of weights required
possibleWeights.sort(key = lambda w: (w[1], sum(abs(x) for x in w[0])), reverse = True)

#Reverse the sign if the sum of the weight is negative
possibleWeights = [([-w if (weight[1] < 0) else w for w in weight[0]], -weight[1]) for weight in possibleWeights if(weight[1] < 11000 and weight[1] > -11000)]

last = possibleWeights[-1]
possibleWeights = [(possibleWeights[r]) for r in range(len(possibleWeights) - 1) if(possibleWeights[r + 1][1] != possibleWeights[r][1])]
possibleWeights.append(last)

row = [w[1] for w in possibleWeights]

#sort the values
for r in range(10, 10010, 10):
    
    mini = min(possibleWeights, key = lambda x:abs(x[1] - r))
    weightsRight = [(str(mini[0][r]) + "*" + str(weightsList[r]) + "g") for r in range(len(weightsList)) if(mini[0][r] > 0)]
    weightsLeft = [(str(abs(mini[0][r])) + "*" + str(weightsList[r]) + "g") for r in range(len(weightsList)) if(mini[0][r] < 0)]
    print(str(r) + "g -> " + str(mini[1]) + "g\nRight: " + str(weightsRight)[1:-1].replace("'", "") + "\nLeft: " + str(weightsLeft)[1:-1].replace("'", ""))
    
print(time.time() - start)
