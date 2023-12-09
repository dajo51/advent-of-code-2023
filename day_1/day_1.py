def a(input: str) -> int:
    total = 0
    with open(input, "r") as f:
        for line in f:
            line = "".join(i for i in line.strip() if i.isdigit())
            line = line[0] + line[-1]
            if line:
                total += int(line)
    return total


def b(input: str) -> int:
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    total = 0
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            for word, digit in digits.items():
                if word in line:
                    line = line.replace(word, word[0] + str(digit) + word[-1])
            line = "".join(i for i in line if i.isdigit())
            line = line[0] + line[-1]
            if line:
                total += int(line)
    return total


print(f"part 1 sol:  {a('day_1/input.txt')} part 2 sol:  {b('day_1/input.txt')}")
