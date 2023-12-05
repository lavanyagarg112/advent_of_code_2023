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
  

for j in seeds:
    start = j[0]
    end = j[1]
    for i in range(start,end+1):
        soil = get_value(tosoils, i)
        fertiliser = get_value(tofertilisers, soil)
        water = get_value(towater, fertiliser)
        light = get_value(tolight, water)
        temp = get_value(totemperature, light)
        humid = get_value(tohumidity, temp)
        location = get_value(tolocation, humid)
        if min_location == "start" or location < min_location:
            min_location = location

    

print(min_location)


fh.close()