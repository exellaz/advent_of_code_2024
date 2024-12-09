# Answer: 83595109

import re

if __name__ == "__main__":
    total_sum = 0
    instruction_enabled = True
    with open("input.txt") as file:
        for line in file:
            expr_list = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
            for expr in expr_list:
                if expr == "do()":
                    instruction_enabled = True
                    continue
                elif expr == "don't()":
                    instruction_enabled = False
                    continue

                if instruction_enabled:
                    nums = re.findall(r"\d+", expr)
                    product = int(nums[0]) * int(nums[1])
                    total_sum += product

    print(total_sum)
