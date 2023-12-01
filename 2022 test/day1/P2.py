file = open("day2/input.txt", "r")
max=[0, 0, 0]; nombre=0; somme=0
finLutin = False
while True:
    c = file.read(1)
    if c=="":
        break
    if c!="\n":
        finLutin = False
        nombre = 10*nombre + int(c)
    if c=="\n":
        if finLutin == True:
            if somme > max[0] :
                if somme > max[1]:
                    if somme > max[2]:
                        max[0] = max[1]
                        max[1] = max[2]
                        max[2] = somme
                    else:
                        max[0] = max[1]
                        max[1] = somme
                else:
                    max[0] = somme
            somme = 0
        somme+=nombre
        nombre = 0
        finLutin = True
print(max[0]+max[1]+max[2])