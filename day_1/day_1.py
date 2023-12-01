def a(input: str) -> int:
    total = 0
    with open(input, "r") as f:
        for line in f:
            line = ''.join(i for i in line.strip() if i.isdigit())
            line = line[0] + line[-1]
            if line:
                total += int(line)
    return total

def b(input: str) -> int:
    pass

print(a("day_1/input.txt"))