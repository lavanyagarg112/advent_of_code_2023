fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q2/input.txt", "r")
fhread = fh.readlines()

sums = 0
red = 12
green = 13
blue = 14

for i in fhread:
    games = i.split(":")
    game_num = int((games[0].split(" "))[1])
    allsets = games[1]
    sets_lst = allsets.split(";")
    print(sets_lst)
    for j in sets_lst:
        d = {"red":0, "blue": 0, "green": 0}
        comp = j.split(",")
        for k in comp:
            k = k.lstrip(" ")
            final = k.split(" ")
            color = final[1].rstrip("\n")
            num = int(final[0])
            d[color] += num 
        if d["red"] > red or d["blue"] > blue or d["green"] > green:
            break
    else:
        sums += game_num
        

print(sums)

fh.close()