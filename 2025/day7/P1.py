file = open("input.txt", "r")
map = file.read().splitlines()

# Récurssif
def go_beam_rec(x:int, y:int):
    if not (0 <= x < len(map)) or not (0 <= y < len(map[0])) or map[x][y] != '.':
        return 0
    while 0<=x<len(map) and not map[x][y] in ('X', '^'):
        map[x] = map[x][:y] + '|' + map[x][y+1:]
        x+=1
    if 0<=x<len(map) and map[x][y] == '^':
        map[x] = map[x][:y] + 'X' + map[x][y+1:]
        return go_beam_rec(x, y-1) + 1 + go_beam_rec(x, y+1)
    return 0


# Find S
y = 0
while map[0][y] != 'S':
    y+=1
result = go_beam_rec(1, y)

for line in map:
    print(line)
print(result)
