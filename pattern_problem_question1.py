rows = int(input(""))
column = int(input(""))

for x in range(rows):
    for f in range(column):
        if f ==0 or f == column-1 or x ==0 or x == rows-1:
            print("*", end = "")
        else:
            print(" ",end = "") 

    print()