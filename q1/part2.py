import re

fh = open("/Users/lavanya/Documents/GitHub/advent_of_code/q1/input.txt", "r")
fhread = fh.readlines()
sums = 0

words = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
digits = ["1","2","3","4","5","6","7","8","9","0"]


for i in fhread:
    nums = []

    '''
    Have to consider that in "sevenine" - it is taken as seven and nine
    rolling window
    '''

    for j in range(len(i)):
        lst = re.findall('one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9', i[j:])
        if len(lst)>0:
            nums.append(lst[0])


    dig1 = nums[0]
    if dig1 in words:
        dig1 = words[dig1]
    dig1 = int(dig1)
    
    dig2 = nums[-1]
    if dig2 in words:
        dig2 = words[dig2]
    dig2 = int(dig2)

    number = dig1*10 + dig2
    sums = sums + number

print(sums)


