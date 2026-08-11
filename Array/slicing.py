from array import *

val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

abc = val[2 : 5]
abc = val[2 : -3]   #to remove last three elements
abc = val[::-1]     #to reverse the array

for i in range (0, len(abc)):
    print(abc[i], end= " ")



