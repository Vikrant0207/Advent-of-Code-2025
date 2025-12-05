with open('Day 5/input.txt') as f:
    lines = f.read().strip().split('\n')

ranges = []
i = 0
while i < len(lines) and lines[i] != '':
    start, end = map(int, lines[i].split('-'))
    ranges.append((start, end))
    i += 1

# Sort ranges by start
ranges.sort()

# Merge overlapping ranges
merged = []
for start, end in ranges:
    if not merged or merged[-1][1] + 1 < start:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

# Calculate total unique IDs
total = 0
for start, end in merged:
    total += end - start + 1

print(total)
