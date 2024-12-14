def read_map(filename):
    with open(filename, 'r') as f:
        return [[int(char) for char in line.strip()] for line in f]

def find_starts(topo_map):
    trailheads = []
    for y in range(len(topo_map)):
        for x in range(len(topo_map[y])):
            if topo_map[y][x] == 0:
                trailheads.append((x, y))
    return trailheads

def dfs_search(topo_map, pos, visited):
    stack = [pos]
    reachable_nines = set()

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if topo_map[y][x] == 9:
            reachable_nines.add((x, y))
            continue


        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(topo_map[0]) and 0 <= ny < len(topo_map): 
                if topo_map[ny][nx] == topo_map[y][x] + 1: 
                    stack.append((nx, ny))

    return reachable_nines

def calculate_scores(topo_map, start_positions):
    total_score = 0
    for start_pos in start_positions:
        visited = set()
        reachable_nines = dfs_search(topo_map, start_pos, visited)
        score = len(reachable_nines)
        total_score += score
    return total_score

def main():
    topo_map = read_map('input.txt')
    start_positions = find_starts(topo_map)
    total_score = calculate_scores(topo_map, start_positions)
    print(f"Total score: {total_score}")

if __name__ == "__main__":
    main()
