file = open("2023/day1/input.txt", "r")
sum = 0
while True:
    c = file.readline()
    if (c==""):
        break
    firstDigit = -1
    lastDigit = -1
    for i in range(len(c)):
        if ('0'<=c[i] and c[i]<='9'):  
            lastDigit = int(c[i])
        if (firstDigit==-1):
                firstDigit = lastDigit
    sum += firstDigit*10 + lastDigit
print(sum)