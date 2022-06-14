'''
This program changes the case of element.
SAMPLE : Pythonist 2 → pYTHONIST 2  
'''

def swap_case(s):
    result = ""
    for x in s:
      
        if x.islower():
            result += x.upper()
        elif x.isupper():
            result += x.lower()
        else:
            result += x
    return result


s = input()
result = swap_case(s)
print(result)