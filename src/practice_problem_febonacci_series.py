'''This program print fibonacci series upto n terms.
Logic : Every Febonacci term is sum of the previous two term.
f(n) = f(n-1) + f(n-2)

'''

start_point1 = 0 
start_point2 = 1
input = int(input(""))
for x in range(0,input):

    print(start_point2)
    temp = start_point1 + start_point2  # f(n) = f(n-1)+ f(n-2)
    start_point1 = start_point2
    start_point2 = temp
