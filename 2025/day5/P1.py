file = open("input.txt", "r")
lines = file.read().splitlines()


def merge_range(s1, e1, s2, e2):
    return (min(s1, s2), max(e1, e2))

# ------------- Merge ranges -------------
i = 0
ranges = []
while (lines[i]!=''): # merge ranges
    start = int(lines[i].split('-')[0])
    end = int(lines[i].split('-')[1])
    
    inserted = False
    j = 0
    while j < len(ranges):
        s, e = ranges[j]
        if end < s:
            ranges.insert(j, (start, end))
            inserted = True
            break
        elif start < s and s <= end <= e:
            ranges[j] = (start, e)
            if j > 0: # Essayer de merge avant la range précédente
                s_pre, e_pre = ranges[j-1]
                if e_pre >= start:
                    ranges[j] = merge_range(s_pre, e_pre, start, e)
            inserted = True
            break
        elif s <= start and end <= e:
            # Ne rien insérer
            inserted = True
            break
        elif s <= start <= e and e < end:
            # Nouvelle range = (s, end)
            ranges[j] = (s, end)
            if j < len(ranges)-1:
                s_next, e_next = ranges[j+1]
                if end >= s_next: # Essayer de merge avec la range d'après
                    ranges[j] = merge_range(s, end, s_next, e_next)
                    ranges.remove(ranges[j+1])
            inserted = True
            break
        # Cas e < start : on comparera la range avec celle d'après. Si on est au bout du tableau, on ajoute à la fin du tableau (s, e)
        j+=1
    
    if not inserted:
        # Append range (start, end)
        ranges.append((start, end))
    i+=1
i+=1
print(ranges)

# ------------- Compare IDs to ranges -------------
result = 0
while i < len(lines):
    value = int(lines[i])
    for start, end in ranges:
        if start <= value <= end:
            result+=1
            print(value)
            break
    i+=1

print(result)