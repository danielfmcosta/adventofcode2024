def improve_readability(input_text):
    sections = input_text.strip().split('\n\n')
    grid = [list(line) for line in sections[0].split('\n')]
    movements = sections[1].replace('\n', '')
    return grid, movements

def find_robot(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '@':
                return (x, y)

def find_move(direction):
    return {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0)
    }[direction]

def is_valid_position(grid, x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] != '#'

def move_robot_and_boxes(grid, x, y, dx, dy):
    print(dx, dy)
    print("".join(["".join(row) + "\n" for row in grid if len(row) < 15 ]))
    next_x, next_y = x + dx, y + dy

    if not is_valid_position(grid, next_x, next_y):
        return x, y  

    if grid[next_y][next_x] == 'O':  
        stack = []
        bx, by = next_x, next_y
        while is_valid_position(grid, bx, by) and grid[by][bx] == 'O':
            stack.append((bx, by))
            bx += dx
            by += dy

        if not is_valid_position(grid, bx, by) or grid[by][bx] == '#':
            return x, y  

        if grid[by][bx] == '.':
            for box_x, box_y in reversed(stack):
                grid[box_y + dy][box_x + dx] = 'O'
                grid[box_y][box_x] = '.'

            grid[next_y][next_x] = '@'
            grid[y][x] = '.'
            return next_x, next_y

    elif grid[next_y][next_x] == '.':
        grid[next_y][next_x] = '@'
        grid[y][x] = '.'
        return next_x, next_y

    return x, y 

def calculate_gps_sum(grid):
    gps_sum = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'O':
                gps_sum += 100 * y + x
    return gps_sum

def simulate_robot(input_text):
    grid, movements = improve_readability(input_text)
    x, y = find_robot(grid)

    for movement in movements:
        dx, dy = find_move(movement)
        x, y = move_robot_and_boxes(grid, x, y, dx, dy)

    return calculate_gps_sum(grid)

with open('input.txt', 'r') as f:
    s = f.read().strip()

print(simulate_robot(s))