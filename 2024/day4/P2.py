file = open("2024/day4/input.txt", "r")

wordSearch = file.readlines()
result = 0

def countChar(wordSearch, i, j, char):
    count = 0
    if wordSearch[i-1][j-1] == char:
        count +=1
    if wordSearch[i-1][j+1] == char:
        count +=1
    if wordSearch[i+1][j-1] == char:
        count +=1
    if wordSearch[i+1][j+1] == char:
        count +=1
    return count

def countXMAS(wordSearch, i, j):
    Mcount = countChar(wordSearch, i, j, 'M')
    Scount = countChar(wordSearch, i, j, 'S')
    
    if Mcount == 2 and Scount == 2 and wordSearch[i-1][j-1] != wordSearch[i+1][j+1]:
        return 1
    else:
        return 0

for i in range(len(wordSearch)):
    for j in range(len(wordSearch[i])):
        if i > 0 and i < len(wordSearch)-1 and j > 0 and j < len(wordSearch) - 1 and wordSearch[i][j] == 'A':
            result += countXMAS(wordSearch, i, j)

print(result)
