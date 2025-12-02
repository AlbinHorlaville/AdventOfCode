file = open("input.txt", "r")
lines = file.read().splitlines()
ranges = lines[0].split(",")

result = 0

def is_valid_ID(word:str) -> bool:
    for i in range(1, len(word)//2+1): # Nombre de digit dans la séquence (max la moitié de la taille du mot)
        if len(word) % i != 0: continue
        k = 1
        while i*(k+1) <= len(word) and word[:i] == word[i*k:i*(k+1)]: # Comparaison de la première séquence avec toutes celles d'après
            k+=1
        if i*(k+1) > len(word): # L'ID est valide, la séquence se répète jusqu'à la fin
            return True
    return False

for sequence in ranges:
    sequence = sequence.split("-")
    start = int(sequence[0])
    end = int(sequence[1])
    for number in range(start, end+1): # Il faut check end aussi donc +1
        word = str(number)
        if is_valid_ID(word):
            result += number

print(result)
