file = open("input.txt", 'r')
sum = 0
while (True):
    elf_1 = file.readline()
    if (elf_1 == ""):
        break
    elf_2 = file.readline()
    elf_3 = file.readline()

    badge = ""

    len_elf_1 = len(elf_1)-1
    len_elf_2 = len(elf_2)-1
    len_elf_3 = len(elf_3)-1

    priority = -1

    for i in range(len_elf_1):
        for j in range(len_elf_2):
            for k in range(len_elf_3):
                

    print(badge, priority)
    sum+=priority
print(sum)