top, bottom = open("input.txt").read().split("\n\n")

grid = [list(line) for line in top]
moves = bottom.replace("\n", "")

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            break
    else:
        continue
    break

for move in moves:
    # dr = -1 if move == "^" else 1 if move == "v" else 0
    dr = {"^": -1, "v": 1}.get(move, 0)
    dc = {"<": -1, ">": 1}.get(move, 0)
    targets = [(r, c)]
    cr = r
    cc = c
    go = True
    while True:
        cr += dr
        cc += dc
        char = grid[cr][cc]
        if char == "#":
            go = False
            break
        if char == "0":
            targets.append((cr,cc))
        if char == ".":
            break

    if not go:
        continue
    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"
    for br, bc in targets[1:]:
        grid[br + dr][bc + dc] = "0"
    r += dr
    c += dc

# print(grid)
# print(moves)
for row in grid:
    print(*row, sep="")