def improve_readability(input_text):
    sections = input_text.strip().split('\n\n')
    grid = [list(line) for line in sections[0].split('\n')]
    movements = sections[1].replace('\n', '')
    return grid, movements

def scale_grid(grid):
    scaled_grid = []
    for row in grid:
        scaled_row = []
        for cell in row:
            if cell == '#':
                scaled_row.append('##')
            elif cell == 'O':
                scaled_row.append('[]')
            elif cell == '.':
                scaled_row.append('..')
            elif cell == '@':
                scaled_row.append('@.')
        scaled_grid.append(''.join(scaled_row))
    return [list(row) for row in scaled_grid]

def find_move(direction):
    return {
        '^': (-1, 0),
        'v': (1, 0),
        '>': (0, 1),
        '<': (0, -1)  
    }[direction]

with open('input.txt', 'r') as f:
    input_data = f.read().strip()

grid, movements = improve_readability(input_data)

cx, cy = 0, 0
grid = scale_grid(grid)
n, m = len(grid), len(grid[0])
for i in range(n):
    for j in range(m): 
        if grid[i][j] == '@':
            cx, cy = i, j
            break

for movement in movements:
    dx, dy = find_move(movement)
    coords_2_move = [(cx, cy)]
    i=0
    impos = False
    while i<len(coords_2_move):
        x, y = coords_2_move[i]
        nx, ny = x+dx, y+dy
        if grid[nx][ny] in "[]":
            if (nx, ny) not in coords_2_move:
                coords_2_move.append((nx, ny))
            if grid[nx][ny] == "[":
                if (nx, ny+1) not in coords_2_move:
                    coords_2_move.append((nx, ny+1))
            if grid[nx][ny] == "]":
                if (nx, ny-1) not in coords_2_move:
                    coords_2_move.append((nx, ny-1))
        elif grid[nx][ny] == "#":
            impos = True
            break
        i+=1
    if impos:
        continue
    new_grid = [[grid[i][j] for j in range(m)] for i in range(n)]
    for x, y in coords_2_move:
        new_grid[x][y] = "."
    for x, y in coords_2_move:
        new_grid[x+dx][y+dy] = grid[x][y]
    
    grid = new_grid
    #print("".join(["".join(row) + "\n" for row in grid]))
    cx += dx
    cy += dy

ans=0
for i in range(n):
    for j in range(m):
        if grid[i][j] != "[":
            continue
        ans+=100*i+j

print(ans)