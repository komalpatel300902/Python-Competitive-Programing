'''This is Solution of HackerRank Question '''

from cmath import *
n = input()

if "+" in n :
    real ,img = n.split("+")
    img  = int(img[:len(img)-1])
    real = int(real)

else:
    numbers = n.split("-")
    if len(numbers) == 2:
        real ,img = n.split("-")
    
        img  = int(img[:len(img)-1])*-1
        real = int(real)
    
    else:
        n ,real ,img = n.split("-")
        img  = int(img[:len(img)-1])*-1
        real = int(real)*-1
      

modulus = abs(complex(real,img))
phas =  phase(complex(real, img))
print(modulus)
print(phas)
