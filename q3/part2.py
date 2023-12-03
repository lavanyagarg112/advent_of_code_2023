# disclaimer: my solution assumes that the numbers around a gear are all unique

fh = open("/Users/lavanya/Documents/GitHub/advent_of_code/q3/input.txt", "r")
fhread = fh.readlines()
rows = len(fhread)
cols = len(fhread[0])-1
sums = 0

def get_num(row,col):
    while col >= 0 and fhread[row][col] in "0123456789":
        col = col - 1
    col = col + 1
    num = 0
    while col < cols and fhread[row][col] in "0123456789":
         num = num*10 + int(fhread[row][col])
         col = col + 1
    return num
    
    
def check_num(row, col):
      
      if row<0 or row >= rows or col < 0 or col >= cols:
           return False

      if fhread[row][col] in "0123456789":
            return True
      else:
            return False

for i in range(rows):
    for j in range(cols):
         if fhread[i][j] == "*":
            nums = set()
            if check_num(i-1,j-1):
                nums.add(get_num(i-1,j-1))
            if check_num(i-1,j):
                 nums.add(get_num(i-1,j))
            if check_num(i-1,j+1):
                 nums.add(get_num(i-1,j+1))
            if check_num(i,j-1):
                nums.add(get_num(i,j-1))
            if check_num(i,j+1):
                nums.add(get_num(i,j+1))
            if check_num(i+1,j-1):
                nums.add(get_num(i+1,j-1))
            if check_num(i+1,j):
                nums.add(get_num(i+1,j))
            if check_num(i+1,j+1):
                nums.add(get_num(i+1,j+1))
            
            if len(nums) == 2:
                prod = 1
                for k in nums:
                    prod = prod * k
                sums = sums + prod


print(sums)

fh.close()