""" This question is based on premutation and combination.
Create all possible outcome for i , j , k set and filter it out with conditin i+j+k == n.
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())
lst = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                lst += [[i,j,k]] 
                
print(lst)