
# Scanning a square 3x3 around the point (i,j)
def scanning_S(map, i, j):
    # haut
    if map[i-1][j]=="|" or map[i-1][j]=="7" or map[i-1][j]=="F":
        return [map[i-1][j]], i-1, j
    # droite
    if map[i][j+1]=="J" or map[i][j+1]=="7" or map[i][j+1]=="-":
        return map[i][j+1], i, j+1
    # bas
    if map[i+1][j]=="|" or map[i+1][j]=="J" or map[i+1][j]=="L":
        return map[i+1][j], i+1, j
    # gauche
    if map[i][j-1]=="-" or map[i][j-1]=="L" or map[i][j-1]=="F":
        return map[i][j-1], i, j-1
    raise ValueError

# (i,j) les coordonnées du tuyau d'avant
# (k,l) les coordonnées du tuyau avant le tuyau d'avant
def scanning(map, i, j, k, l):
    match map[i][j]:
        case "F":
            if k==i+1 and l==j:
                return map[i][j+1], i, j+1
            else:
                return map[i+1][j], i+1, j
        case "7":
            if k==i and l==j-1:
                return map[i+1][j], i+1, j
            else:
                return map[i][j-1], i, j-1
        case "|":
            if k==i+1 and l==j:
                return map[i-1][j], i-1, j
            else:
                return map[i+1][j], i+1, j
        case "-":
            if k==i and l==j-1:
                return map[i][j+1], i, j+1
            else:
                return map[i][j-1], i, j-1
        case "J":
            if k==i-1 and l==j:
                return map[i][j-1], i, j-1
            else:
                return map[i-1][j], i-1, j
        case "L":
            if k==i-1 and l==j:
                return map[i][j+1], i, j+1
            else:
                return map[i-1][j], i-1, j
        case _:
            raise ValueError

file = open("2023/day10/input.txt", "r")

map = file.read().split("\n")

print(map)

# Finding S
s = -1,-1
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j]=="S":
            s = i, j

l=["S"]
cell, i, j = scanning_S(map, s[0], s[1])
l.append(cell)
prev_i = s[0]
prev_j = s[1]
while l[-1]!="S":
    current_i = i
    current_j = j
    cell, i, j = scanning(map, i, j, prev_i, prev_j)
    prev_i = current_i
    prev_j = current_j
    l.append(cell)
print((len(l)-1)//2)