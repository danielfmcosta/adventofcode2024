def read_from_file(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f if line.strip()]

def simulate_guard(grid, start_row, start_col):
    directions = ['up', 'right', 'down', 'left']
    direction_idx = 0
    pos_row, pos_col = start_row, start_col
    visited_paths = set() 
    
    while 0 < pos_row < len(grid)-1 and 0 < pos_col < len(grid[0])-1:
        next_row, next_col = pos_row, pos_col
        if directions[direction_idx] == 'up':
            next_row -= 1
        elif directions[direction_idx] == 'right':
            next_col += 1
        elif directions[direction_idx] == 'down':
            next_row += 1
        elif directions[direction_idx] == 'left':
            next_col -= 1
        
        # print(next_row, next_col, visited_paths)
        # Check if the next position is within bounds and not a wall
        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != '#':
            # Define the current state as (current_position, direction)
            current_state = (pos_row, pos_col, direction_idx)
            
            # If the state has been visited, it's a loop
            if current_state in visited_paths:
                return 1  # Loop detected
            
            # Add the state to the set of visited states
            visited_paths.add(current_state)
            
            # Move to the next position
            pos_row, pos_col = next_row, next_col
        else:
            # Hit a wall or boundary, change direction
            direction_idx = (direction_idx + 1) % 4
    
    # If the guard exits the grid without looping
    return 0


def find_valid_obstruction_positions(grid, start_row, start_col):
    sum = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '.' and (r, c) != (start_row, start_col):
                grid[r][c] = '#'
                sum += simulate_guard(grid, start_row, start_col)
                grid[r][c] = '.' 

    return sum

def main():
    FILENAME = 'input.txt'
    grid = read_from_file(FILENAME)
    start_row, start_col = None, None

    # Locate the guard's starting position
    for r, row in enumerate(grid):
        if '^' in row:
            start_row, start_col = r, row.index('^')
            break

    if start_row is None or start_col is None:
        print("No starting position found.")
        return

    valid_positions = find_valid_obstruction_positions(grid, start_row, start_col)
    print(f"Number of valid obstruction positions: {valid_positions}")


if __name__ == "__main__":
    main()