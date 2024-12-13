def traverse(grid, row, col):
    row_offset = -1 # Offset based on the initial position and orientation
    col_offset = 0

    grid[row][col] = "X"
    while True:
        grid[row][col] = "X"
        if row + row_offset < 0 or row + row_offset >= rows \
            or col + col_offset < 0 or col + col_offset >= cols:
            break
        if grid[row + row_offset][col + col_offset] == "#":
            row_offset, col_offset = col_offset, -row_offset # Changes the orientation of the guard when it encounters obstacles
        else:
            row += row_offset
            col += col_offset

def simulate(grid, row, col, initial_row, initial_col):
    row_offset, col_offset = -1, 0  # Starting direction (up)
    seen_states = set()  # To track visited states (position + direction)

    while True:
        # Saves the current state
        state = (row, col, row_offset, col_offset)
        if state in seen_states:
            return True  # Loop detected
        seen_states.add(state)

        if row + row_offset < 0 or row + row_offset >= rows \
                or col + col_offset < 0 or col + col_offset >= cols:
            break

        if grid[row + row_offset][col + col_offset] == "#":
            row_offset, col_offset = col_offset, -row_offset
        else:
            row += row_offset
            col += col_offset

        # If back at the starting position and orientation
        if (row, col) == (initial_row, initial_col) and (row_offset, col_offset) == (-1, 0):
            return True

    return False

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

    initial_row, initial_col = row, col
    loop_positions = []

    traverse(grid, initial_row, initial_col)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "X":
                grid[row][col] = "#"

                if simulate(grid, initial_row, initial_col, initial_row, initial_col):
                    loop_positions.append((row, col))

                grid[row][col] = "X"

    print(len(loop_positions))
