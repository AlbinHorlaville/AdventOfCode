file = open("2024/day3/input.txt", "r")

doParse = file.read().split("do()")
result = 0
for sequence in doParse:
    mulParse = sequence.split("mul(")
    
    for i in range(1, len(mulParse)):
        if "don't()" in mulParse[i-1]:
            break # On sort de la séquence puisque toutes celles de droites sont désactivées
        # Sinon on regarde si multiplication il y a
        try:
            multiplication = mulParse[i].split(")")[0].split(",")

            if len(multiplication) > 2:
                continue

            X = multiplication[0]
            Y = multiplication[1]

            result += int(X) * int(Y)
        except:
            continue

print(result)
