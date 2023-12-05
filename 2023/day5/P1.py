import numpy
# modifier l'input et enlever les espaces dans les mots au
file = open("2023/day5/input.txt", "r")
 
maps = file.read().split("\n\n")

for i in range(len(maps)):
    maps[i] = maps[i].split("\n")
    for j in range(len(maps[i])):
        maps[i][j] = maps[i][j].split(" ")

seeds = numpy.zeros(len(maps[0][0])-1, dtype=int)
for i in range(len(maps)):
    changing = numpy.ones(len(seeds), dtype=int) # Vaut 1 si on a le droit de mapper le nombre i, 0 sinon
    match(i):
        case 0: # seeds
            for j in range(1, len(maps[0][0])):
                seeds[j-1] = int(maps[0][0][j])
        case _:
            for j in range(1, len(maps[i])):
                dest = int(maps[i][j][0])
                src = int(maps[i][j][1])
                rng = int(maps[i][j][2])
                for k in range(len(seeds)):
                    if changing[k] and src<=seeds[k] and seeds[k]<(src+rng):
                            seeds[k] = dest+seeds[k]-src
                            changing[k] = 0
print(min(seeds))