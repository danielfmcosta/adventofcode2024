from collections import deque

def parse_input(s):
    grid = s.splitlines()
    rA, rB, rC = None, None, None
    program = []
    aux = []
    for row in grid:
        if row.startswith("Register A:"):
            rA = int(row.split(':')[-1].strip())
        elif row.startswith("Register B:"):
            rB = int(row.split(':')[-1].strip())
        elif row.startswith("Register C:"):
            rC = int(row.split(':')[-1].strip())
        elif row.startswith("Program:"):
            aux = [row.split(':')[-1].strip()]
            aux = aux[0].split(',')
            program = [int(x) for x in aux]
    return rA, rB, rC, program

with open("input.txt", "r") as f:
    s = f.read().strip()

rA, rB, rC, programs = parse_input(s)
print(rA, rB, rC, programs)
debug = []

while rA != 0:
    print(rA)
    debug.append((((rA%8)^7) ^ 7) ^ (rA // (2**((rA%8)^7)))%8)
    rA = rA // 8


queue = deque([[1, len(programs) - 1]])
min_a = float('inf')

while len(queue) > 0:
    node = queue.popleft()
    starting_a = node[0]
    ip = node[1]
    
    for n in range(8):
        a = starting_a + n

        b = (((a%8)^7) ^ 7) ^ (a // (2**((a%8)^7)))
        
        print(a)
        if b % 8 == programs[ip]:
            if ip == 0 and a < min_a:
                min_a = a
            elif ip != 0:
                queue.append([a * 8, ip - 1])

print(min_a)
print(debug)

