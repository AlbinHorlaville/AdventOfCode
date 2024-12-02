file = open("2024/day2/input.txt", "r")
reports = file.read().splitlines()

safe = 0

def isDecreasing(liste: list, secondChancePassed: bool):
    for i in range(len(liste) - 1):
        if not (liste[i] > liste[i+1] and liste[i] - liste[i+1] <= 3):
            if not secondChancePassed:
                second_chance_A = liste.copy()
                second_chance_A.pop(i)
                second_chance_B = liste.copy()
                second_chance_B.pop(i + 1)
                return isDecreasing(second_chance_A, True) or isDecreasing(second_chance_B, True)
            return False
    return True

def isIncreasing(liste: list, secondChancePassed: bool):
    for i in range(len(liste) - 1):
        if not (liste[i] < liste[i+1] and liste[i+1] - liste[i] <= 3):
            if not secondChancePassed:
                second_chance_A = liste.copy()
                second_chance_A.pop(i)
                second_chance_B = liste.copy()
                second_chance_B.pop(i + 1)
                return isIncreasing(second_chance_A, True) or isIncreasing(second_chance_B, True)
            return False
    return True


# On forme les deux listes
for report in reports:
    # On range les levels
    levels = report.split(" ")
    for i in range(len(levels)):
        levels[i] = int(levels[i])

    # Sont ils croissants ou décroissants ?
    if isIncreasing(levels, False) or isDecreasing(levels, False):
        safe += 1

print(safe)
