def read_from_file(filename):
    with open(filename, 'r') as f:
        line = [l.strip().split('   ') for l in f]
        return line
    
def main():
    FILENAME = 'input.txt'
    numbers = read_from_file(FILENAME)
    numbers_left = [number[0] for number in numbers]
    numbers_right = [number[1] for number in numbers]
    numbers_right.sort()
    numbers_left.sort()
    diference = [abs(int(right) - int(left)) for left, right in zip(numbers_left, numbers_right)]
    print(sum(diference))


if __name__ == "__main__":
    main()