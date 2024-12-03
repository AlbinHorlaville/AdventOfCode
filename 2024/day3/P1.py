file = open("2024/day3/input.txt", "r")

parseFile = file.read().split("mul(")
result = 0
for multiplication in parseFile:
    try:
        multiplication = multiplication.split(")")[0].split(",")

        if len(multiplication) > 2:
            continue

        X = multiplication[0]
        Y = multiplication[1]

        result += int(X) * int(Y)
    except:
        continue

print(result)
