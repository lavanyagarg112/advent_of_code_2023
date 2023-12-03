
fh = open("/Users/lavanya/Documents/GitHub/advent_of_code/q3/input.txt", "r")
fhread = fh.readlines()
rows = len(fhread)
cols = len(fhread[0])-1
sums = 0
def check_symbol(lst, row, col):
      
      if row<0 or row >= rows or col < 0 or col >= cols:
           return False

      if lst[row][col] not in ".0123456789":
            return True
      else:
            return False

for i in range(rows):
        j = 0
        while j < cols:
            num = 0
            if fhread[i][j] in "0123456789": 
                flag = False
                while j < cols and fhread[i][j] in "0123456789":
                    if check_symbol(fhread, i-1, j-1) or check_symbol(fhread, i-1,j) or check_symbol(fhread, i-1, j+1) or check_symbol(fhread, i, j-1) or check_symbol(fhread,i,j+1) or check_symbol(fhread,i+1,j-1) or check_symbol(fhread,i+1,j) or check_symbol(fhread,i+1,j+1):  
                         flag = True
                    num = num*10 + int(fhread[i][j])
                    j = j + 1
                if flag == True:
                    sums = sums + num
                else:
                    j = j + 1
            else:
                j = j + 1

print(sums)

fh.close()