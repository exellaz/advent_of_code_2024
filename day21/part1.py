# Answer: 105458

from collections import Counter

def build_grid(keys):
    return {c: (i % 3, i // 3) for i, c in enumerate(keys)}

def steps(grid, seq, weight):
    px, py = grid["A"]
    bx, by = grid[" "]
    result = Counter()
    for instruction in seq:
        npx, npy = grid[instruction]
        block = (npx == bx and py == by) or (npy == by and px == bx)
        result[(npx - px, npy - py, block)] += weight
        px, py = npx, npy
    return result

def get_complexity(codes, n, keypad, dirpad):
    total = 0
    for code in codes:
        res = steps(keypad, code, 1)
        for _ in range(n + 1):
            new_res = Counter()
            for (x, y, block), count in res.items():
                seq = ("<" * -x + "v" * y + "^" * -y + ">" * x)[::-1 if block else 1] + "A"
                new_res += steps(dirpad, seq, count)
            res = new_res
        total += res.total() * int(code[:3])
    return total

codes = open("input.txt").read().split("\n")
keypad = build_grid("789456123 0A")
dirpad = build_grid(" ^A<v>")
print(get_complexity(codes, 2, keypad, dirpad))