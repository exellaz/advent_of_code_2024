# Answer: 6420913943576

if __name__ == "__main__":
    line = open("input.txt").readline().strip()
    files = {}
    free_space = []
    id = 0
    pos = 0

    for i, char in enumerate(line):
        x = int(char)
        if i % 2 == 0:
            files[id] = (pos, x)
            id += 1
        else:
            if x != 0:
                free_space.append((pos, x))
        pos += x

    while id > 0:
        id -= 1
        pos, size = files[id]
        for i, (start, len) in enumerate(free_space):
            if start >= pos:
                free_space = free_space[:i]
                break
            if size <= len:
                files[id] = (start, size)
                if size == len:
                    free_space.pop(i)
                else:
                    free_space[i] = (start + size, len - size)
                break

    total = 0
    for id, (pos, size) in files.items():
        for x in range(pos, pos + size):
            total += id * x
    print(total)