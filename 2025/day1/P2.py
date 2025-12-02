file = open("input.txt", "r")
lines = file.read().splitlines()

zeros = 0
current_pos = 50
for line in lines:
    rotation = int(line[1:])
    for i in range(0, rotation):
        current_pos = (current_pos + 1 * (-1 if line[0] == 'L' else 1)) % 100
        if current_pos == 0:
            zeros += 1

print(zeros)