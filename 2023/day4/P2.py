import numpy

file = open("2023/day4/input.txt", "r")
cards = file.read().splitlines()

# cards[i] -> liste de nombres gagnants, liste de nombres dont on dispose
for i in range(len(cards)):
    cards[i] = cards[i][8:len(cards[i])]
    cards[i] = cards[i].split("|")
    cards[i][0] = cards[i][0].split(" ")
    cards[i][1] = cards[i][1].split(" ")

cardsNumber = numpy.ones(len(cards), dtype=int)
for i in range(len(cards)):
    ratio=0
    for jW in range(len(cards[i][0])): # jWinning et jOwning
        for jO in range(len(cards[i][1])):
            if cards[i][0][jW]!="" and cards[i][0][jW]==cards[i][1][jO]:
                ratio+=1
    for k in range(ratio):
        cardsNumber[i+k+1]+=cardsNumber[i]
sum=0
for i in range(len(cardsNumber)):
    sum+=cardsNumber[i]
print(sum)