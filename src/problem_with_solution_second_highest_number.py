"""
Solution for the program to find the second highest number.
"""

n = int(input())
arr = map(int, input().split())
arr = list(arr)
highest_value = arr[0]
second_highest_value = arr[0]
for x in arr:
    if highest_value < x:
        second_highest_value = highest_value
        highest_value = x
    elif (x < highest_value and highest_value == second_highest_value) or (x < highest_value and x > second_highest_value):
        second_highest_value = x
        
print(second_highest_value)