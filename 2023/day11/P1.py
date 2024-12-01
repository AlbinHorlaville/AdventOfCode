# Albin Horlaville
# Advent of Code 2023

file = open("2023/day11/input.txt", "r")
map = file.read().split("\n")
output = map.copy()

print("----- Input -----")
print("\n".join(map))

# Expand the universe

# Double rows
for i in range(len(map)):
    if not "#" in map[i]:
        output.insert(i, "."*len(map[i])) # We put a row of '.'

# Double columns
# for j in range(len(map[0])):
#     empty_col = True
#     for i in range(len(map)):
#         if map[i][j]=="#":
#             empty = False
#             break
    
#     if empty_col:
#         for i in range (len(map)):
#             map[i][:j].join("."+map[i][j:]) # We put a '.' each row

print("----- Output -----")
print("\n".join(output))