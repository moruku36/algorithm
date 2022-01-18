null = 0
# array = [[2,null,2,null],[2,null,2,null],[null,null,null,null],[null,null,null,null]]
array = [[4,2,4,2],[4,null,4,2],[2,null,8,2],[16,null,4,null]]
range = [0,1,2]
for y in range:
   for x in range:
       if array[x+1][y] != null:
           if array[x+1][y] == array[x][y]:
               array[x][y] = array[x][y]*2
               array[x+1][y] = null
           if array[x][y] == null:
               array[x][y] = array[x+1][y]
               array[x+1][y] = null
print(array)