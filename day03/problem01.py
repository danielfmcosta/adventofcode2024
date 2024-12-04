def read_from_file(filename):
    with open(filename, 'r') as f:
        line = [l.strip().split('mul') for l in f]
        return line

def filter_line(line):
    characters = "1234567890(,)"
    try:
        line = line[:line.index(')')+1]
        if any(c not in characters for c in line):
            return ''
        return line
    except ValueError:
        return ''

def multiply(string):
    if string == '':
        return 0
    string = string.split(',')
    if len(string) != 2:
        return 0
    string[0] = string[0][1:]
    string[1] = string[1][:-1]
    x = int(string[0]) * int(string[1])
    return x

def main():
    FILENAME = 'input.txt'
    lines = read_from_file(FILENAME)
    sum = 0
    for line in lines:
        for string in line:
            sum += multiply(filter_line(string))
    print(sum)

if __name__ == "__main__":
    main()