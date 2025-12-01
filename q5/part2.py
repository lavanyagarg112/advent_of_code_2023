# too long to run

'''
New idea:

Reverse Map
Start from location = 0 and keep going

tbh can start from bigger number but why take the risk

check if there is a reverse mapping to the seed number
check for all
as soon as one hits the seed number
thats the smallest location
'''

fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q5/input.txt", "r")
fhread = fh.readlines()

def clean_to_int(lst):
    xs = []
    for i in lst:
        if i != "" and i !="\n":
            i = i.rstrip("\n")
            xs.append(int(i))
    return xs

def clean(lst):
    xs = []
    for i in lst:
        if i != "" and i !="\n":
            i = i.rstrip("\n")
            xs.append(i)
    return xs
        
        
init_lst = clean_to_int((fhread[0].split(":")[1]).split(" "))
seeds = []
s = 0
while s < (len(init_lst) - 1):
    t = (init_lst[s], init_lst[s+1]+init_lst[s])
    s = s + 2
    seeds.append(t)


superlst = []


i = 0
while i < len(fhread):
    j = i + 1
    if "-" in fhread[i]:
        xs = []
        while j<len(fhread) and "-" not in fhread[j]:
            xs.append(fhread[j])
            j = j + 1
        superlst.append(xs)
    i = j

new_superlst = []
for k in superlst:
    k = clean(k)
    new_superlst.append(k)


def maps(lst):
    d = {}
    for i in lst:
        nums = i.split(" ")
        dest = int(nums[0])
        source = int(nums[1])
        rnge = int(nums[2])
        tup = (dest, dest+rnge)
        d[tup] = source  
    return d



fromsoils = maps(new_superlst[0])
fromfertilizers = maps(new_superlst[1])
fromwater = maps(new_superlst[2])
fromlight = maps(new_superlst[3])
fromtemperature = maps(new_superlst[4])
fromhumidity = maps(new_superlst[5])
fromlocation = maps(new_superlst[6])

min_location = "start"

def get_value(d, elem):
    final = 0
    for j in d:
        if elem >= j[0] and elem <= j[1]:
            start = j[0]
            length = elem - start
            final = d[j] + length
            break
    else:
        final = elem

    return final

def check_seed(s):
    for i in seeds:
        if s >= i[0] and s <= i[1]:
            return True 
    else:
        return False


loc = 108000000 # assumed this number for faster runtime, cause i already knew the answer
while True:
    humidity = get_value(fromlocation, loc)
    temperature = get_value(fromhumidity, humidity)
    light = get_value(fromtemperature, temperature)
    water = get_value(fromlight, light)
    fertilizers = get_value(fromwater, water)
    soils = get_value(fromfertilizers, fertilizers)
    seed = get_value(fromsoils, soils)

    if check_seed(seed):
        print(loc)
        break 
    else:
        loc += 1


fh.close()