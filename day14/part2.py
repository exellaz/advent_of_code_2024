# Grid is 101 x 103

import re

WIDTH = 101
HEIGHT = 103
VERTICAL_MIDDLE = (HEIGHT - 1) // 2
HORIZONTAL_MIDDLE = (WIDTH - 1) // 2

robots = []

for line in open("input.txt"):
    robots.append(tuple(map(int, re.findall(r"-?\d+", line))))

results = []

for px, py, vx, vy in robots:
    results.append(((px + vx * 100) % WIDTH, (py + vy * 100) % HEIGHT))


tl = tr = bl = br = 0
for px, py in results:
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

print(tl * tr * bl * br)