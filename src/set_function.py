"""Solution of HackerRank Question"""

n = int(input())
s = set(map(int, input().split()))
row = int(input())
for x in range(row):
    cmd = input().split(" ")
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "remove":
        s.remove(int(cmd[1]))
    elif cmd[0] == "discard":
        s.discard(int(cmd[1]))
m = 0
for x in s:
    m+=x
print(m)
