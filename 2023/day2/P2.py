file = open("input.txt", "r")
sum = 0

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

while True:
    # Reader
    game_n = file.readline()
    if (game_n==""):
        break

    # On récupère le game ID
    game_id = int(game_n[5])
    i = 6
    if (game_n[6]!=":"):
        game_id = game_id*10+int(game_n[6])
        i = 7
        if (game_n[7]!=":"):
            game_id = game_id*10+int(game_n[7])
            i = 8

    max_red = 0
    max_green = 0
    max_blue = 0
    
    while game_n[i]!="\n":
        i+=2
        k = 0 # Incrémentation de i changeant en fonction de ce qu'on a parsé
        current_n = 0
        # Lecture du nombre
        if ('0'<=game_n[i] and game_n[i]<='9'):
            current_n = ord(game_n[i])-ord('0')
            if ('0'<=game_n[i+1] and game_n[i+1]<='9'):
                current_n = current_n*10+ord(game_n[i+1])-ord('0')
                k+=1
        k+=2
        match (game_n[i+k]):
            case 'r':
                if current_n > max_red:
                    max_red = current_n
                k+=3
            case 'g':
                if current_n > max_green:
                    max_green = current_n
                k+=5
            case 'b':
                if current_n > max_blue:
                    max_blue = current_n
                k+=4
        i+=k
    sum+=max_red*max_green*max_blue
print(sum)