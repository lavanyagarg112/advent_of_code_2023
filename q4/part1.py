fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q4/input.txt", "r")
fhread = fh.readlines()

print(fhread)

for i in fhread:
    nums = i.split(":")[1]
    numsplit = nums.split("|")
    win_nums = numsplit[0]
    my_nums = numsplit[1]
    print(win_nums)

fh.close()