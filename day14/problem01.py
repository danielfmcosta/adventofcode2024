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
            if grid[y][x] != '.':
                grid[y][x] = str(int(grid[y][x]) + 1)
            else:
                grid[y][x] = '1'
    return grid

def robots_new_positions(robots, width, height):
    for robot in robots:
        robot[0][0] = (robot[1][0] + robot[0][0]) % width
        robot[0][1] = (robot[1][1] + robot[0][1]) % height
    return robots
    
def robots_movement(robots, grid, seconds):
    for _ in range(seconds):
        robots=robots_new_positions(robots, len(grid[0]), len(grid))
        
    return robots

def quadrants(grid):
    q1, q2, q3, q4 = [], [], [], []
    for i in range(len(grid)//2):
        q1.append(grid[i][:len(grid[0])//2])
        q2.append(grid[i][len(grid[0])//2+1:])
    for i in range(len(grid)//2+1, len(grid)):
        q3.append(grid[i][:len(grid[0])//2])
        q4.append(grid[i][len(grid[0])//2+1:])
    return q1, q2, q3, q4

def safety_factor(q1, q2, q3, q4):
    sum1, sum2, sum3, sum4 = 0, 0, 0, 0
    sum1 = sum([int(x) for row in q1 for x in row if x != '.'])
    sum2 = sum([int(x) for row in q2 for x in row if x != '.'])
    sum3 = sum([int(x) for row in q3 for x in row if x != '.'])
    sum4 = sum([int(x) for row in q4 for x in row if x != '.'])
    return sum1*sum2*sum3*sum4
    

with open('input.txt', 'r') as f:
    s = f.read().strip()

input = s.split('\n')
robots = improve_readability(input)
w, h = 101, 103
grid = tiles(w, h)

robots = robots_movement(robots, grid, 100)
grid = robots_on_tiles(robots, grid)

print("\n".join(["".join(row) for row in grid]))
q1, q2, q3, q4 = quadrants(grid)
print(safety_factor(q1, q2, q3, q4))