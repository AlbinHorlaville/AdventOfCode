import numpy
import math

file = open("2023/day8/input.txt", "r")

direction = file.readline()[:-1] # Permet de retirer le dernier caractère de la ligne

etats = file.read().split("\n")

# transformation en tableau
for i in range(len(etats)):
    etats[i] = etats[i].split(" ")

state_dict = dict()
# transformation en dictionnaire d'état
for i in range(len(etats)):
    state_dict[etats[i][0]] = [etats[i][1], etats[i][2]]


# Construction de l'ensemble des états de départ
start_state = []
for i in range(len(etats)):
    if etats[i][0][-1]=="A":
        start_state.append(etats[i][0])

# Construction de l'ensemble des états de départ
end_state = []
for i in range(len(etats)):
    if etats[i][0][-1]=="Z":
        end_state.append(etats[i][0])


steps = numpy.ones(len(start_state), dtype=int)
i=0
current_state = start_state
while True:
    end_reach = True
    for j in range(len(end_state)):
        try:
            current_state.index(end_state[j])
        except:
            end_reach = False
    if end_reach:
        break

    current_direction = direction[i]

    if current_direction=="L":
        for j in range(len(current_state)):
            if current_state[j][-1]!="Z":
                current_state[j] = state_dict[current_state[j]][0]

    if current_direction=="R":
        for j in range(len(current_state)):
            if current_state[j][-1]!="Z":
                current_state[j] = state_dict[current_state[j]][1]

    for j in range(len(steps)):
        if current_state[j][-1]!="Z":
            steps[j]+=1
    i = (i+1)%len(direction)
print(steps)
print(math.lcm(steps[0], steps[1], steps[2], steps[3], steps[4], steps[5]))