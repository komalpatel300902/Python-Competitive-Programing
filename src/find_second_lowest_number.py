"""Hacker Rank Question Solution"""

if __name__ == '__main__':

    # getting the values into a list
    names = []
    value = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        value += [score]
        names += [name]
        
    # finding the second lowest value
    frist_value = second_value = value[0]
    for x in value:
        if x < frist_value:
            second_value = frist_value
            frist_value = x
        elif x > frist_value and (x < second_value or frist_value == second_value):
            second_value = x
    
    # sorting the names Alphabatically
    output = []
    for m in range(len(value)):
        if value[m] == second_value:
            output += [names[m]]
    output.sort()

    # Printing the output
    for o in output:
        print(o)
        
    
    