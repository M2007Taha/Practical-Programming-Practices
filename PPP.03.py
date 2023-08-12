#!/bin/python3
"""
Practical-Programming-Practices 03:

https://github.com/jadijadi/Practical-Programming-Practices/tree/main/math/111-999-two-digits-no-zero

@M2007Taha
"""

all_number = []
number = []
for i in range(112,999):
    if '0' not in str(i):
        all_number.append(str(i))

def myfunc(n):
    if i.count(i[0]) == 2 or i.count(i[1]) == 2 or i.count(i[2]) == 2: 
        return True
for i in all_number:
    #if i.count(i[0]) == 2 or i.count(i[1]) == 2 or i.count(i[2]) == 2:
     if myfunc(i) == True:
        number.append(i)

print('Count : {0}, Original number : 216, The main number is as follows :  {} '.format(len(number), 216 - len(number))) 
for i in number: print(i)
