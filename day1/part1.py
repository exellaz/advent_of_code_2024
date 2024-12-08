# Answer: 2904518

left_col = []
right_col = []

with open("input.txt", encoding="utf-8") as file:
    for line in file:
        numbers = line.split()
        left_col.append(int(numbers[0]))
        right_col.append(int(numbers[1]))

left_col.sort()
right_col.sort()
sum = 0

for left_num, right_num in zip(left_col, right_col):
    difference = abs(left_num - right_num)
    sum += difference

print(sum)
