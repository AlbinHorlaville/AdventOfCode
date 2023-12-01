file = open("input.txt", "r")
sum = 0
while True:
    c = file.readline()
    if (c==""):
        break
    firstDigit = -1
    lastDigit = -1
    wordNumber = ""
    for i in range(len(c)):
        if ('0'<=c[i] and c[i]<='9'):
            lastDigit = int(c[i])
            wordNumber = ""
        elif (wordNumber == "o" and c[i]=="n"):
            wordNumber = "on"
        elif (wordNumber == "on" and c[i]=="e"):
            lastDigit = 1
            wordNumber = "e"
        elif (wordNumber=="t" and c[i] == "w"):
            wordNumber = "tw"
        elif (wordNumber=="tw" and c[i] == "o"):
            lastDigit=2
            wordNumber = "o"
        elif (wordNumber=="t" and c[i] == "h"):
            wordNumber = "th"
        elif (wordNumber=="th" and c[i] == "r"):
            wordNumber = "thr"
        elif (wordNumber=="thr" and c[i] == "e"):
            wordNumber = "thre"
        elif (wordNumber=="thre" and c[i] == "e"):
            lastDigit = 3
            wordNumber = "e"
        elif (wordNumber=="f" and c[i] == "o"):
            wordNumber = "fo"
        elif (wordNumber=="fo" and c[i] == "u"):
            wordNumber = "fou"
        elif (wordNumber=="fou" and c[i] == "r"):
            lastDigit = 4
            wordNumber = "r"
        elif (wordNumber=="f" and c[i] == "i"):
            wordNumber = "fi"
        elif (wordNumber=="fi" and c[i] == "v"):
            wordNumber = "fiv"
        elif (wordNumber=="fiv" and c[i] == "e"):
            lastDigit = 5
            wordNumber = "e"
        elif (wordNumber=="s" and c[i] == "i"):
            wordNumber = "si"
        elif (wordNumber=="si" and c[i] == "x"):
            lastDigit = 6
            wordNumber = "x"
        elif (wordNumber=="s" and c[i] == "e"):
            wordNumber = "se"
        elif (wordNumber=="se" and c[i] == "v"):
            wordNumber = "sev"
        elif (wordNumber=="sev" and c[i] == "e"):
            wordNumber = "seve"
        elif (wordNumber=="seve" and c[i] == "n"):
            lastDigit = 7
            wordNumber = "n"
        elif (c[i] == "i" and (wordNumber=="e" or wordNumber=="thre")):
            wordNumber = "ei"
        elif (wordNumber=="ei" and c[i] == "g"):
            wordNumber = "eig"
        elif (wordNumber=="eig" and c[i] == "h"):
            wordNumber = "eigh"
        elif (wordNumber=="eigh" and c[i] == "t"):
            lastDigit = 8
            wordNumber = "t"
        elif (wordNumber=="n" or wordNumber=="on" and c[i] == "i"):
            wordNumber = "ni"
        elif (wordNumber=="ni" and c[i] == "n"):
            wordNumber = "nin"
        elif (wordNumber=="nin" and c[i] == "e"):
            lastDigit = 9
            wordNumber = "e"
        # Début des nombres
        elif (c[i] == "o"):
            wordNumber = "o"
        elif (c[i] == "t"):
            wordNumber = "t"
        elif (c[i] == "f"):
            wordNumber = "f"
        elif (c[i] == "s"):
            wordNumber = "s"
        elif ( c[i] == "e"):
            wordNumber = "e"
        elif(c[i] == "n"):
            wordNumber = "n"
        else:
            wordNumber = ""
        # firstDigit prend la valeur de lastDigit la première fois que lastDigit prend une valeur
        if (firstDigit==-1):
                firstDigit = lastDigit
    if (firstDigit==lastDigit & firstDigit==-1):
        firstDigit = 0
        lastDigit = 0
    sum += firstDigit*10 + lastDigit
print(sum)