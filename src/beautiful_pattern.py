# Enter your code here. Read input from STDIN. Print output to STDOUT

pattern_input = list(map(int,input().split(" ")))
row = pattern_input[0]
column = pattern_input[1]

# Upper Portion
for x in range(row//2):
    for y in range(row//2+x+1):
        if y >= row//2 -x:
            print(".|.",end= "")
        else:
            print("---",end= "")
        
    for m in range(row//2-x):
        print("---",end= "")
    print()

# Middle Portion
factor = (column-7)//2
print("-"*factor + "WELCOME" + "-"*factor)

# Lower Portion
for x in range(row//2):
    for y in range((row//2)*2-x):
        if y > x :
            print(".|.",end= "")
        else:
            print("---",end= "")
        
    for m in range(x+1):
        print("---",end= "")
    print()
