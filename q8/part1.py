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
start = ""


for i in nodes:
    comp = i.split(" = ")
    maps = comp[1].strip("()")
    maps = maps.split(", ")
    node_dict[comp[0]] = (maps[0], maps[1])
    if start == "":
        start = comp[0]

steps = 0

while start != "ZZZ":
    for i in instructions:
        if start != "ZZZ":
            if i == "L":
                start = node_dict[start][0]
            else:
                start = node_dict[start][1]
            steps += 1
        else:
            break

print(steps)

