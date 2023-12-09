fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q9/input.txt", "r")
fhread = fh.readlines()

sums = 0

def clean(lst):
    xs = []
    for i in lst:
        if i != "" and i !="\n":
            i = i.rstrip("\n")
            xs.append(i)
    return xs

def clean_to_int(lst):
    xs = []
    for i in lst:
        if i != "" and i !="\n":
            i = i.rstrip("\n")
            xs.append(int(i))
    return xs

def get_unique(mylist):
    mylist = list( dict.fromkeys(mylist) )
    return mylist

fhread = clean(fhread)

for i in fhread:
    nums = clean_to_int(i.split(" "))
    thelist = []
    my_seq_main = nums
    while get_unique(my_seq_main) != [0]:
        thelist.append(my_seq_main[-1])
        my_seq = []
        for j in range(len(my_seq_main)-1):
            diff = int(my_seq_main[j+1]) - int(my_seq_main[j])
            my_seq.append(diff)
        my_seq_main = my_seq

    thelist.reverse()
    next = 0
    for k in thelist:
        next += k

    sums += next

print(sums)

fh.close()