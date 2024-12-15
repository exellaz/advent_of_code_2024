# Answer: 1541

# Easy Solution. Same as part1 but removed the check for visited spots
# Inefficient but simpler to implement

from collections import deque

def score(grid, r, c):
    q = deque([(r, c)])
    trailends = 0
    while len(q) > 0:
        cr, cc = q.popleft()
        for nr, nc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                continue
            if grid[nr][nc] != grid[cr][cc] + 1:
                continue
            if grid[nr][nc] == 9:
                trailends += 1
            else:
                q.append((nr, nc))
    return trailends

if __name__ == "__main__":
	grid = [[int(char) for char in line.strip()] for line in open("input.txt")]
	rows = len(grid)
	cols = len(grid[0])

	trailheads = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]
	print(sum(score(grid, r, c) for r, c in trailheads))