fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q8/input.txt", "r")
fhread = fh.readlines()

fh.close()

def clean(lst):
    xs = []
    for i in lst:
        if i != "" and i !="\n":
            i = i.rstrip("\n")
            xs.append(i)
    return xs

instructions = fhread[0].rstrip("\n")
nodes = clean(fhread[1:])
node_dict = {}
start = []


for i in nodes:
    comp = i.split(" = ")
    maps = comp[1].strip("()")
    maps = maps.split(", ")
    node_dict[comp[0]] = (maps[0], maps[1])
    if comp[0][-1] == "A":
        start.append(comp[0])

steps = []
print(start)

def check():
    for k in start:
        if k[-1] != "Z":
            return False
    return True

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for alph in start:
    temp = 0
    while alph[-1] != "Z":
        for i in instructions:
            if alph[-1] != "Z":
                if i == "L":
                    alph = node_dict[alph][0]
                else:
                    alph = node_dict[alph][1]
                temp += 1
            else:
                break
    steps.append(temp)

from math import gcd

lcm = 1
for i in steps:
    lcm = lcm*i//gcd(lcm, i) # lcm = product / gcd
print(lcm)



