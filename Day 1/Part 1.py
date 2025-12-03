def part1(input):
    position = 50
    zeros = 0

    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            if direction == 'L':
                position = (position - distance) % 100
            else:
                position = (position + distance) % 100

            if position == 0:
                zeros += 1

    return zeros

if __name__ == "__main__":
    input = "Day 1/input.txt"
    result = part1(input)
    print("Password:", result)

