
input = int(input())

for x in range(input):
    for o in range(input+x):
        if input -x-1 <= o:
            print("*",end ="")
        else:
            print(" ",end= "")
    print()