import re

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
    digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    total = 0
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            for word, digit in digits.items():
                if word in line:
                    print(line)
                    line = line.replace(word, str(digit))
                    print(line)
            line = ''.join(i for i in line if i.isdigit())
            print(line)
            # line = line[0] + line[-1]
            print(line)
            if line and len(line) > 1:
                line = line[0] + line[-1]
                total += int(line)
                print("total" + str(total))
        
    return total


# print(a("day_1/input.txt"))
# print(b("day_1/input.txt"))