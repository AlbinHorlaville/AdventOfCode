# On récupère le tableau de caractère du fichier
def getStr(source: str):
    file = open(source, 'r')
    tableau = file.read()
    file.close()
    return tableau

# On récupère le nombre de ligne du fichier
def getNBLines(source: str):
    file = open(source, 'r')
    nbLines = 0
    while True:
        line = file.readline()
        if line=="":
            break
        nbLines+=1
    file.close()
    return nbLines

# On récupère le nombre de colonne du fichier
def getNBRows(source: str):
    file = open(source, 'r')
    nbRows = 0
    while True:
        line = file.read(1)
        if line=="\n":
            break
        nbRows+=1
    file.close()
    return nbRows

def detourerNB(tab, i, j):
    n = charToInt(tab[i*nbRows+j])
    jbis = j-1
    # On récupère les chiffres de gauche
    if (jbis!=0):
        while ('0'<=tab[i*nbRows+jbis] and tab[i*nbRows+jbis]<='9'):
            n = charToInt(tab[i*nbRows+jbis])*10 + n
            jbis-=1
    jbis = j+1
    if (jbis!=nbRows-1):
        while ('0'<=tab[i*nbRows+jbis] and tab[i*nbRows+jbis]<='9'):
            n = n + charToInt(tab[i*nbRows+jbis])*10
            jbis+=1
    return n, jbis==(j+1)

# Analyse le pourtour du nombre pour trouver un symbole différent de "."
def searchMul(tab:str, i:int, j:int):
    # case de gauche
    one = -1
    two = -1
    checkIndex = False
    # case en haut à gauche
    if (i!=0 and j!=0 and '0'<=tab[(i-1)*nbRows+j-1] and tab[(i-1)*nbRows+j-1]<='9'):
        one, checkIndex = detourerNB(tab, i-1, j-1)
    # case en haut
    if (one==-1 and j!=0 and '0'<=tab[(i-1)*nbRows+j] and tab[(i-1)*nbRows+j]<='9'):
        one, checkIndex = detourerNB(tab, i-1, j)
    # case en haut à droite
    if (checkIndex and i!=0 and j!=(nbRows-1) and '0'<=tab[(i-1)*nbRows+j+1] and tab[(i-1)*nbRows+j+1]<='9'):
        if one==-1:
            one, checkIndex = detourerNB(tab, i-1, j+1)
        else:
            two, checkIndex = detourerNB(tab, i-1, j+1)
    # case à gauche
    if (j!=0 and '0'<=tab[i*nbRows+j-1] and tab[i*nbRows+j-1]<='9'):
        if (one!=-1 and two!=-1):
            return 0
        if one==-1:
            one, checkIndex = detourerNB(tab, i, j-1)
        else:
            two, checkIndex = detourerNB(tab, i, j-1)
    # case à droite
    if (j!=(nbRows-1) and '0'<=tab[i*nbRows+j+1] and tab[i*nbRows+j+1]<='9'):
        if (one!=-1 and two!=-1):
            return 0
        if one==-1:
            one, checkIndex = detourerNB(tab, i, j+1)
        else:
            two, checkIndex = detourerNB(tab, i, j+1)
    # case en bas à gauche
    if (i!=(nbLines-1) and j!=0 and '0'<=tab[(i+1)*nbRows+j-1] and tab[(i+1)*nbRows+j-1]<='9'):
        if (one!=-1 and two!=-1):
            return 0
        if one==-1:
            one, checkIndex = detourerNB(tab, i+1, j-1)
        else:
            two, checkIndex = detourerNB(tab, i+1, j-1)
    # case en bas
    if (i!=(nbLines-1) and '0'<=tab[(i+1)*nbRows+j] and tab[(i+1)*nbRows+j]<='9'):
        if (one!=-1 and two!=-1):
            return 0
        if one==-1:
            one, checkIndex = detourerNB(tab, i+1, j)
        else:
            two, checkIndex = detourerNB(tab, i+1, j)
    # case en bas à droite
    if (i!=(nbLines-1) and j!=(nbRows-1) and '0'<=tab[(i+1)*nbRows+j+1] and tab[(i+1)*nbRows+j+1]<='9'):
        if (one!=-1 and two!=-1):
            return 0
        if one==-1:
            one, checkIndex = detourerNB(tab, i+1, j+1)
        else:
            two, checkIndex = detourerNB(tab, i+1, j+1)
    return one*two

def charToInt(src:str):
    return ord(src)-ord('0')

source = "2023/day3/input.txt"
tab = getStr(source)
nbRows = getNBRows(source)
nbLines = getNBLines(source)

newtab = ""
i = 0
while i<len(tab):
    if (tab[i]!="\n"):
        newtab = newtab + tab[i]
    i+=1
tab = newtab

sum=0
indexI_deb = 0
indexI_fin = 0
indexJ_deb = 0
indexJ_fin = 0

inNumber = False
for i in range(nbLines):
    for j in range(nbRows):
        if tab[i*nbRows+j]=="*":
            sum+=searchMul(tab, i, j)
print(sum)