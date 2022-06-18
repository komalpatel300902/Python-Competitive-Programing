"Solution of HackerRank Question"

def solve(s):
    refined_words = []
    words = s.split(" ")
    for x in words:
        refined_words += [x.capitalize()]
    return " ".join(refined_words)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()