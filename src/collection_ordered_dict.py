"""Solution of HackerRank Question"""

from collections import OrderedDict

dic = OrderedDict()
n = int(input())

for x in range(n):
    cart = input().split(" ")
    value = int(cart.pop())
    name = " ".join(cart)
    if name in dic:
        dic[name] = dic[name] + value
    else:
        dic[name] = value
    
for x in dic:
    print(x,dic[x])
    
    
    
    