def improve_readability(input):
    robots = []
    for i in range(len(input)):
        pos, vel = input[i].split(' ')
        p = pos[2:].split(',')
        v = vel[2:].split(',')
        robots.append([[int(p[0]), int(p[1])], [int(v[0]), int(v[1])]])     
    return robots

def tiles(width, height):
    return [['.' for _ in range(width)] for _ in range(height)]

def robots_on_tiles(robots, grid):
    for robot in robots:
        x, y = robot[0]
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            grid[y][x] = '1'
    return grid

def robots_new_positions(robots, width, height):
    for robot in robots:
        robot[0][0] = (robot[1][0] + robot[0][0]) % width
        robot[0][1] = (robot[1][1] + robot[0][1]) % height
    return robots

def write_grid_to_file(grid, second, file):
    file.write(f"Second {second}:\n")
    for row in grid:
        file.write(''.join(row) + '\n')
    file.write('\n')

def robots_movement(robots, grid, seconds):
    with open("grid_output.txt", 'w') as file:
        for second in range(seconds):
            grid = tiles(len(grid[0]), len(grid))
            robots = robots_new_positions(robots, len(grid[0]), len(grid))
            grid = robots_on_tiles(robots, grid)

            # Write the current grid to the file
            write_grid_to_file(grid, second, file)

            #if check_easter_egg(grid):
            #    print("Easter egg found at second", second)
            #    break
    return robots

def check_easter_egg(grid):
    x = 5
    for i in range(len(grid)):
        row_string = ''.join(grid[i])
        if '1' * x in row_string:
            print(row_string)
            print(f"Row {i} contains at least {x} sequential '1's.")
            return True
    return False

with open('input.txt', 'r') as f:
    s = f.read().strip()

input = s.split('\n')
robots = improve_readability(input)
w, h = 101, 103
grid = tiles(w, h)

robots = robots_movement(robots, grid, 8000)
grid = robots_on_tiles(robots, grid)
