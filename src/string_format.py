"""Solution of HackerRank Problem"""

def merge_the_tools(string, k):

    strg =""
    for x in range(len(string)):    # Traversing eac element
        if string[x] not in strg :  
            strg += string[x]
        if (x+1)%(k) == 0:
            print(strg)
            strg = ""

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)