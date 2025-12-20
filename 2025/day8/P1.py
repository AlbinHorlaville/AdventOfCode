file = open("input.txt", "r")
coords = file.read().splitlines()
for j in range(len(coords)):
    coords[j] = coords[j].split(',')
    for i in range(len(coords[j])):
        coords[j][i] = int(coords[j][i])
circuits = []
closest_pairs = []

for i in range(len(coords)):
    for j in range(i, len(coords)):
        if i==j: continue
        distance_square = pow(coords[i][0]-coords[j][0], 2) + pow(coords[i][1]-coords[j][1], 2) + pow(coords[i][2]-coords[j][2], 2)
        pair = [(i, j), distance_square]
        closest_pairs.append(pair)

# Nouvelle idée: Faire la liste des 10 ou 1000 pairs les plus proches puis itérer dessus
closest_pairs.sort(key= lambda x: x[1])

def get_index(x):
    for i in range(len(circuits)):
        if x in circuits[i]:
            return i
    return -1

i=0
while True:
    x, y = closest_pairs[i][0]
    index_x = get_index(x)
    index_y = get_index(y)
    if index_x == index_y and not (index_x == -1 and index_y == -1):
        i+=1
        continue
    if index_x == -1 and index_y == -1:
        circuits.append([x, y])
    elif index_x != -1 and index_y != -1:
        # merge les deux array
        old_array_x = circuits[index_x]
        old_array_y = circuits[index_y]
        new_array = old_array_x + old_array_y
        circuits.remove(old_array_x)
        circuits.remove(old_array_y)
        circuits.append(new_array)
    elif index_x != -1:
        circuits[index_x].append(y)
    elif index_y != -1:
        circuits[index_y].append(x)
    i+=1
    if len(circuits[0]) == 1000:
        break

print(coords[x][0] * coords[y][0])
