# Answer: 1352

def find_antennas(antennas):
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != ".":
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((r, c))

def find_antinodes(antinodes):
    for array in antennas.values():
        for i in range(len(array)):
            for j in range(len(array)):
                if i == j:
                    continue
                r1, c1 = array[i]
                r2, c2 = array[j]
                dr = r2 - r1
                dc = c2 - c1
                r = r1
                c = c1
                while 0 <= r < rows and 0 <= c < cols:
                    antinodes.add((r, c))
                    r += dr
                    c += dc

if __name__ == "__main__":
    grid = list(line.strip() for line in open("input.txt"))
    rows = len(grid)
    cols = len(grid[0])

    antennas = {}
    find_antennas(antennas)
    antinodes = set()
    find_antinodes(antinodes)
print(len(antinodes))