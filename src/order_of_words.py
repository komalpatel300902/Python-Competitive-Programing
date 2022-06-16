"""Solution of HackerRank Question"""

from collections import OrderedDict

dic = OrderedDict()
n = int(input())
for x in range(n):
    string = input()
    if string in dic:
        dic[string] = dic[string] + 1
    else:
        dic[string] = 1
strg = ""       
for x in dic:
    strg += str(dic[x]) + " "

print(len(dic))
print(strg)
