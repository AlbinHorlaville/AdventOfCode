file = open("input.txt", "r")
lines = file.read().splitlines()

zeros = 0
current_pos = 50
for line in lines:
    rotation = int(line[1:]) * (-1 if line[0] == 'L' else 1)
    current_pos = (current_pos + rotation) % 100
    if current_pos == 0:
        zeros += 1

print(zeros)