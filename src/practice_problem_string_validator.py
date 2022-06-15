"""STRING VALIDATOR"""

s = input()
a = [False,False,False,False,False]

for x in s:
    if x.isalnum() and not a[0] :
        a[0] = True
    if x.isalpha() and not a[1] :
        a[1] = True
    if x.isdigit() and not a[2] :
        a[2] = True
    if x.islower() and not a[3] :
        a[3] = True
    if x.isupper() and not a[4] :
        a[4] = True
    
for i in a:
    print(i)