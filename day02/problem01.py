def read_from_file(filename):
    with open(filename, 'r') as f:
        line = [l.strip().split(' ') for l in f]
        return line
    
def check_monotonic(levels):
    return (
        all(levels[i] <= levels[i + 1] for i in range(len(levels) - 1)) or 
        all(levels[i] >= levels[i + 1] for i in range(len(levels) - 1))
    )


def check_jumps(levels):
    return all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))

    
def main():
    FILENAME = 'input.txt'
    sum=0
    lines = read_from_file(FILENAME)
    for levels in lines:
        levels = [int(level) for level in levels]
        incline=check_monotonic(levels)
        jumps=check_jumps(levels)
        if incline and jumps:
            sum+=1
            print(levels)
    print(sum)


if __name__ == "__main__":
    main()