# Stones with 0 gets replaced with a stone with 1

# Stones with an even number of digits get split into 2 and the left half of the digits are one the first stone and right half on the second stone
# Leading zeroes will be trimmed as well. E.g. 1000 stone splits into 10 stone and 0 stone. (Stone with 0 had the last 0 trimmed)

# If both rules don't apply, the number on the stone is multiplied by 2024

# Part2 requires 75 blinks instead of 25. Part1 solution is not efficient enough for that
# Instead of storing a list of all the values, using a counter will reduce the space complexity
# Memoization map here will stop redundant computation
# Answer: 257246536026785


def count(stone, steps, cache):
    if (stone, steps) in cache:
        return cache[(stone, steps)]
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1, cache)
    str_stone = str(stone)
    len_stone = len(str_stone)
    if len_stone % 2 == 0:
        result = count(int(str_stone[:len_stone // 2]), steps - 1, cache) \
            + count(int(str_stone[len_stone // 2:]), steps - 1, cache)
    else:
        result = count(stone * 2024, steps - 1, cache)

    cache[(stone, steps)] = result
    return result

if __name__ == "__main__":
    with open("input.txt") as file:
        stones = [int(x) for x in file.read().split()]
    cache = {}
    print(sum(count(stone, 75, cache) for stone in stones))
