def a(input: str) -> int:
    with open(input, "r") as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        line = ''.join(i for i in line.strip() if i.isdigit())
        line = line[0] + line[-1]
        if line:
            total += int(line)
    return total

print(a("day_1/input.txt"))