
'''
Correct Answer:
248256639

My code gives:
248378758
'''

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
    if ("J" in mylist and len(mylist) == 2) or (len(mylist) == 1):
        return True 
    else:
        return False

def four_of_a_kind(s):
    mylist = list(s)
    strings = list( dict.fromkeys(mylist) )
    if ("J" in mylist and len(strings) == 3) or len(strings) == 2:
        count1 = 0
        count2 = 0
        count3 = 0
        for i in s:
            if i == strings[0] or i == "J":
                count1 += 1
        for i in s:
            if i == strings[1] or i == "J":
                count2 += 1
        if len(strings) == 3:
            for i in s:
                if i == strings[2] or i == "J":
                    count3 += 1
        if count1 == 4 or count2 == 4 or count3 == 4:
            return True
        else:
            return False
    else:
        return False

def full_house(s): # can give true for four of a kind but comes here only if that fails
    mylist = list(s)
    mylist = list( dict.fromkeys(mylist) )

    if ("J" in mylist and len(mylist) == 3) or len(mylist) == 2:
        return True
    else:
        return False
    
def three_of_a_kind(s): # can give true for a full house as well but i check for full house first, and come here only if that fails
    mylist = list(s)
    strings = list( dict.fromkeys(mylist) )
    count1 = 0
    count2 = 0
    count3 = 0
    for i in s:
        if i == strings[0] or i == "J":
            count1 += 1
    for i in s:
        if i == strings[1] or i == "J":
            count2 += 1
    for i in s:
        if i == strings[2] or i =="J":
            count3 += 1 
    
    if count1 == 3 or count2 == 3 or count3 == 3:
        return True 
    return False

def two_pair(s): # can give true for three of a kind but comes here only after that fails
    mylist = list(s)
    mylist = list( dict.fromkeys(mylist) )

    if (len(mylist) == 3) or ("J" in mylist and len(mylist) == 4):
        return True
    else:
        return False
    
def one_pair(s): # can give true for two pair but comes here only after that fails
    mylist = list(s)
    strings = list( dict.fromkeys(mylist) )

    if (len(strings) == 4) or ("J" in mylist and len(strings) == 5):
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


strength = {"A": 13, "K": 12, "Q":11,"J":0,"T":9,"9":8,"8":7,"7":6,"6":5,"5":4,"4":3,"3":2,"2":1} # J made weakest
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

final = highf + onef + twof + threef + fullf + fourf + fivef

sums = 0
for i in range(len(final)):
    hand = final[i]
    rank = i + 1
    bid = d[hand]
    prod = rank * bid
    sums += prod

print(sums)


fh.close()