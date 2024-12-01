def read_from_file(filename):
    with open(filename, 'r') as f:
        line = [l.strip().split('   ') for l in f]
        return line
    
def main():
    FILENAME = 'input.txt'
    numbers = read_from_file(FILENAME)
    numbers_left = [number[0] for number in numbers]
    numbers_right = [number[1] for number in numbers]
    similarity_score = [numbers_right.count(left) for left in numbers_left]
    total_score = [int(left) * similarity_score for left, similarity_score in zip(numbers_left, similarity_score)]
    print(sum(total_score))


if __name__ == "__main__":
    main()