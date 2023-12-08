import random
# Tri rapide
file = open("2023/day7/input.txt", "r")

hands = file.read().split("\n")


for i in range(len(hands)):
    hands[i] = hands[i].split(" ")

def getStrength(hand):
    triple = False
    pair = False
    pairC = ""
    for i in range(len(hand)):
        nb_card_i = 1
        for j in range(len(hand)):
            if i==j:
                continue
            if hand[i]==hand[j]:
                nb_card_i+=1
        if not triple and nb_card_i==3:
            triple = True
        if nb_card_i==5:
            return 7 # Five of a Kind
        if nb_card_i==4:
            return 6 # Four of a Kind
        if triple and pair:
            return 5 # Full House
        if pair and (not pairC==hand[i]) and nb_card_i==2:
            return 3 # Two pair
        if not pair and nb_card_i==2:
            pair = True
            pairC+=hand[i]
    if triple:
        return 4 # Three of a Kind
    if pair:
        return 2 # One pair
    return 1

def compare(T, i, j): # Renvoie 1 si T[i]<T[j] dans l'ordre du poker, 0 sinon
    if i==j:
        return 1
    hand_i = T[i][0]
    hand_j = T[j][0]

    strength_i = getStrength(hand_i)
    strength_j = getStrength(hand_j)
    if strength_i < strength_j:
        return 1
    if strength_i==strength_j:
        k=0
        while hand_i[k]==hand_j[k]:
            k+=1
        if hand_i[k]=="2":
            return 1 # i est donc plus petit
        if hand_i[k]=="3":
            if hand_j[k]=="2":
                return 0
            else:
                return 1
        if hand_i[k]=="4":
            if hand_j[k]=="2" or hand_j[k]=="3":
                return 0
            else:
                return 1
        if hand_i[k]=="5":
            if hand_j[k]=="2" or hand_j[k]=="3" or hand_j[k]=="4":
                return 0
            else:
                return 1
        if hand_i[k]=="6":
            if hand_j[k]=="2" or hand_j[k]=="3" or hand_j[k]=="4" or hand_j[k]=="5":
                return 0
            else:
                return 1
        if hand_i[k]=="7":
            if hand_j[k]=="2" or hand_j[k]=="3" or hand_j[k]=="4" or hand_j[k]=="5" or hand_j[k]=="6":
                return 0
            else:
                return 1
        if hand_i[k]=="8":
            if hand_j[k]=="2" or hand_j[k]=="3" or hand_j[k]=="4" or hand_j[k]=="5" or hand_j[k]=="6" or hand_j[k]=="7":
                return 0
            else:
                return 1
        if hand_i[k]=="9":
            if hand_j[k]=="A" or hand_j[k]=="K" or hand_j[k]=="Q" or hand_j[k]=="J" or hand_j[k]=="T":
                return 1
            else:
                return 0
        if hand_i[k]=="T":
            if hand_j[k]=="A" or hand_j[k]=="K" or hand_j[k]=="Q" or hand_j[k]=="J":
                return 1
            else:
                return 0
        if hand_i[k]=="J":
            if hand_j[k]=="A" or hand_j[k]=="K" or hand_j[k]=="Q":
                return 1
            else:
                return 0
        if hand_i[k]=="Q":
            if hand_j[k]=="A" or hand_j[k]=="K":
                return 1
            else:
                return 0
        if hand_i[k]=="K":
            if hand_j[k]=="A":
                return 1
            else:
                return 0
    return 0

def echanger(T, a, b):
    tempo = T[a]
    T[a] = T[b]
    T[b] = tempo

def choix_pivot(T, premier, dernier):
     return random.randint(premier, dernier)

def partitionner(T, premier, dernier, pivot):
    echanger(T, pivot, dernier)
    j = premier
    for i in range(premier,dernier):
        if compare(T, i, dernier): # Condition à changer
            echanger(T, i, j)
            j+=1
    echanger(T, dernier, j)
    return j

def tri_rapide(T, premier, dernier):
        if premier < dernier:
            pivot = choix_pivot(T, premier, dernier)
            pivot = partitionner(T, premier, dernier, pivot)
            tri_rapide(T, premier, pivot-1)
            tri_rapide(T, pivot+1, dernier)

tri_rapide(hands, 0, len(hands)-1)

sum=0
for i in range(len(hands)):
    sum+=int(hands[i][1])*(i+1)
print(sum)