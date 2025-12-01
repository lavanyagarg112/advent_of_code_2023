# too long to run

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

times = clean(((fhread[0].split(":"))[1]).split(" "))
distances = clean(((fhread[1].split(":"))[1]).split(" "))

total_time = ""
total_distance = ""

for i in times:
    total_time += i

for i in distances:
    total_distance += i

total_time = int(total_time)
total_distance = int(total_distance)

prod = 1

t = total_time
d = total_distance
ways = 0
max_num = "start"
for j in range(t):
    if j == 0 or j == t:
        pass
    else:
        s = j
        move = t - j 
        dis = s*move 
        if dis > d:
            ways += 1
            max_num = dis
        if max_num != "start" and dis < d:
            break
prod *= ways 

print(prod) 


fh.close()