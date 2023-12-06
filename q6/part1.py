fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q6/input.txt", "r")
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

times = clean_to_int(((fhread[0].split(":"))[1]).split(" "))
distances = clean_to_int(((fhread[1].split(":"))[1]).split(" "))

prod = 1

for i in range(len(times)):
    t = times[i]
    d = distances[i]
    ways = 0
    for j in range(t):
        if j == 0 or j == t:
            pass
        else:
            s = j
            move = t - j 
            dis = s*move 
            if dis > d:
                ways += 1
    prod *= ways 

print(prod) 


fh.close()