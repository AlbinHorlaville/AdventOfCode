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

distance = 0
for i in range(len(left)):
    distance += abs(left[i] - right[i])

print(distance)
