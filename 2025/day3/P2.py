file = open("input.txt", "r")
lines = file.read().splitlines()

result = 0
for line in lines:
    # Récupérer le max (ne peut pas être le 11ème dernier indice)
    max = -1
    max_indice = 0
    for i in range(0, len(line)-11):
        if int(line[i]) > max:
            max = int(line[i])
            max_indice = i

    joltage = max
    
    # Boucle while pour trouver les 11 autres nombres
    for j in range(11):
        max = -1
        # Puis récupérer le max parmis les numéro
        for i in range(max_indice+1, len(line)-10+j):
            if int(line[i]) > max:
                max = int(line[i])
                new_max_indice = i
        
        joltage = joltage * 10 + max
        max_indice = new_max_indice
    result += joltage
    print(joltage)

print(result)