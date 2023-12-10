
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

steps=0
i=0
start_state = "AAA"
end_state = "ZZZ"
current_state = start_state
while True:
    if current_state==end_state:
        break
    current_direction = direction[i]
    if current_direction=="L":
        current_state = state_dict[current_state][0]
    if current_direction=="R":
        current_state = state_dict[current_state][1]

    steps+=1
    i = (i+1)%len(direction)
print(steps)