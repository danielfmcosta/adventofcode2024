def read_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def move_up(grid, pos_row, pos_col):
    while pos_row >= 0 and grid[pos_row][pos_col] != '#':
        grid[pos_row][pos_col] = 'X'
        pos_row -= 1
    if pos_row < 0 or pos_col < 0 or pos_col >= len(grid[0]) or pos_row >= len(grid):
        return  
    move_right(grid, pos_row + 1, pos_col)

def move_right(grid, pos_row, pos_col):
    while pos_col < len(grid[0]) and grid[pos_row][pos_col] != '#':
        grid[pos_row][pos_col] = 'X'
        pos_col += 1
    if pos_row < 0 or pos_col < 0 or pos_col >= len(grid[0]) or pos_row >= len(grid):
        return  
    move_down(grid, pos_row, pos_col - 1)

def move_down(grid, pos_row, pos_col):
    while pos_row < len(grid) and grid[pos_row][pos_col] != '#':
        grid[pos_row][pos_col] = 'X'
        pos_row += 1
    if pos_row < 0 or pos_col < 0 or pos_col >= len(grid[0]) or pos_row >= len(grid):
        return 
    move_left(grid, pos_row - 1, pos_col)

def move_left(grid, pos_row, pos_col):
    while pos_col >= 0 and grid[pos_row][pos_col] != '#':
        grid[pos_row][pos_col] = 'X'
        pos_col -= 1
    if pos_row < 0 or pos_col < 0 or pos_col >= len(grid[0]) or pos_row >= len(grid):
        return  
    move_up(grid, pos_row, pos_col + 1)

def main():
    FILENAME = 'input.txt'
    map_data = read_from_file(FILENAME)
    grid = [list(row) for row in map_data] 
    start_row, start_col = None, None

    for r, row in enumerate(grid):
        if '^' in row:
            start_row, start_col = r, row.index('^')
            break

    move_up(grid, start_row, start_col)
    sum = 0
    for row in grid:
        print("".join(row))
        sum += row.count('X')
    print(sum)
if __name__ == "__main__":
    main()
