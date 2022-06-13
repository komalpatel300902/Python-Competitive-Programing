'''Only used function of the list that are provided by compiler.'''


def lst_fun(lst ,command):
    cmd_fragment = command.split()
    if cmd_fragment[0] == "insert":
        lst.insert(int(cmd_fragment[1]),int(cmd_fragment[2]))
        
    elif cmd_fragment[0] == "print":
        print(lst)
        
    elif cmd_fragment[0] == "remove":
        lst.remove(int(cmd_fragment[1]))
        
    elif cmd_fragment[0] == "append":
        lst.append(int(cmd_fragment[1]))
        
    elif cmd_fragment[0] == "sort":
        lst.sort()
        
    elif cmd_fragment[0] == "pop":
        lst.pop()
        
    if cmd_fragment[0] == "reverse":
        lst.reverse()
        
N = int(input())
lst = []
for x in range(N):
    command = input()
    lst_fun(lst ,command)
