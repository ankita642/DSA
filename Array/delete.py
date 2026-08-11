from array import *

val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

val.pop(2)  #delete element by index
val.remove(2)  #delete element by value
val.pop()   #delete last element

for i in range (0, len(val)):
    print(val[i], end= " ")

