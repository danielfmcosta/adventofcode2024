import heapq

def improve_readability(input_text):
    grid = [list(line) for line in input_text.strip().split('\n')]
    return grid

def find_start(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                return (x, y)

def find_end(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'E':
                return (x, y)

def is_valid_position(grid, x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] != '#'

def calculate_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)

def rotation_cost(current_dir, new_dir):
    if current_dir == new_dir:
        return 0  
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    current_dir_index = directions.index(current_dir)
    new_dir_index = directions.index(new_dir)
    rotation_steps = min(abs(new_dir_index - current_dir_index), 4 - abs(new_dir_index - current_dir_index))
    return rotation_steps * 1000  

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current[:2])  # direction in reconstruction not needed
        current = came_from[current]
    path.reverse()
    return path

def a_star_with_rotations(grid, start_pos, end_pos):
    open_set = []
    start_dir = (1, 0) 
    heapq.heappush(open_set, (0, (start_pos[0], start_pos[1], start_dir)))  
    
    came_from = {}  
    g_score = {(start_pos[0], start_pos[1], start_dir): 0}
    f_score = {(start_pos[0], start_pos[1], start_dir): calculate_distance(start_pos, end_pos)}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        x, y, current_dir = current
        
        if (x, y) == end_pos:
            path = reconstruct_path(came_from, current)
            return path, g_score[current]
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]: 
            neighbor = (x + dx, y + dy)
            new_dir = (dx, dy)
            
            if is_valid_position(grid, neighbor[0], neighbor[1]):
                move_cost = 1
                turn_cost = rotation_cost(current_dir, new_dir)
                tentative_g_score = g_score[current] + move_cost + turn_cost
                neighbor_state = (neighbor[0], neighbor[1], new_dir)
                if neighbor_state not in g_score or tentative_g_score < g_score[neighbor_state]:
                    came_from[neighbor_state] = current
                    g_score[neighbor_state] = tentative_g_score
                    f_score[neighbor_state] = tentative_g_score + calculate_distance(neighbor, end_pos)
                    heapq.heappush(open_set, (f_score[neighbor_state], neighbor_state))
    
    return None, None 

with open('input.txt', 'r') as f:
    s = f.read().strip()

grid = improve_readability(s)

start_pos = find_start(grid)
end_pos = find_end(grid)

path, total_score = a_star_with_rotations(grid, start_pos, end_pos)
print(path)
print(total_score)