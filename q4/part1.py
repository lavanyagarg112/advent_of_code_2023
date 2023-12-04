fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q4/input.txt", "r")
fhread = fh.readlines()

total = 0

for i in fhread:
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
            if score == 0:
                score = 1
            else:
                score *= 2
    total += score

print(total)

fh.close()