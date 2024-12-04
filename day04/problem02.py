def read_from_file(filename):
    with open(filename, 'r') as f:
        line = [l.strip() for l in f]
        return line

def check_X(lines, i, j):
    if i < 1 or j < 1:
        return 0
    if i == len(lines) - 1 or j == len(lines[i]) - 1:
        return 0
    if lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S' and lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S':
        return 1
    if lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S' and lines[i+1][j-1] == 'S' and lines[i-1][j+1] == 'M':
        return 1
    if lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M' and lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S':
        return 1
    if lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M' and lines[i+1][j-1] == 'S' and lines[i-1][j+1] == 'M':
        return 1
    return 0

def main():
    FILENAME = 'input.txt'
    lines = read_from_file(FILENAME)
    print(lines)
    sum = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == 'A':
                print(i, j)
                sum += check_X(lines, i, j)
                print(sum)
    print(sum)

if __name__ == "__main__":
    main()