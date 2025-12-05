file = open("input.txt", "r")
lines = file.read().splitlines()

result = 0
for line in lines:
    # Récupérer le max (ne peut pas être le dernier indice)
    max_l = -1
    max_indice = 0
    for i in range(0, len(line)-1):
        if int(line[i]) > max_l:
            max_l = int(line[i])
            max_indice = i
    
    max_r = 0
    # Puis récupérer le max parmis les numéro
    for i in range(max_indice+1, len(line)):
        if int(line[i]) > max_r:
            max_r = int(line[i])
    
    result += max_l * 10 + max_r

print(result)