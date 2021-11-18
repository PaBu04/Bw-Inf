'''
Created on 03.11.2021

@author: Paul Buda
@contact: mailan@paulbuda.de
'''

from numpy import array, meshgrid, sum

#read the weights
weights = open("gewichtsstuecke.txt", "r")
#get the number of weights
numberWeights = int(weights.readline())

#Liste mit allen Gewichten
weightsList = []

#Liste mit möglicher Anzahl der Gewichte multipliziert mit dem Gewicht (Bsp. für 2*10g -> [-20, -10, 0, 10, 20])
amounts = []

for r in range(numberWeights):
    weight, amount = weights.readline().split()
    
    weightsList.append(int(weight))
    
    amounts.append([r * int(weight) for r in range(int(amount) * -1, int(amount) + 1)])

#berechnet alle Kombinationsmöglichkeiten der Gewichte
exec("meshgrid = meshgrid(" + str(amounts)[1:-1] + ")")
combs = array(meshgrid).T.reshape(-1, numberWeights)

#es muss nur die Hälfe der Kombinationsmöglichkeiten betrachtet werden, da die andere Hälfte genau den negativen Wert ergibt
combs = combs[:len(combs) // 2]

#berechnet die Summe der jeweiligen Verteilung
combsSum = sum(combs, axis = 1)

#es werden nur die Summen unter 11kg berücksichtigt
combsSum = combsSum[abs(combsSum) < 11000]

#erstellt eine Liste mit den Kombinationen und deren Summen [[[10, 100], 110], [[-10, 100], 90], ...]
possibleWeights = list(zip(combs, combsSum))

#sortiert die Gewichte nach Gewicht und dann nach Summe der einzelnen benötigten Gewichte
possibleWeights.sort(key = lambda w: (abs(w[1]), sum(abs(x) for x in w[0])))

#negiert die Gewichte falls die Summe der Gewichte negativ ist
possibleWeights = [([-w if (weight[1] < 0) else w for w in weight[0]], abs(weight[1])) for weight in possibleWeights]

#sortiert doppelt erzielte Summen aus, es werden hierbei die behalten, bei welchen man am wenigsten Gewichte braucht
first = possibleWeights[1]
possibleWeights = [(possibleWeights[r + 1]) for r in range(len(possibleWeights) - 1) if(possibleWeights[r + 1][1] != possibleWeights[r][1])]
possibleWeights.append(first)

#gibt die Ergebnisse aus
for r in range(10, 10010, 10):
    #sucht das Gewicht, welches am nächten am gesuchten Gewicht liegt
    mini = min(possibleWeights, key = lambda x:abs(x[1] - r))
    
    weightsRight = [(str(int(mini[0][r] / weightsList[r])) + "*" + str(weightsList[r]) + "g") for r in range(len(weightsList)) if(mini[0][r] > 0)]
    weightsLeft = [(str(int(abs(mini[0][r] / weightsList[r]))) + "*" + str(weightsList[r]) + "g") for r in range(len(weightsList)) if(mini[0][r] < 0)]
    
    print(str(r) + "g -> " + str(mini[1]) + "g\nRechts: " + str(weightsRight)[1:-1].replace("'", "") + "\nLinks: " + str(weightsLeft)[1:-1].replace("'", ""))
