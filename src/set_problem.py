"""Solution of HackerRank Question"""

n,m = list(map(int,input().split(" ")))
elements = list(map(int,input().split(" ")))
a = set(map(int,input().split(" ")))
b = set(map(int,input().split(" ")))

result = 0
for element in elements:
    if element in a:
        result += 1
    if element in b:
        result += -1
print(result)
