# Answer: 6382875730645

if __name__ == "__main__":
    line = open("input.txt").readline().strip()
    disk = []
    id = 0

    for i, char in enumerate(line):
        x = int(char)
        if i % 2 == 0:
            disk += [id] * x
            id += 1
        else:
            disk += ["."] * x

    free_space = [i for i, val in enumerate(disk) if val == '.']

    for i in free_space:
        while disk[-1] == ".":
            disk.pop()
        if len(disk) <= i:
            break
        disk[i] = disk.pop()

    print(sum(i * x for i, x in enumerate(disk)))