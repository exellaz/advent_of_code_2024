# Answer: 5955

def is_ordered(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in cache and not cache[key]:
                return False
    return True

if __name__ == "__main__":
    file = open("input.txt")
    rules = []

    for line in file:
        if line.isspace():
            break
        rules.append(list(map(int, line.split("|"))))

    cache = {}
    for x, y in rules:
        cache[(x, y)] = True
        cache[(y, x)] = False

    total_sum = 0
    for line in file:
        update = list(map(int, line.split(",")))
        if (is_ordered(update)):
            total_sum += update[len(update) // 2]

    print(total_sum)

