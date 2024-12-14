def read_map(filename):
    """Read the topographic map from the input file."""
    with open(filename, 'r') as f:
        return [[int(char) for char in line.strip()] for line in f]

def find_trailheads(topo_map):
    trailheads = []
    for y in range(len(topo_map)):
        for x in range(len(topo_map[y])):
            if topo_map[y][x] == 0:
                trailheads.append((x, y))
    return trailheads

def dfs_paths(topo_map, pos, path, visited, all_paths):
    x, y = pos
    visited.add(pos)
    path.append(pos)

    if topo_map[y][x] == 9:
        all_paths.add(tuple(path)) 
    else:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(topo_map[0]) and 0 <= ny < len(topo_map) and topo_map[ny][nx] == topo_map[y][x] + 1 and (nx, ny) not in visited):  
                dfs_paths(topo_map, (nx, ny), path, visited, all_paths)

    path.pop()
    visited.remove(pos)

def calculate_paths(topo_map, trailheads):
    total_paths = 0
    for trailhead in trailheads:
        all_paths = set()  
        dfs_paths(topo_map, trailhead, [], set(), all_paths)
        total_paths += len(all_paths)  
        print(f"Trailhead {trailhead} has {len(all_paths)} distinct paths.")

    return total_paths

def main():
    topo_map = read_map('input.txt')
    trailheads = find_trailheads(topo_map)
    total_paths = calculate_paths(topo_map, trailheads)
    print(f"Total distinct paths: {total_paths}")

if __name__ == "__main__":
    main()
