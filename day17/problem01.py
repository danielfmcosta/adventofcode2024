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

    for i in range(0, len(aux), 2):
        print(aux[i])
        program.append((int(aux[i]), int(aux[i+1])))
    return rA, rB, rC, program

def adv(rA, rB):
    """Performs division between rA and 2^rB"""
    return rA // (2 ** rB)


def bxl(rB, literal):
    """Performs a bitwise XOR of rB and the literal."""
    return rB ^ literal


def bst(value):
    """Returns the value modulo 8 (keeping the lowest 3 bits)."""
    return value % 8


def jnz(rA, literal, instruction_pointer):
    """
    If rA is zero, do nothing.
    Otherwise, jump to the instruction specified by the literal operand.
    """
    return literal if rA != 0 else instruction_pointer + 2


def bxc(rB, rC):
    """Performs a bitwise XOR between rB and rC, storing the result in rB."""
    return rB ^ rC


def out(value):
    """Outputs the value modulo 8."""
    return value % 8


def bdv(rA, rB):
    """Performs adv operation and stores the result in register B."""
    return adv(rA, rB)


def cdv(rA, rB):
    """Performs adv operation and stores the result in register C."""
    return adv(rA, rB)

literal_to_combo = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: lambda: rA,
    5: lambda: rB,
    6: lambda: rC,
    7: lambda: 0
}

def instruction(rA, rB, rC, program, instruction_pointer, debug):
    opcode, literal = program
    combo = literal_to_combo[literal]
    combo = combo() if callable(combo) else combo

    if opcode == 0:
        rA = adv(rA, combo)
        instruction_pointer += 1
    elif opcode == 1:
        rB = bxl(rB, literal)
        instruction_pointer += 1
    elif opcode == 2:
        rB = bst(combo)
        instruction_pointer += 1
    elif opcode == 3:
        instruction_pointer = jnz(rA, literal, instruction_pointer)
    elif opcode == 4:
        rB = bxc(rB, rC)
        instruction_pointer += 1
    elif opcode == 5:
        debug.append(out(combo))
        print(out(combo))
        instruction_pointer += 1
    elif opcode == 6:
        rB = bdv(rA, combo)
        instruction_pointer += 1
    elif opcode == 7:
        rC = cdv(rA, combo)
        instruction_pointer += 1
        
    return rA, rB, rC, instruction_pointer, debug

with open("input.txt", "r") as f:
    s = f.read().strip()

rA, rB, rC, programs = parse_input(s)
print(rA, rB, rC, programs)
instruction_pointer = 0
debug = []

while instruction_pointer < len(programs):
    rA, rB, rC, instruction_pointer, debug = instruction(rA, rB, rC, programs[instruction_pointer], instruction_pointer, debug)

print(rA, rB, rC)
print(debug)