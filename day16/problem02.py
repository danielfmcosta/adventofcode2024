import heapq
# from collections import defaultdict

def parse_input(input_text):
    grid = [list(line) for line in input_text.strip().split('\n')]
    start, end = None, None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return grid, start, end

def dijkstra(grid, starts):
    delta = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}
    dist = {}
    pq = []
    for sr, sc, dir in starts:
        dist[(sr, sc, dir)] = 0
        heapq.heappush(pq, (0, sr, sc, dir))

    while pq:
        d, row, col, direction = heapq.heappop(pq)
        if dist[(row, col, direction)] < d:
            continue
        for next_dir in "EWNS".replace(direction, ""):
            if (row, col, next_dir) not in dist or dist[(row, col, next_dir)] > d + 1000:
                dist[(row, col, next_dir)] = d + 1000
                heapq.heappush(pq, (d + 1000, row, col, next_dir))
        dr, dc = delta[direction]
        next_row, next_col = row + dr, col + dc
        if (
            0 <= next_row < len(grid)
            and 0 <= next_col < len(grid[0])
            and grid[next_row][next_col] != "#"
            and (
                (next_row, next_col, direction) not in dist
                or dist[(next_row, next_col, direction)] > d + 1
            )
        ):
            dist[(next_row, next_col, direction)] = d + 1
            heapq.heappush(pq, (d + 1, next_row, next_col, direction))

    return dist

def best(grid_data):
    grid, (sr, sc), (er, ec) = grid_data
    dist = dijkstra(grid, [(sr, sc, "E")])
    best_cost = float("inf")
    for dir in "EWNS":
        if (er, ec, dir) in dist:
            best_cost = min(best_cost, dist[(er, ec, dir)])
    return best_cost

# Parse input and process
with open("input.txt", "r") as f:
    s = f.read().strip()

grid, (sr, sc), (er, ec) = parse_input(s)

from_start = dijkstra(grid, [(sr, sc, "E")])
from_end = dijkstra(grid, [(er, ec, d) for d in "EWNS"])

optimal_cost = best((grid, (sr, sc), (er, ec)))

flip = {"E": "W", "W": "E", "N": "S", "S": "N"}
result = set()
for row in range(len(grid)):
    for col in range(len(grid[0])):
        for dir in "EWNS":
            state_from_start = (row, col, dir)
            state_from_end = (row, col, flip[dir])
            if state_from_start in from_start and state_from_end in from_end:
                if from_start[state_from_start] + from_end[state_from_end] == optimal_cost:
                    result.add((row, col))

print(len(result))




# def is_valid_position(grid, x, y):
#     return 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] != '#'

# def calculate_distance(pos1, pos2):
#     x1, y1 = pos1
#     x2, y2 = pos2
#     return abs(x1 - x2) + abs(y1 - y2)

# def rotation_cost(current_dir, new_dir):
#     if current_dir == new_dir:
#         return 0  
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     current_index = directions.index(current_dir)
#     new_index = directions.index(new_dir)
#     rotation_steps = min(abs(new_index - current_index), 4 - abs(new_index - current_index))
#     return rotation_steps * 1000  

# def reconstruct_all_paths(came_from, end_state):
#     def dfs(state, path):
#         if state not in came_from:
#             all_paths.append(path[::-1])  
#             return
#         for previous in came_from[state]:
#             dfs(previous, path + [state[:2]])  

#     all_paths = []
#     dfs(end_state, [end_state[:2]]) 
#     return all_paths

# def a_star_find_all_paths(grid, start_pos, end_pos):
#     open_set = []
#     start_dir = (1, 0)  
#     heapq.heappush(open_set, (0, (start_pos[0], start_pos[1], start_dir)))  
    
#     came_from = defaultdict(list)  
#     g_score = defaultdict(lambda: float('inf'))
#     g_score[(start_pos[0], start_pos[1], start_dir)] = 0
    
#     best_cost = float('inf')
#     best_end_states = []
    
#     while open_set:
#         current_cost, current = heapq.heappop(open_set)
#         x, y, current_dir = current
        
#         if current_cost > best_cost:
#             continue
        
#         if (x, y) == end_pos:
#             if current_cost < best_cost:
#                 best_cost = current_cost
#                 best_end_states = [current]
#             elif current_cost == best_cost:
#                 best_end_states.append(current)
#             continue
        
#         for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  
#             neighbor = (x + dx, y + dy)
#             new_dir = (dx, dy)
            
#             if is_valid_position(grid, neighbor[0], neighbor[1]):
#                 move_cost = 1
#                 turn_cost = rotation_cost(current_dir, new_dir)
#                 tentative_g_score = g_score[current] + move_cost + turn_cost
                
#                 neighbor_state = (neighbor[0], neighbor[1], new_dir)
#                 if tentative_g_score <= g_score[neighbor_state]:
#                     if tentative_g_score < g_score[neighbor_state]:
#                         g_score[neighbor_state] = tentative_g_score
#                         heapq.heappush(open_set, (tentative_g_score, neighbor_state))
#                     if current not in came_from[neighbor_state]:
#                         came_from[neighbor_state].append(current)  
    
#     all_best_paths = []
#     for end_state in best_end_states:
#         all_best_paths.extend(reconstruct_all_paths(came_from, end_state))
    
#     return all_best_paths, best_cost

# def add_places_to_sit(grid, paths, start_pos, end_pos):
#     marked_positions = set()
#     x, y = start_pos
#     marked_positions.add((x, y))
#     x, y = end_pos
#     marked_positions.add((x, y))
    
#     for path in paths:
#         for x, y in path:
#             marked_positions.add((x, y))
    
#     for y, row in enumerate(grid):
#         for x, cell in enumerate(row):
#             if (x, y) in marked_positions and grid[y][x] != '#':
#                 grid[y][x] = 'O'
#     return grid

# def print_grid(grid):
#     for row in grid:
#         print(''.join(row))

# def count_sitting_places(grid):
#     return sum(row.count('O') for row in grid)

# with open('input.txt', 'r') as f:
#     s = f.read().strip()

# grid, start_pos, end_pos = parse_input(s)

# paths, total_score = a_star_find_all_paths(grid, start_pos, end_pos)

# print(total_score)

# print(len(paths))


# n_grid = add_places_to_sit(grid, paths, start_pos, end_pos)

# print_grid(n_grid)
# print(count_sitting_places(n_grid))