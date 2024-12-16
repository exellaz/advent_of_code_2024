# Answer: 106228669504887

import re

cost = 0
for machine in open("input.txt").read().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", machine))
    px += 10000000000000
    py += 10000000000000
    a_count = (px * by - py * bx) / (ax * by - ay * bx)
    b_count = (px - ax * a_count) / bx
    if a_count % 1 == b_count % 1 == 0:
        cost += int(a_count * 3 + b_count)
print(cost)

