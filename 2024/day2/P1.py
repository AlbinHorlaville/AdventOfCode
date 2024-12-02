file = open("2024/day2/input.txt", "r")
reports = file.read().splitlines()

safe = 0

def isDecreasing(liste: list):
    for i in range(len(liste) - 1):
        if not (liste[i] > liste[i+1] and liste[i] - liste[i+1] <= 3):
            return False
    return True

def isIncreasing(liste: list):
    for i in range(len(liste) - 1):
        if not (liste[i] < liste[i+1] and liste[i+1] - liste[i] <= 3):
            return False
    return True


# On forme les deux listes
for report in reports:
    # On range les levels
    levels = report.split(" ")
    for i in range(len(levels)):
        levels[i] = int(levels[i])

    # Sont ils croissants ou décroissants ?
    if isIncreasing(levels) or isDecreasing(levels):
        safe += 1

print(safe)
