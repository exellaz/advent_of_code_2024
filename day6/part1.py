# Answer: 4433

if __name__ == "__main__":
    grid = list(map(list, open("input.txt").read().splitlines()))

    rows = len(grid)
    cols = len(grid[0])

    # Find the initial position of the guard
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "^":
                break
        else:
            continue
        break

    row_offset = -1 # Offset based on the initial position and orientation
    col_offset = 0

    seen = {(row, col)} # Store each position in a set to ensure they are all unique
    while True:
        seen.add((row, col))
        if row + row_offset < 0 or row + row_offset >= rows \
            or col + col_offset < 0 or col + col_offset >= cols:
            break
        if grid[row + row_offset][col + col_offset] == "#":
            row_offset, col_offset = col_offset, -row_offset # Changes the orientation of the guard when it encounters obstacles
        else:
            row += row_offset
            col += col_offset

    print(len(seen))