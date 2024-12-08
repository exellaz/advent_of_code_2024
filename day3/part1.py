import re

def extract_valid_mul(string):
    pattern = r"mul\([0-9]+,[0-9]+\)"
    return re.findall(pattern, string)

def extract_num_from_mul(valid_mul):
    pattern = r"mul\((d+),(\d+)\)"
    match = re.match(pattern, valid_mul)
    if match:
        return int(match.group(1), int(match.group(2)))
    return 0, 0

sum = 0
with open("input.txt") as file:
    for line in file:
        valid_mul_list = extract_valid_mul(line)
        for valid_mul in valid_mul_list:
            num1, num2 = extract_num_from_mul(valid_mul)
            product = num1 * num2
            sum += product

print(sum)
