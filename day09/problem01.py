def read_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def layout(files, free_space):
    print("layout")
    length = len(files)
    layout_files = []
    for i in range(length):
        file_count = int(files[i])
        free_space_count = int(free_space[i])

        layout_files.extend([i] * file_count)

        layout_files.extend(['.'] * free_space_count)

    return layout_files

def separate_string(line):
    if len(line) % 2 != 0:
        line += "0" 

    files = []
    free_space = []
    for i in range(len(line)):
        if i % 2 == 0:
            files.append(line[i])
        else:
            free_space.append(line[i])
    return files, free_space

def order_layout_files(layout_files):
    print("ordering layout")
    while '.' in layout_files:
        dot_index = layout_files.index('.') 
        for i in range(len(layout_files)-1, dot_index + 1, -1):
            if layout_files[i] != '.':
                layout_files[dot_index], layout_files[i] = layout_files[i], '.'
                break
        else:
            break
    return layout_files

def filesystem_checksum(layout_files):
    print("checksum")
    checksum = 0
    for position, block in enumerate(layout_files):
        if block != '.': 
            checksum += position * int(block)
    return checksum

def main():
    FILENAME = 'input.txt'
    line = "".join(read_from_file(FILENAME))
    files, free_space = separate_string(line)
    layout_files = layout(files, free_space)

    sorted_layout_files = order_layout_files(layout_files)


    checksum = filesystem_checksum(sorted_layout_files)

    print("Filesystem Checksum:", checksum)

if __name__ == "__main__":
    main()
