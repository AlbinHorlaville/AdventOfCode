file = open("day2/input.txt", 'r')
score = 0
while True:
    c = file.read(4)
    if len(c)==0:
        break
    lutinPlay = c[0]
    myPlay = c[2]
    # Lutin : 
    #   A for Rock      
    #   B for Paper     
    #   C for Scissors  
    #
    # Me :
    #   X for Rock      1 p
    #   Y for Paper     2 p
    #   Z for Scissors  3 p
    match lutinPlay:
        case 'A':
            match myPlay:
                case 'X':
                    score += 1 + 3
                case 'Y':
                    score += 2 + 6
                case 'Z':
                    score += 3 + 0
                case _:
                    print("ERREUR parsing myPlay")
        case 'B':
            match myPlay:
                case 'X':
                    score += 1 + 0
                case 'Y':
                    score += 2 + 3
                case 'Z':
                    score += 3 + 6
                case _:
                    print("ERREUR parsing myPlay")
        case 'C':
            match myPlay:
                case 'X':
                    score += 1 + 6
                case 'Y':
                    score += 2 + 0
                case 'Z':
                    score += 3 + 3
                case _:
                    print("ERREUR parsing myPlay")
        case _:
            print("ERREUR parsing lutinPlay")
print(score)