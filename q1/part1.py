import re

fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q1/input.txt", "r")
fhread = fh.readlines()

sum = 0

for i in fhread:
    nums = re.findall("\d", i)
    number = int(nums[0])*10 + int(nums[-1])
    sum = sum + number

print(sum)

fh.close()