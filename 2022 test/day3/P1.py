file = open("input.txt", 'r')

sum = 0

while (True):
    line = file.readline()
    print(line)
    lenghtLine = len(line)

    for i in range(int((lenghtLine-1)/2)):
        for j in range(int((lenghtLine-1)/2), lenghtLine-1):
            print(i,j)
            if (line[i]==line[j]):
                print("fin")
                break