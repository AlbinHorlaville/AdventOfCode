import numpy
# modifier l'input et enlever les espaces dans les mots au
file = open("2023/day5/input.txt", "r")
 
maps = file.read().split("\n\n")

for i in range(len(maps)):
    maps[i] = maps[i].split("\n")
    for j in range(len(maps[i])):
        maps[i][j] = maps[i][j].split(" ")

def checkAlreadyDid(alreadyDid, n):
    for i in range(0, len(alreadyDid), 2):
        if alreadyDid[i]<=n<alreadyDid[i+1]:
            return True
    return False

def checkAlreadyDidInterval(alreadyDid, start, end):
    lenfor = len(alreadyDid)
    for i in range(0, lenfor, 2):
        if (end<alreadyDid[i] or start>=alreadyDid[i+1]):
            return start, end
        elif (start<=alreadyDid[i] and alreadyDid[i]<end<alreadyDid[i+1]):
            return start, alreadyDid[i]
        elif (alreadyDid[i]<=start<=alreadyDid[i+1] and end>alreadyDid[i+1]):
            return alreadyDid[i+1], end
        elif (alreadyDid[i]<=start<=alreadyDid[i+1] and alreadyDid[i]<end<alreadyDid[i+1]):
            return -1, -1
        elif (start<=alreadyDid[i] and alreadyDid[i+1]<end):
            return (start, alreadyDid[i]), (alreadyDid[i+1], end)
    return start, end

def convert(start, end, maps):
    min = -1
    for seed in range(start, end):
        print(seed)
        movementS = seed
        # Si un nombre a déjà été soumis à l'algorithme, on ne lui soumet pas de nouveau
        #    if (not checkAlreadyDid(alreadyDid, movementS)):
        lenmaps = len(maps)
        # Parcours de tous les mapping dans l'ordre (l'algo)
        for j in range(1, lenmaps):
            lenmapsj = len(maps[j])
            # Parcours de toutes les lignes des mapping dans l'ordre (l'algo)
            for k in range(1, lenmapsj):
                dest = int(maps[j][k][0])
                src = int(maps[j][k][1])
                rng = int(maps[j][k][2])
                # Si la seed est transformé, on peut arrêter de scanner le mapping courant et passer au suivant
                if src<=movementS<(src+rng):
                        movementS = dest+movementS-src
                        break
        if min==-1 or movementS < min:
            min = movementS
    return min

alreadyDid = []
minimum = -1
# Parsing des seeds
lenmapsforseed = len(maps[0][0])-1
for i in range(1, lenmapsforseed, 2): 
    start = int(maps[0][0][i])
    lenght = int(maps[0][0][i+1])
    
    start, end = checkAlreadyDidInterval(alreadyDid, start, start+lenght)
    if start==-1:
        continue
    try:
        start1, end1 = start
        start2, end2 = end
        # intervale 1
        movementS = convert(start1, end1, maps)
        if minimum==-1 or movementS<minimum:
            minimum = movementS
        alreadyDid.append(start1)
        alreadyDid.append(end1)
        #intervale 2
        movementS = convert(start2, end2, maps)
        if minimum==-1 or movementS<minimum:
            minimum = movementS
        alreadyDid.append(start2)
        alreadyDid.append(end2)
    except:
        # Parcours de tous les intervalles de seeds
        movementS = convert(start, end, maps)
        if minimum==-1 or movementS<minimum:
            minimum = movementS
        alreadyDid.append(start)
        alreadyDid.append(end)
print(minimum)