import numpy

file = open("2023/day9/input.txt", "r")

histories = file.read().split("\n")

for i in range(len(histories)):
    histories[i] = histories[i].split(" ")

# fonction récursive
def histo(tab):
    tab_1 = []
    for i in range(len(tab)-1):
        tab_1.append(int(tab[i+1]) - int(tab[i]))
    return rec_histo(tab, tab_1)
# tab_n est le niveau n de la pyramide (au dessus)
# tab_n_1 est le niveau n-1 de la pyramide (en dessous)
def rec_histo(tab_n, tab_n_1):
    zero=True
    for i in range(len(tab_n_1)):
        if int(tab_n_1[i])!=0:
            zero=False
    if zero:
        tab_n.insert(0, int(tab_n[0]) - int(tab_n_1[0]))
        return tab_n
    tab_n_2 = []
    for i in range(len(tab_n_1)-1):
        tab_n_2.append(int(tab_n_1[i+1]) - int(tab_n_1[i]))
    tab_n_1 = rec_histo(tab_n_1, tab_n_2)
    tab_n.insert(0, int(tab_n[0]) - int(tab_n_1[0]))
    return tab_n

sum=0
for i in range(len(histories)):
    current = histo(histories[i])
    sum+=current[0]
print(sum)