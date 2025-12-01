fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q15/input.txt", "r")
fhread = fh.readline()
fhread = fhread.split(",")
fh.close()

print(fhread)


total = 0
for i in fhread:
    current = 0
    for j in i:
        asc = ord(j)
        current += asc
        current *= 17
        current = current % 256
    total += current

print(total)

