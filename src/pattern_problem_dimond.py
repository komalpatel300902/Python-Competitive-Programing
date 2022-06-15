
"""Ths is a pattern problem.
Number of rows is as per user input.
Number of stars in each column is 2*(number of row) -1"""


input = int(input())

# This prints upper half pyramid
for x in range(input):
    for o in range(input+x):
        if input -x-1 <= o:
            print("*",end ="")
        else:
            print(" ",end= "")
    print()

# This prints lower half Inverted pyramid
for x in range(input):
    for o in range(2*input - x -1):
        if o>=x:
            print("*",end ="")
        else:
            print(" ",end= "")
    print()