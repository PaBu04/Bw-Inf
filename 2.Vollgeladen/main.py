'''
Created on 02.11.2021

@author: Paul Buda
'''

#ließt die Datei mit den Infos zu den Hotels ein
hotels = open("hotels.txt", "r")
#speichert die Gesamtanzahl an Hotels
numberHotels = int(hotels.readline())
#speichert die Gesamtreisestrecke
totalDistance = int(hotels.readline())

#ließt alle Hotels aus der Datei ein
hotelsList = [[-1, 0]]
for r in range(numberHotels):
    hotelKm, hotelRating = hotels.readline().split()
    
    #wenn am gleiche Reisekilometer mehrere Hotels stehen, wird nur das bestbewertete ausgewählt
    if(hotelsList[-1][0] == int(hotelKm)):
        hotelsList[-1][1] = max(float(hotelRating), hotelsList[-1][1])
    else:
        hotelsList.append([int(hotelKm), float(hotelRating)])
        
hotels.close()
#sortiert die Hotels nach deren Bewertung
hotelsList.sort(key=lambda x: x[1], reverse=True)

checkHotels = []
allCheckHotels = [0, totalDistance]
for hotel in hotelsList:
    canUsed = True
    allCheckHotels.append(hotel[0])
    allCheckHotels.sort()
    checkHotels = allCheckHotels.copy()
    minus = 0
    
    for r in range(len(checkHotels) - 2):
        if(checkHotels[r + 2 - minus] - checkHotels[r - minus] <= 360):
            del checkHotels[r + 1 - minus]
            minus += 1
            
    for r in range(len(checkHotels) - 1):
        if(checkHotels[r + 1] - checkHotels[r] > 360):
            canUsed = False
            break
        
    if(canUsed and len(checkHotels) <= 6):
        #ließt die Hotels welche benötigt werden mit Km Angabe und Bewertung aus
        useHotels = [hotel for hotel in hotelsList if(hotel[0] in checkHotels[1:-1])]
        #sortiert die Hotels nach km
        useHotels.sort(key=lambda x: x[0])
        
        #gibt die Hotels nacheinander aus
        [print("Das Hotel nach: " + str(hotel[0]) + " km hat eine Bewertung  " + str(hotel[1]) + " Sternen!") for hotel in useHotels]
        break

#gibt die Sterne, des am schlechtesten bewertete Hotel aus
print("Das am schlechtesten bewertete Hotel hat: " + str(min(hotel[1] for hotel in useHotels)) + " Sterne")
