def Total_Joltage(input):
    total_joltage = 0
    with open(input, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    for line in lines:
        digits = [int(ch) for ch in line if ch.isdigit()]
        n = len(digits)
        if n < 2:
            continue

        suffix_max = [0] * n
        suffix_max[-1] = -1
        for i in range(n - 2, -1, -1):
            if i == n - 2:
                suffix_max[i] = digits[i + 1]
            else:
                suffix_max[i] = max(digits[i + 1], suffix_max[i + 1])

        max_jolt = 0
        for i in range(n - 1):
            max_right = suffix_max[i]
            jolt = digits[i] * 10 + max_right
            if jolt > max_jolt:
                max_jolt = jolt

        total_joltage += max_jolt

    return total_joltage

if __name__ == "__main__":
    input = "Day 3/input.txt"
    print(Total_Joltage(input))
