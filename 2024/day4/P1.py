file = open("2024/day4/input.txt", "r")

wordSearch = file.readlines()
result = 0

def countXMAS(wordSearch, i, j):
    somme = 0
    # Croix
    if j < len(wordSearch[i]) - 3 and wordSearch[i][j] == 'X' and wordSearch[i][j+1] == 'M' and wordSearch[i][j+2] == 'A' and wordSearch[i][j+3] == 'S':
        somme +=1
    if j >= 3 and wordSearch[i][j] == 'X' and wordSearch[i][j-1] == 'M' and wordSearch[i][j-2] == 'A' and wordSearch[i][j-3] == 'S':
        somme +=1
    if i < len(wordSearch) - 3 and wordSearch[i][j] == 'X' and wordSearch[i+1][j] == 'M' and wordSearch[i+2][j] == 'A' and wordSearch[i+3][j] == 'S':
        somme +=1
    if i >= 3 and wordSearch[i][j] == 'X' and wordSearch[i-1][j] == 'M' and wordSearch[i-2][j] == 'A' and wordSearch[i-3][j] == 'S':
        somme +=1
    # Diagonales
    if j < len(wordSearch[i]) - 3 and i < len(wordSearch) - 3 and wordSearch[i][j] == 'X' and wordSearch[i+1][j+1] == 'M' and wordSearch[i+2][j+2] == 'A' and wordSearch[i+3][j+3] == 'S':
        somme +=1
    if j >= 3 and i >= 3 and wordSearch[i][j] == 'X' and wordSearch[i-1][j-1] == 'M' and wordSearch[i-2][j-2] == 'A' and wordSearch[i-3][j-3] == 'S':
        somme +=1
    if i < len(wordSearch) - 3 and j >= 3 and wordSearch[i][j] == 'X' and wordSearch[i+1][j-1] == 'M' and wordSearch[i+2][j-2] == 'A' and wordSearch[i+3][j-3] == 'S':
        somme +=1
    if i >= 3 and j < len(wordSearch[i]) - 3 and wordSearch[i][j] == 'X' and wordSearch[i-1][j+1] == 'M' and wordSearch[i-2][j+2] == 'A' and wordSearch[i-3][j+3] == 'S':
        somme +=1
    return somme

for i in range(len(wordSearch)):
    for j in range(len(wordSearch[i])):
        if wordSearch[i][j] == 'X':
            result += countXMAS(wordSearch, i, j)

print(result)
