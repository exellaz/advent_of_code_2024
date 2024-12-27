#Anwer: 2189

# Mix: Bitwise XOR
# Prune: Modulo 16777216

def steps(num):
    num = (num ^ (num * 64) % 16777216) # Multiply by 64 then `mix` and `prune`
    num = (num ^ (num // 32) % 16777216) # Floor by 32 then `mix` and `prune`
    num = (num ^ (num * 2048) % 16777216) # Multiply by 2048 then `mix` and `prune`
    return num

seq_to_total = {}

for line in open("input.txt"):
    num = int(line)
    buyer = [num % 10]
    for _ in range(2000):
        num = steps(num)
        buyer.append(num % 10)

    seen = set()
    for i in range(len(buyer) - 4): # Loop until the number of digits that allows a valid sequence
        a, b, c, d, e = buyer[i:i + 5] # Get the current 5 values
        seq = (b - a, c - b, d - c, e - d) # Get the sequence in those 5 values
        if seq in seen:
            continue
        seen.add(seq)
        if seq not in seq_to_total:
            seq_to_total[seq] = 0 # Add this sequence into the set
        seq_to_total[seq] += e # Add the number of bananas bought if the sequence is seen

print(max(seq_to_total.values()))