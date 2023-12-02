file = open("2023/day2/input.txt", 'r')
sum = 0
while (True):
    line = file.readline()
    if (line == ""):
        break
    lengthLine = len(line)-1 # Du fait du caractère de retour à la ligne
    errorItem = ""
    print(lengthLine//2)
    for i in range(lengthLine//2):
        for j in range(lengthLine//2):
            if (line[i] == line[lengthLine//2+j]):
                errorItem = line[i]
    if (errorItem==""):
        print("Error parsing")
    if ('a'<=errorItem and errorItem<='z'):
        priority = ord(errorItem) - ord('a') + 1
    elif ('A'<=errorItem and errorItem<='Z'):
        priority = ord(errorItem) - ord('A') + 27
    else:
        print("Error parsing")
        priority = 0
    print(errorItem, priority)
    sum+=priority
print(sum)