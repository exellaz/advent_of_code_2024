#Anwer: 19927218456

# Mix: Bitwise XOR
# Prune: Modulo 16777216

def steps(num):
    num = (num ^ (num * 64) % 16777216) # Multiply by 64 then `mix` and `prune`
    num = (num ^ (num // 32) % 16777216) # Floor by 32 then `mix` and `prune`
    num = (num ^ (num * 2048) % 16777216) # Multiply by 2048 then `mix` and `prune`
    return num

total = 0

for line in open("input.txt"):
    num = int(line)
    for _ in range(2000):
        num = steps(num)
    total += num

print(total)