tabTime = [44, 70, 70, 80]
tabDist = [283, 1134, 1134, 1491]

# a b a*b
res = 1
for c in range(len(tabTime)):
    n = 0
    for t in range(tabTime[c]):
        if t*(tabTime[c]-t)>tabDist[c]:
            n+=1
    res*=n
print(res)