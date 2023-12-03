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

# Analyse le pourtour du nombre pour trouver un symbole différent de "."
def IsASymbol(tab:str, indexI_deb:int, indexJ_deb:int, indexI_fin:int, indexJ_fin:int, number:int):
    # case de gauche
    if (indexJ_deb!=0 and tab[indexI_deb*nbRows+indexJ_deb-1]!="." and not('0'<=tab[indexI_deb*nbRows+indexJ_deb-1] and tab[indexI_deb*nbRows+indexJ_deb-1]<='9')):
        return number
    for k in range(indexJ_fin-indexJ_deb+1):
        # ligne du dessus
        if (indexI_deb!=0 and tab[(indexI_deb-1)*nbRows+indexJ_deb+k]!="." and not('0'<=tab[(indexI_deb-1)*nbRows+indexJ_deb+k] and tab[(indexI_deb-1)*nbRows+indexJ_deb+k]<='9')):
            return number
        # ligne du dessous
        if (indexI_fin!=(nbLines-1) and tab[(indexI_deb+1)*nbRows+indexJ_deb+k]!="." and not('0'<=tab[(indexI_deb+1)*nbRows+indexJ_deb+k] and tab[(indexI_deb+1)*nbRows+indexJ_deb+k]<='9')):
            return number
    # case de droite
    if (indexJ_fin!=(nbRows-1) and tab[indexI_deb*nbRows+indexJ_fin+1]!="." and not('0'<=tab[indexI_deb*nbRows+indexJ_fin+1] and tab[indexI_deb*nbRows+indexJ_fin+1]<='9')):
        return number
    # case en haut à gauche
    if (indexJ_deb!=0 and indexI_deb!=0 and tab[(indexI_deb-1)*nbRows+indexJ_deb-1]!="." and not('0'<=tab[(indexI_deb-1)*nbRows+indexJ_deb-1] and tab[(indexI_deb-1)*nbRows+indexJ_deb-1]<='9')):
        return number
    # case en haut à droite
    if (indexJ_deb!=(nbRows-1) and indexI_deb!=0 and tab[(indexI_deb-1)*nbRows+indexJ_fin+1]!="." and not('0'<=tab[(indexI_deb-1)*nbRows+indexJ_fin+1] and tab[(indexI_deb-1)*nbRows+indexJ_fin+1]<='9')):
        return number
    # case en bas à gauche
    if (indexJ_deb!=0 and indexI_deb!=(nbLines-1) and tab[(indexI_deb+1)*nbRows+indexJ_deb-1]!="." and not('0'<=tab[(indexI_deb+1)*nbRows+indexJ_deb-1] and tab[(indexI_deb+1)*nbRows+indexJ_deb-1]<='9')):
        return number
    # case en bas à droite
    if (indexJ_deb!=(nbRows-1) and indexI_deb!=(nbLines-1) and tab[(indexI_deb+1)*nbRows+indexJ_fin+1]!="." and not('0'<=tab[(indexI_deb+1)*nbRows+indexJ_fin+1] and tab[(indexI_deb+1)*nbRows+indexJ_fin+1]<='9')):
        return number
    return 0

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


# Flag pour savoir si on est en train de lire un nombre ou pas
inNumber = False
for i in range(nbLines):
    for j in range(nbRows):
        # Si on est en train de lire un nombre, alors on continue
        if inNumber:
            if '0'<=tab[i*nbRows+j] and tab[i*nbRows+j]<='9':
                inNumber = True
                number = number*10+charToInt(tab[i*nbRows+j])
                indexI_fin = i
                indexJ_fin = j
            else:
                inNumber = False
                number = IsASymbol(tab, indexI_deb, indexJ_deb, indexI_fin, indexJ_fin, number)
                sum+=number
        # On note le premier chiffre que l'on trouve, ainsi que ses indexs
        if not inNumber and '0'<=tab[i*nbRows+j] and tab[i*nbRows+j]<='9':
            inNumber = True
            number = charToInt(tab[i*nbRows+j])
            indexI_deb = i
            indexJ_deb = j
            indexI_fin = i
            indexJ_fin = j
print(sum)