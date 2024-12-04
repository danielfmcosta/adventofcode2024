def read_from_file(filename):
    with open(filename, 'r') as f:
        line = [l.strip() for l in f]
        return line

def check_top_left(lines, i, j):
    if i < 3 or j < 3:
        return 0
    if lines[i-1][j-1] == 'M':
        if lines[i-2][j-2] == 'A':
            if lines[i-3][j-3] == 'S':
                return 1
    return 0

def check_up(lines, i, j):
    if i < 3:
        return 0
    if lines[i-1][j] == 'M':
        if lines[i-2][j] == 'A':
            if lines[i-3][j] == 'S':
                return 1
    return 0
 

def check_top_right(lines, i, j):
    if i < 3 or j >= len(lines[i]) - 3:
        return 0
    if lines[i-1][j+1] == 'M':
        if lines[i-2][j+2] == 'A':
            if lines[i-3][j+3] == 'S':
                return 1
    return 0

def check_left(lines, i, j):
    if j < 3:
        return 0
    if lines[i][j-1] == 'M':
        if lines[i][j-2] == 'A':
            if lines[i][j-3] == 'S':
                return 1
    return 0

def check_right(lines, i, j):
    if j >= len(lines[i]) - 3:
        return 0
    if lines[i][j+1] == 'M':
        if lines[i][j+2] == 'A':
            if lines[i][j+3] == 'S':
                return 1
    return 0

def check_bottom_left(lines, i, j):
    if i >= len(lines[i]) - 3 or j < 3:
        return 0
    if lines[i+1][j-1] == 'M':
        if lines[i+2][j-2] == 'A':
            if lines[i+3][j-3] == 'S':
                return 1
    return 0

def check_down(lines, i, j):
    if i >= len(lines[i]) - 3:
        return 0
    if lines[i+1][j] == 'M':
        if lines[i+2][j] == 'A':
            if lines[i+3][j] == 'S':
                return 1
    return 0

def check_bottom_right(lines, i, j):
    if i >= len(lines[i]) - 3 or j >= len(lines[i]) - 3:
        return 0
    if lines[i+1][j+1] == 'M':
        if lines[i+2][j+2] == 'A':
            if lines[i+3][j+3] == 'S':
                return 1
    return 0

def main():
    FILENAME = 'input.txt'
    lines = read_from_file(FILENAME)
    print(lines)
    sum = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == 'X':
                print(i, j)
                sum += check_top_left(lines, i, j)
                sum += check_up(lines, i, j)
                sum += check_top_right(lines, i, j)
                sum += check_left(lines, i, j)
                sum += check_right(lines, i, j)
                sum += check_bottom_left(lines, i, j)
                sum += check_down(lines, i, j)
                sum += check_bottom_right(lines, i, j)
                print(sum)
    print(sum)

if __name__ == "__main__":
    main()