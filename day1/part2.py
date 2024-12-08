# Answer: 18650129

left_col = []
right_col = []

with open("input.txt", encoding="utf-8") as file:
    for line in file:
        numbers = line.split()
        left_col.append(int(numbers[0]))
        right_col.append(int(numbers[1]))

map = {}
similarity_score = 0

for right_num in right_col:
    if right_num in map:
        map[right_num] += 1
    else:
        map[right_num] = 1

for left_num in left_col:
    if left_num in map:
        product = left_num * map[left_num]
    else:
        product = 0
    similarity_score += product

print(similarity_score)
