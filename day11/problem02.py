def read_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip().split() for line in file]

def blink(rock):
    if rock == 0:
        return [1]
    s = str(rock)
    num_digits = len(s)
    if num_digits % 2 == 0:
        mid = num_digits // 2
        lhs, rhs = int(s[:mid]), int(s[mid:])
        return [lhs, rhs]
    return [rock * 2024]

def memoize(func):
    memo = {}
    def helper(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return helper

@memoize
def rec(rocks, n):
    if n == 0:
        return len(rocks)
    return sum(rec(tuple(blink(rock)), n - 1) for rock in rocks)

def main():
    FILENAME = 'input.txt'
    rocks = [int(rock) for rock in read_from_file(FILENAME)[0]]
    result = rec(tuple(rocks), 75) 
    print(result)

if __name__ == "__main__":
    main()
