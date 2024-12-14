# Answer: 376

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
            for j in range(i + 1, len(array)):
                r1, c1 = array[i]
                r2, c2 = array[j]
                antinodes.add((2 * r1 - r2, 2 * c1 - c2))
                antinodes.add((2 * r2 - r1, 2 * c2 - c1))

if __name__ == "__main__":
    grid = list(line.strip() for line in open("input.txt"))
    rows = len(grid)
    cols = len(grid[0])

    antennas = {}
    find_antennas(antennas)
    antinodes = set()
    find_antinodes(antinodes)
    print(len([0 for r, c in antinodes if 0 <= r < rows and 0 <= c < cols])) # Prints only the antinodes within the map