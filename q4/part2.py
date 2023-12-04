fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q4/input.txt", "r")
fhread = fh.readlines()

total = 0
d = {}
match = {}

for i in fhread:
    cards = i.split(":")[0]
    card_num = int(cards.split(" ")[-1])
    d[card_num] = 1

    nums = i.split(":")[1]
    numsplit = nums.split("|")
    win_nums = numsplit[0]
    my_nums = numsplit[1]
    all_win = win_nums.split(" ")
    all_my = my_nums.split(" ")

    score = 0
    
    for k in all_my:
        k = k.rstrip("\n")
        if k in all_win and k != "":
            score = score + 1
    match[card_num] = score


for i in d:
    matches = match[i]
    if matches != 0:
        for m in range(d[i]):
                k = i+1
                for j in range(matches):
                    if k in d:
                        d[k] += 1
                        k = k + 1
                    else:
                        break


total = 0

for l in d:
    total += d[l]

print(total)

fh.close()