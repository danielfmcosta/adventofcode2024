def read_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def different_frequencies(grid):
    freqs = []
    for r, row in enumerate(grid):
        grid[r] = row.split('.')
    for row in grid:
        for col in row:
            if col not in freqs and col != '':
                freqs.append(col)
    return freqs    

def resonant_frequency(grid, vector, position):
    pos_res_freq = (position[0] + vector[0], position[1] + vector[1])
    pos_res_freqs = []
    while not (pos_res_freq[0] < 0 or pos_res_freq[1] < 0 or pos_res_freq[0] >= len(grid) or pos_res_freq[1] >= len(grid[0])):
        if grid[pos_res_freq[0]][pos_res_freq[1]] == '.':
            grid[pos_res_freq[0]][pos_res_freq[1]] = '#'
        pos_res_freqs.append(pos_res_freq)
        pos_res_freq = (pos_res_freq[0] + vector[0], pos_res_freq[1] + vector[1])
    return pos_res_freqs

def calculate_vector(grid, positions):
    pos_res_freq = []
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i != j:
                vector = (positions[j][0] - positions[i][0], positions[j][1] - positions[i][1])
                pos_res_freq += resonant_frequency(grid, vector, positions[j])
    return pos_res_freq

def freq_positions(grid, freq):
    positions = []
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == freq:
                positions.append((r, c))
    return positions

def main():
    FILENAME = 'input.txt'
    grid = [list(row) for row in read_from_file(FILENAME)]  
    freqs = different_frequencies(["".join(row) for row in grid])  
    all_pos_res_freq = set() 

    for freq in freqs:
        positions = freq_positions(grid, freq)
        
        all_pos_res_freq.update(positions)
        
        pos_res_freq = calculate_vector(grid, positions)
        all_pos_res_freq.update(pos_res_freq)  

    print("\n".join("".join(row) for row in grid)) 
    print(len(all_pos_res_freq))  
if __name__ == "__main__":
    main()
