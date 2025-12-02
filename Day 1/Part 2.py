def part2(input):
    position = 50
    Zeros = 0

    with open(input, "r") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            if direction == "R":
                Zeros += (position + distance) // 100
                position = (position + distance) % 100

            else:
                if position == 0:
                    Zeros += distance // 100
                else:
                    if distance >= position:
                        Zeros += (distance - position) // 100 + 1

                position = (position - distance) % 100

    return Zeros


if __name__ == "__main__":
    result = part2("Day 1/input.txt")
    print("Part 2 Password:", result)
