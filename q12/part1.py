fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q12/input.txt", "r")
fhread = fh.readlines()

fh.close()

# not done

sums = 0

for i in fhread:
    splits = i.split(" ")
    symbols = splits[0]
    nums = splits[1].rstrip("\n")

    print(symbols)
    print(nums)

