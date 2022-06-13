"""This is program that checks wheather the year is leep or not.
Conditions: 1. The year can be evenly divided by 4, is a leap year, unless:
            2. The year can be evenly divided by 100, it is NOT a leap year, unless:
               2.1 The year is also evenly divisible by 400. Then it is a leap year.
"""

def is_leap(year):
    leap = False
    if year%100 == 0:           # The year can be evenly divided by 100.
        if year % 400 == 0:     # The year is also evenly divisible by 400.
            return True
    elif year % 4 == 0:         # The year can be evenly divided by 4.
        return True
    return leap

year = int(input())
print(is_leap(year))