file = open("2024/day1/input.txt", "r")
lines = file.read().splitlines()

left = []
right = []

# On forme les deux listes
for line in lines:
    left.append(int(line.split(" ")[0]))
    right.append(int(line.split(" ")[1]))

left.sort()
right.sort()

similarity = 0
i = 0
while i < len(left):
    # Compte le nombre à gauche
    i_next = i+1
    count_left_number = 1
    while(i < len(left) - 1 and left[i] == left[i_next]): # On s'arrête 1 avant la fin pour ne pas dépasser la fin du tableau
        count_left_number += 1
        i_next += 1
    
    # Compte le nombre à droite
    j = 0
    count_right_number = 0
    while j < len(right) and right[j] <= left[i]:
        if right[j] == left[i]:
            count_right_number += 1
        j += 1
    
    # Calcul de la similarité pour le nombre de gauche
    similarity += left[i] * count_left_number * count_right_number
    
    i = i_next

print(similarity)
