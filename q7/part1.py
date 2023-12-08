fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q7/input.txt", "r")
fhread = fh.readlines()

def clean(lst):
    xs = []
    for i in lst:
        if i != "" and i !="\n":
            i = i.rstrip("\n")
            xs.append(i)
    return xs

fhread = clean(fhread)
lst = []

def five_of_a_kind(s):
    mylist = list(s)
    mylist = list( dict.fromkeys(mylist) )

    if len(mylist) == 1:
        return True 
    else:
        return False

def four_of_a_kind(s):
    mylist = list(s)
    strings = list( dict.fromkeys(mylist) )
    if len(strings) == 2:
        count1 = 0
        for i in s:
            if i == strings[0]:
                count1 += 1
        if count1 == 4 or count1 == 1:
            return True 
        return False
    else:
        return False


    


def full_house(s):
    mylist = list(s)
    mylist = list( dict.fromkeys(mylist) )

    if len(mylist) == 2:
        return True
    else:
        return False
    
def three_of_a_kind(s):
    mylist = list(s)
    strings = list( dict.fromkeys(mylist) )
    count1 = 0
    count2 = 0
    count3 = 0
    for i in s:
        if i == strings[0]:
            count1 += 1
    for i in s:
        if i == strings[1]:
            count2 += 1
    for i in s:
        if i == strings[2]:
            count3 += 1 
    
    if count1 == 3 or count2 == 3 or count3 == 3:
        return True 
    return False

def two_pair(s):
    mylist = list(s)
    mylist = list( dict.fromkeys(mylist) )

    if len(mylist) == 3:
        return True
    else:
        return False
    
def one_pair(s):
    mylist = list(s)
    strings = list( dict.fromkeys(mylist) )

    if len(strings) == 4:
        return True 
    else:
        return False


          

five = []
four = []
full = []
three = []
two = []
one = []
high = []

d = {}

for i in fhread:
    comps = i.split(" ")
    s = comps[0]
    bid = int(comps[1])
    d[s] = bid
    if five_of_a_kind(s):
        five.append(s)
    elif four_of_a_kind(s):
        four.append(s)
    elif full_house(s):
        full.append(s)
    elif three_of_a_kind(s):
        three.append(s)
    elif two_pair(s):
        two.append(s)
    elif one_pair(s):
        one.append(s)
    else:
        high.append(s)

print(high)
print(one)
print(two)
print(three)
print(full)
print(four)
print(five)

strength = {"A": 13, "K": 12, "Q":11,"J":10,"T":9,"9":8,"8":7,"7":6,"6":5,"5":4,"4":3,"3":2,"2":1}
def sortlst(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            for k in range(5):
                alph1 = lst[j][k]
                alph2 = lst[j+1][k]
                if strength[alph1] != strength[alph2]:
                    if strength[alph1] > strength[alph2]:
                        lst[j], lst[j+1] = lst[j+1], lst[j]
                    break 
    return lst



highf = sortlst(high)
onef = sortlst(one)
twof = sortlst(two)
threef = sortlst(three)
fullf = sortlst(full)
fourf = sortlst(four)
fivef = sortlst(five)

final = []
final.extend(highf)
final.extend(onef)
final.extend(twof)
final.extend(threef)
final.extend(fullf)
final.extend(fourf)
final.extend(fivef)


sums = 0
for i in range(len(final)):
    hand = final[i]
    rank = i + 1
    bid = d[hand]
    prod = rank * bid
    sums += prod

print(sums)

fh.close()