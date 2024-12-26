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
# q = deque[(r, c)]

# while q:
#     cr, cc = q.popleft()
#     for nr, nc in [(cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)]:
#         if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
#             continue
#         if grid[nr][nc] == "#":
#             continue
#         if distances[nr][nc] != -1:
#             continue
#         distances[nr][nc] = distances[cr][cc] + 1
#         q.append((nr, nc))

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
