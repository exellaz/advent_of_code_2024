# Stones with 0 gets replaced with a stone with 1

# Stones with an even number of digits get split into 2 and the left half of the digits are one the first stone and right half on the second stone
# Leading zeroes will be trimmed as well. E.g. 1000 stone splits into 10 stone and 0 stone. (Stone with 0 had the last 0 trimmed)

# If both rules don't apply, the number on the stone is multiplied by 2024

# Answer: 217443

if __name__ == "__main__":
    with open("input.txt") as file:
        stones = [int(x) for x in file.read().split()]

    for _ in range(25):
        output = []
        for stone in stones:
            if stone == 0:
                output.append(1)
                continue
            str_stone = str(stone)
            len_stone = len(str_stone)
            if len_stone % 2 == 0:
                output.append(int(str_stone[:len_stone // 2]))
                output.append(int(str_stone[len_stone // 2:]))
            else:
                output.append(stone * 2024)
        stones = output

    print(len(stones))