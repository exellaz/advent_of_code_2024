# Answer: 2532

def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    xmas = "XMAS"
    matches = 0
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                match = True
                for i in range(4):
                    r, c = row + i * dr, col + i * dc
                    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != xmas[i]:
                        match = False
                        break
                if match:
                    matches += 1

    return matches

if __name__ == "__main__":
    input = []
    with open("input.txt") as file:
            for line in file:
                    input.append(line)

    grid = [list(row.strip()) for row in input]

    matches = find_xmas(grid)
    print(matches)

