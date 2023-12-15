'''
same result at 1000 as at the given number
'''

fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q14/input.txt", "r")
fhread = fh.readlines()
fh.close()

def clean(lst):
    xs = []
    for i in lst:
        if i != "" and i !="\n":
            i = i.rstrip("\n")
            xs.append(i)
    return xs


def cleanprint(arr):
    for i in arr:
        for j in i:
            print(j, end="")
        print()

arr = []
fhread = clean(fhread)
for i in fhread:
    arr.append([])
    for j in i:
        arr[-1].append(j)

def shift(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "O":
                count = i-1
                while arr[count][j] == "." and count >= 0:
                    arr[count][j] = "O"
                    arr[count + 1][j] = "."
                    count -= 1

def movewest(arr):
    newarr = arr[::-1]
    arrnew = []

    for i in range(len(newarr)):
        temp = []
        for j in range(len(newarr[0])):
            temp.append(newarr[j][i])
        arrnew.append(temp)
    return arrnew

for i in range(1000):
  for j in range(4):
    shift(arr)    
    arr = movewest(arr)



load = 0

for i in range(len(arr)):
    count = 0
    for j in arr[i]:
        if j == "O":
            count += 1
    load = load + (count*(len(arr) - i))

print(load)

