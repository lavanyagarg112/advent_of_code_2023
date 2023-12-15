fh = open("/Users/lavanya/Documents/GitHub/advent_of_code_2023/q10/input.txt", "r")
fhread = fh.readlines()

fh.close()

def clean(lst):
    xs = []
    for i in lst:
        if i != "" and i !="\n":
            i = i.rstrip("\n")
            xs.append(i)
    return xs

fhread = clean(fhread)

dir = {"|": ("north", "south"), "-": ("east", "west"), "L": ("north","east"), "J": ("north", "west"), "7": ("south", "west"), "F": ("south", "east"), ".": ("ground",), "S": ("start",)}

matrix = []

for i in fhread:
    matrix.append(list(i))

rows = len(matrix)
cols = len(matrix[0])
start_pos = 0

# not done

def check(current, direction):
    if current[0] < 0 or current[1] < 0 or current[0] >= rows or current[1] >= cols:
        return False

    r = current[0]
    c = current[1]

    if direction == "east":    
        checkdir = (r, c+1)
    elif direction == "west":
        checkdir = (r, c-1)
    elif direction == "north":
        checkdir = (r-1, c)
    else:
        checkdir = (r+1, c)
 

    if "start" in dir[matrix[r][c]]:
        if direction == "east":
            c = c + 1
            direction = "west"
        elif direction == "west":
            c = c - 1
            direction = "east"
        elif direction == "north":
            r = r - 1
            direction = "south"
        else:
            r = r + 1
            direction = "north"

        if direction in dir[matrix[r][c]]:
            return "start"
        
        else:
            return False

    return direction in dir[matrix[r][c]]

def checkpath(curr, path):

    row = curr[0]
    col = curr[1]

    left = check((row, col-1), "east")
    right = check((row, col+1), "west")
    top = check((row-1, col), "south")
    bottom = check((row+1, col), "north")

    if path == "L":
        right = False
    elif path == "R":
        left = False
    elif path == "T":
        bottom = False
    else:
        top = False

    if left and checkvalid((row, col-1), "R"):
        print("left")
        return ((row, col-1), "L")
    elif right and checkvalid((row, col+1), "L"):
        print("right")
        return ((row, col+1), "R")
    elif top and checkvalid((row-1, col), "B"):
        print("top")
        return ((row-1, col), "T")
    else:
        print("bottom")
        return ((row+1, col), "B")

'''def checkvalid(curr, coming_from):
    
    row = curr[0]
    col = curr[1]

    left = check((row, col-1), "east")
    right = check((row, col+1), "west")
    top = check((row-1, col), "south")
    bottom = check((row+1, col), "north")

    if coming_from == "L":
        left = False
    elif coming_from == "R":
        right = False
    elif coming_from == "T":
        top = False
    else:
        bottom = False
    if "start" in (left, right, top, bottom):
        return True
    elif True not in (left, right, top, bottom):
        return False
    else:
        return (left and checkvalid((row, col-1), "R")) or ((right and checkvalid((row, col+1), "L")) or ((top and checkvalid((row-1, col), "B")) or (bottom and checkvalid((row+1, col), "T"))))
'''

def checkvalid(curr, coming_from):
    stack = [(curr, coming_from)]
    travelled = []
    while stack:    
        curr, coming_from = stack.pop()
        travelled.append(curr)
        row, col = curr

        left = check((row, col - 1), "east")
        right = check((row, col + 1), "west")
        top = check((row - 1, col), "south")
        bottom = check((row + 1, col), "north")

        if coming_from == "L":
            left = False
        elif coming_from == "R":
            right = False
        elif coming_from == "T":
            top = False
        else:
            bottom = False

        if "start" in (left, right, top, bottom):
            return True

        if True not in (left, right, top, bottom):
            continue

        if left and (row, col - 1) not in travelled:
            stack.append(((row, col - 1), "R"))
        if right and (row, col + 1) not in travelled:
            stack.append(((row, col + 1), "L"))
        if top and (row - 1, col) not in travelled:
            stack.append(((row - 1, col), "B"))
        if bottom and (row+1, col) not in travelled:
            stack.append(((row + 1, col), "T"))

    return False

def find_loop(start):

    row = start[0]
    col = start[1]

    
    left = check((row, col-1), "east")
    right = check((row, col+1), "west")
    top = check((row-1, col), "south")
    bottom = check((row+1, col), "north")


    path1 = ""
    path2 = ""

        
    if left:
        if path1 == "":
            path1 = "L"
            path1_curr = (row,col-1)
        else:
            path2 = "L"
            path2_curr = (row,col-1)
    if right:
        if path1 == "":
            path1 = "R"
            path1_curr = (row,col+1)
        else:
            path2 ="R"
            path2_curr = (row,col+1)
    if top:
        if path1 == "":
            path1 = "T"
            path1_curr = (row-1,col)
        else:
            path2 = "T"
            path2_curr = (row-1,col)
    if bottom:
        if path1 == "":
            path1 = "B"
            path1_curr = (row+1,col)
        else:
            path2 = "B"
            path2_curr = (row+1,col)

    steps = 1

    while path2_curr != start_pos:
        print(path2_curr)
        print(steps)
        #path1_func =  checkpath(path1_curr, path1)
        path2_func = checkpath(path2_curr, path2)
        #path1_curr = path1_func[0]
        path2_curr = path2_func[0]
        #path1 = path1_func[1]
        path2 = path2_func[1]
        steps +=1 
    else:
        return steps

        


flag = False
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "S":
            start_pos = (i,j)
            flag = True
            break
    if flag == True:
        break
    



print(find_loop(start_pos))
