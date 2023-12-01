file = open("day1/input.txt", "r")
max=0; nombre=0; somme=0
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
            if somme > max :
                max = somme
            somme = 0
        somme+=nombre
        nombre = 0
        finLutin = True
print(max)