file = open("input.txt", "r")
lines = file.read().splitlines()

# Enlever les espaces inutiles
for i in range(len(lines)):
    for j in range(8, 1, -1):
        lines[i] = lines[i].replace(' '*j, ' ')
    lines[i] = lines[i].split(' ')
    if lines[i][0] == '':
        lines[i] = lines[i][1:]
    if lines[i][-1] == '':
        lines[i] = lines[i][:-1]
    if i == len(lines)-1: break
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])

# Mettre à 1 ou 0 en fonction de + et *
problems = [0]*len(lines[-1])
for i in range(len(problems)):
    problems[i] = 0 if lines[-1][i] == '+' else 1

# Calculer les problemes
for i in range(len(lines)-1):
    for j in range(len(lines[i])):
        match lines[-1][j]:
            case '+':
                problems[j] += lines[i][j]
            case '*':
                problems[j] *= lines[i][j]

# Calculer la somme totale
result = 0
for i in range(len(problems)):
    result += problems[i]

print(result)
