import re

fh = open("Users/lavanya/Documents/GitHub/advent_of_code/q2/input.txt", "r")
fhread = fh.readlines()

sums = 0

for i in fhread:

    blues = re.findall("^\d blue$", i)
    print(blues)


#fh.close()
