# Answer: 1411

from collections import deque

grid = [list(line.strip()) for line in open("input.txt")]

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            break
    else:
        continue
    break

distances = [[-1] * cols for _ in range(rows)]
distances[r][c] = 0

while grid[r][c] != "E":
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
            continue
        if grid[nr][nc] == "#":
            continue
        if distances[nr][nc] != -1:
            continue
        distances[nr][nc] = distances[r][c] + 1
        r = nr
        c = nc

count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "#":
            continue
        for nr, nc in [(r + 2, c), (r + 1, c + 1), (r, c + 2), (r - 1, c + 1)]:
            if nr < 0 or nc < 0 or nr >= rows or nc >= rows:
                continue
            if grid[nr][nc] == "#":
                continue
            if abs(distances[r][c] - distances[nr][nc]) >= 102:
                count += 1

print(count)