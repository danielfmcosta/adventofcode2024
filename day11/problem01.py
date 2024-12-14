def read_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f ]

def blink(rocks):
    i=0
    while i<len(rocks):
        rock = rocks[i]
        if int(rock) == 0:
            rocks[i] = '1'
        elif len(rock) % 2 == 0:
            rocks[i] = rock[:len(rock)//2] 
            rocks.insert(i+1, str(int(rock[len(rock)//2:])))
            i+=1
        else:
            temp = int(rock) * 2024
            rocks[i] = str(temp)
        i+=1

    return rocks



def main():
    FILENAME = 'input.txt'
    rocks = read_from_file(FILENAME)[0].split(' ')
    print(rocks)
    for _ in range(25):
        #print(rocks)
        rocks = blink(rocks)
    print(len(rocks))
if __name__ == "__main__":
    main()
