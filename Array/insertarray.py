from array import *

val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

val.insert(1, 50)
val.append(100)     #append use for add element to last
val[2] = 200        #To replace element(overide element)
for i in range (0, len(val)):
    print(val[i], end= " ")

