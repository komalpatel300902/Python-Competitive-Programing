"Solution of HackerRank Question"


import calendar
weekend = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
date = list(map(int,input().split(" ")))
weak_day = calendar.weekday(date[2],date[0],date[1])
print(weekend[weak_day])
