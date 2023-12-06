import time
import math
Time = 44707080
Dist = 283113411341491

deb = time.time()
# Version 1
n = 0
d = int(math.sqrt(Time))
for t in range(d, Time):
    if t*(Time-t)>Dist:
        n+=1
fin = time.time()
print("Temps Version 1 : ",fin-deb)
print("Résultat Version 1 : ", n)

# Version 2 avec Polynôme
# -x2 + Time*x - Dist
# delta = b2 - 4ac = Time2 - 4*Dist
# r1 = (-b - sqrt(Time2 - 4*Dist)) / 2a
# r2 = (-b + sqrt(Time2 - 4*Dist)) / 2a
deb = time.time()
r1 = int((Time + math.sqrt(Time*Time - 4*Dist))/2)
r2 = int((- Time + math.sqrt(Time*Time - 4*Dist))/(-2))
n = r1-r2
fin = time.time()
print("Temps Version 2 : ",fin-deb)
print("Résultat Version 2 : ", n)
