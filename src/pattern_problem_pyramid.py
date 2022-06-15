
"""Ths is a pattern problem.
Number of rows is as per user input.
Number of stars in each column is 2*(number of row) -1"""


input = int(input())

for x in range(input):
    for o in range(input+x):
        if input -x-1 <= o:
            print("*",end ="")
        else:
            print(" ",end= "")
    print()