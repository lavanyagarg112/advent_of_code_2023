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


soil_lst = new_superlst[0]
ferti_lst = new_superlst[1]
water_lst = new_superlst[2]
light_lst = new_superlst[3]
temp_lst = new_superlst[4]
humid_lst = new_superlst[5]
loc_lst = new_superlst[6]

def maps(lst):
    d = {}
    for i in lst:
        nums = i.split(" ")
        dest = int(nums[0])
        source = int(nums[1])
        rnge = int(nums[2])
        tup = (source, source+rnge)
        d[tup] = dest  
    return d



tosoils = maps(soil_lst)
tofertilisers = maps(ferti_lst)
towater = maps(water_lst)
tolight = maps(light_lst)
totemperature = maps(temp_lst)
tohumidity = maps(humid_lst)
tolocation = maps(loc_lst)

all_locations = []

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

def search_min(d, tup):
    final = 0
    start = tup[0]
    end = tup[1]
    if start == end:
        return start
    for j in d:
        if start >= j[0] and start <= j[1]:
            final = d[j] + start - j[0]
            if end <= j[1]:
                return final
            else:
                new_start = j[1] + 1
            break 
    else:
        new_start = start + 1

    new_min = search_min(d, (new_start, end))
    return min(start, new_min)
    




for i in seeds:
    soil = search_min(tosoils, i)
    fertiliser = get_value(tofertilisers, soil)
    water = get_value(towater, fertiliser)
    light = get_value(tolight, water)
    temp = get_value(totemperature, light)
    humid = get_value(tohumidity, temp)
    location = get_value(tolocation, humid)
    all_locations.append(location)
    

print(min(all_locations))


fh.close()