'''
This programe finds out the Average of Students Marks.
'''

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
values = student_marks[query_name]
average = 0
for x in values:
    average += x
    
print('%.2f'%(average/len(values))) # only show 2 decimal palces