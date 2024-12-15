# Answer: 1396562

from collections import deque

if __name__ == "__main__":
    grid = [list(line.strip()) for line in open("input.txt")]

    rows = len(grid)
    cols = len(grid[0])

    regions = []
    perimeters = []
    seen = set()

    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue
            seen.add((r, c))
            perimeter = 0
            region = {(r, c)}
            q = deque([(r, c)])
            crop = grid[r][c]
            while q:
                cr, cc = q.popleft()
                for nr, nc in [(cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)]:
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        perimeter += 1
                        continue
                    if grid[nr][nc] != crop:
                        perimeter += 1
                        continue
                    if (nr, nc) in region:
                        continue
                    region.add((nr, nc))
                    q.append((nr, nc))
            seen |= region
            regions.append(region)
            perimeters.append(perimeter)

    cost = 0
    for area, perimeter in zip(regions, perimeters):
        cost += len(area) * perimeter
    print(cost)
