'''
Created on 03.11.2021

@author: Paul Buda
'''

from numpy import array, meshgrid, multiply
import time

start = time.time()

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
    
    amounts.append([r for r in range(int(amount) * -1, int(amount) + 1)])
    calcs *= int(amount) * 2 + 1

print("Needed Time: " + str(int((calcs - 1) / 2) / 130000) + "s")

#from : https://stackoverflow.com/questions/1208118
exec("meshgrid = meshgrid(" + str(amounts)[1:-1] + ")")
combs = array(meshgrid).T.reshape(-1, numberWeights)
combs = combs[:len(combs) // 2]

#calculate all possible sums
possibleWeights = list(zip(combs, [sum(multiply(weightsList, multiplier)) for multiplier in combs if(abs(sum(multiply(weightsList, multiplier))) < 11000)]))

#sort in ascending order according to the weights and the number of weights required
possibleWeights.sort(key = lambda w: (w[1], sum(abs(x) for x in w[0])), reverse = True)

#Reverse the sign if the sum of the weight is negative
possibleWeights = [([-w if (weight[1] < 0) else w for w in weight[0]], -weight[1]) for weight in possibleWeights]

last = possibleWeights[-1]
possibleWeights = [(possibleWeights[r]) for r in range(len(possibleWeights) - 1) if(possibleWeights[r + 1][1] != possibleWeights[r][1])]
possibleWeights.append(last)

print(time.time() - start)
#sort the values
for r in range(10, 10010, 10):
    
    mini = min(possibleWeights, key = lambda x:abs(x[1] - r))
    weightsRight = [(str(mini[0][r]) + "*" + str(weightsList[r]) + "g") for r in range(len(weightsList)) if(mini[0][r] > 0)]
    weightsLeft = [(str(abs(mini[0][r])) + "*" + str(weightsList[r]) + "g") for r in range(len(weightsList)) if(mini[0][r] < 0)]
    print(str(r) + "g -> " + str(mini[1]) + "g\nRight: " + str(weightsRight)[1:-1].replace("'", "") + "\nLeft: " + str(weightsLeft)[1:-1].replace("'", ""))
    
print(time.time() - start)
