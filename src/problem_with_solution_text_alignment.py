'''
This program print HackerRank Logo...
''' 

thickness = int(input()) 
c = 'H'
num = 0
five_times_of_thickness = thickness*5
thickness_half = thickness//2
#Top Cone
for i in range(thickness):
    for t in range(0,thickness+i):
        if t >= thickness - i -1:
            print("H",end = "")
        else:
            print(" ",end = "")
    print()
#Top Pillars
for i in range(thickness+1):
    print(" "*thickness_half,end = "")
    for x in range(five_times_of_thickness):
        if x <thickness or x >= five_times_of_thickness - thickness:
            print("H",end = "")
        else:
            print(" ",end = "")
    print()    
#Middle Belt
for i in range((thickness+1)//2):
    print(" "*thickness_half,end = "")
    for x in range(five_times_of_thickness):
        print("H",end = "")
    print()
#Bottom Pillars
for i in range(thickness+1):
    print(" "*thickness_half,end = "")
    for x in range(five_times_of_thickness):
        if x <thickness or x >=five_times_of_thickness -thickness:
            print("H",end = "")
        else:
        
            print(" ",end = "")
    print()
#Bottom Cone
for i in range(thickness):
    print(" "*(five_times_of_thickness -thickness),end = "")
    for t in range(0,(2*thickness-1)-i):
        
        if t >= i :
            print("H",end = "")
        else:
            print(" ",end = "")
    print()