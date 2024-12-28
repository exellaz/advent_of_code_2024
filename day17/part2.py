# Answer: 37221274271220

import re

program = list(map(int, re.findall(r"\d+", open("input.txt").read())[3:]))

# print(program)
def find(program, ans):
    if program == []:
        return ans
    for x in range(8):
        a = ans << 3 | x
        b = a % 8
        b = b ^ 2
        c = a >> b
        b = b ^ c
        b = b ^ 3
        if b % 8 == program[-1]:
            sub = find(program[:-1], a)
            if sub is None:
                continue
            return sub

print(find(program, 0))