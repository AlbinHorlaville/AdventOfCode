file = open("input.txt", "r")
grid = file.read().splitlines()

def can_be_accessed(grid, x, y) -> bool:
    rolls_around = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i==x and j==y) or i<0 or j<0 or i>=len(grid) or j>=len(grid[i]):
                continue
            if grid[i][j]=='@':
                rolls_around+=1
    return rolls_around < 4

rolls_accessibles = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        # Check if roll is accessible
        if grid[i][j] == '@' and can_be_accessed(grid, i, j):
            rolls_accessibles+=1

print(rolls_accessibles)