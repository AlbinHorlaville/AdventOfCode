file = open("input.txt", "r")
lines = file.read().splitlines()

# Isoler les symboles
for i in range(8, 1, -1):
    lines[-1] = lines[-1].replace(' '*i, ' ')
lines[-1] = lines[-1].split(' ')
last_symbol = lines[-1][-2]

# Construire les nombres (de haut en bas)
problems = []
k = 0
for i in range(len(lines[0])):
    problem = ''
    number = ''
    for j in range(len(lines)-1):
        if lines[j][i] != ' ':
            number += lines[j][i]
        if j == len(lines)-2:
            problem += number
    if problem == '':
        problem = lines[-1][k]
        k+=1
    problems.append(problem)
problems.append(last_symbol)

# Calculer les problèmes
operation = []
result = 0
for i in range(len(problems)):
    if problems[i] == '+':
        add = 0
        for n in operation:
            add += n
        result += add
        print(add)
        operation = []
    elif problems[i] == '*':
        mult = 1
        for n in operation:
            mult *= n
        result += mult
        print(mult)
        operation = []
    else: # Add number to operation
        operation.append(int(problems[i]))

print(result)
