
fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q2/input.txt", "r")
fhread = fh.readlines()

sums = 0

for i in fhread:
    games = i.split(":")
    allsets = games[1]
    sets_lst = allsets.split(";")
    blue = 0
    red = 0
    green = 0
    for j in sets_lst:
        d = {"red":0, "blue": 0, "green": 0}
        comp = j.split(",")
        for k in comp:
            k = k.lstrip(" ")
            final = k.split(" ")
            color = final[1].rstrip("\n")
            num = int(final[0])
            d[color] += num 
        if d["red"] > red:
            red = d["red"]
        
        if d["blue"] > blue:
            blue = d["blue"]

        if d["green"] > green:
            green = d["green"]
    power = red * green * blue
    sums += power
    
        

print(sums)

fh.close()