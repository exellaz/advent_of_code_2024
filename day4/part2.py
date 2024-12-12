# Answer: 1941

if __name__ == "__main__":
    grid = open("input.txt").read().splitlines()

    matches = 0

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] != "A":
                continue
            corners = grid[row - 1][col - 1], grid[row - 1][col + 1] \
                    ,grid[row + 1][col + 1], grid[row + 1][col - 1]
            if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                matches += 1

    print(matches)