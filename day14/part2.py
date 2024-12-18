# Answer: 6888

import re

WIDTH = 101
HEIGHT = 103
VERTICAL_MIDDLE = (HEIGHT - 1) // 2
HORIZONTAL_MIDDLE = (WIDTH - 1) // 2

robots = []
for line in open("input.txt"):
    robots.append(tuple(map(int, re.findall(r"-?\d+", line))))

def simulate(a):
    results = []
    for px, py, vx, vy in robots:
        results.append(((px + vx * a) % WIDTH, (py + vy * a) % HEIGHT))

    return results

def print_grid(results):
    grid = [[0] * WIDTH for _ in range(HEIGHT)]

    for px, py in results:
        grid[py][px] += 1

    for row in grid:
        new_row =['.' if cell == 0 else cell for cell in row]
        print(*new_row, sep="")

values = []
for i in range(10000):
    result = simulate(i)
    tl = tr = bl = br = 0
    for px, py in result:
        if px == HORIZONTAL_MIDDLE or py == VERTICAL_MIDDLE:
            continue
        if px < HORIZONTAL_MIDDLE:
            if py < VERTICAL_MIDDLE:
                tl += 1
            else:
                tr += 1
        else:
            if py < VERTICAL_MIDDLE:
                bl += 1
            else:
                br += 1

    values.append(tl * tr * bl * br)

# print_grid(simulate(values.index(min(values)))) # Use this to see christmas tree :)
print(values.index(min(values)))