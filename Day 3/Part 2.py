input = "Day 3/input.txt"

def remove_k_digits(s, k):
    stack = []
    for digit in s:
        while stack and stack[-1] < digit and k > 0:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k > 0 and stack:
        stack.pop()
        k -= 1
    return ''.join(stack)

with open(input, 'r') as file:
    banks = [line.strip() for line in file if line.strip()]

total_joltage = 0

for bank in banks:
    k = len(bank) - 12
    if k < 0:
        continue
    max_jolt_str = remove_k_digits(bank, k)
    jolt = int(max_jolt_str)
    total_joltage += jolt

print(total_joltage)
