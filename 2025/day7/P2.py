file = open("input.txt", "r")
map = file.read().splitlines()

paths = {}
for line in map:
    for i, c in enumerate(line):
        match c:
            case 'S':
                paths[i] = 1
            case '^':
                if i in paths:
                    paths[i-1] = paths[i] + (paths[i-1] if i-1 in paths else 0)
                    paths[i+1] = paths[i] + (paths[i+1] if i+1 in paths else 0)
                    del paths[i]

result = 0
for value in paths.values():
    result += value

print(paths)
print(result)

# 889669052663471202040 trop haut