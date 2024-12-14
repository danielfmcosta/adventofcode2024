import re
from fractions import Fraction

def inverse_matrix(matrix):

    determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    if determinant == 0:
        return 0
    const = Fraction(1, determinant)

    return [
        [Fraction(matrix[1][1], 1) * const, Fraction(-matrix[0][1]) * const],
        [Fraction(-matrix[1][0]) * const, Fraction(matrix[0][0]) * const]
    ]

def improve_readability(input):
    claw_machines = []
    i=0
    while i < len(input):
        x1 = re.findall(r'\d+', input[i])
        x2 = re.findall(r'\d+', input[i+1])
        x3 = re.findall(r'\d+', input[i+2])
        inv_matrix = (inverse_matrix([[int(x1[0]), int(x2[0])], [int(x1[1]), int(x2[1])]]))
        claw_machines.append([inv_matrix, [[int(x3[0])], [int(x3[1])]]])
        i+=4
    return claw_machines


def calculate_A_B(claw_machine):
    a, b = 0, 0
    x1, x2, x3, x4 = claw_machine[0][0][0], claw_machine[0][0][1], claw_machine[0][1][0], claw_machine[0][1][1]
    y1, y2 = claw_machine[1][0][0], claw_machine[1][1][0]

    #print(x1, x2, x3, x4, y1, y2)

    a = x1 * y1 + x2 * y2 + x1 * 10000000000000 + x2 * 10000000000000
    b = x3 * y1 + x4 * y2 + x3 * 10000000000000 + x4 * 10000000000000

    print(a, b)
    return a, b

with open('input.txt', 'r') as f:
    s = f.read().strip()


input = s.split('\n')
n, m = len(input), len(input[0])

claw_machines = improve_readability(input)

sum = 0 
for claw_machine in claw_machines:
    a, b = calculate_A_B(claw_machine)
    if a == int(a) and b == int(b):
        sum += a * 3 + b

print(sum)