file = open("input.txt", "r")
lines = file.read().splitlines()
ranges = lines[0].split(",")

result = 0

for sequence in ranges:
    sequence = sequence.split("-")
    start = int(sequence[0])
    end = int(sequence[1])
    for i in range(start, end+1): # Il faut check end aussi donc +1
        word = str(i)
        first_part = word[:len(word)//2]
        last_part = word[len(word)//2:]
        if first_part == last_part:
            result += i

print(result)
