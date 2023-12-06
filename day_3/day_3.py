import re


def a(input: str) -> int:
    sol = 0
    lines_matrix = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            lines_matrix.append(line)

    numbers_list = []
    counter = 0

    for line in lines_matrix:
        numbers = {}
        for match in re.finditer(r"\b\d+\b", line):
            number = match.group()
            positions = (match.start(), match.end())
            numbers[number] = positions
        print(numbers)

        for num, pos in numbers.items():
            l = lines_matrix[pos[0] - 1]
            r = lines_matrix[pos[1] + 1]
            if not l.isdigit() or l == "." or not r.isdigit() or r == ".":
                print(number)

        #     right = numbers[number][1] + 1
        #     if not (line[right].isdigit() or line[right] == "."):
        #         print(number)

        numbers_list.append(counter)
        numbers_list.append(numbers)

        counter *= 1

    # is_number = False
    # for line in range(1, len(lines_matrix) - 1):
    #     for char in range(1, len(lines_matrix[line]) - 1):
    #         if lines_matrix[line][char].isdigit():
    #             is_number = True
    #             if (
    #                 lines_matrix[line][char - 1] != "."
    #                 or lines_matrix[line][char + 1] != "."
    #                 or lines_matrix[line - 1][char - 1] != "."
    #                 or lines_matrix[line - 1][char + 1] != "."
    #                 or lines_matrix[line + 1][char - 1] != "."
    #                 or lines_matrix[line + 1][char + 1] != "."
    #             ):
    #                 print(num_str)
    #                 if is_number:
    #                     num_str += lines_matrix[line][char]
    #     else:
    #         sol += int(num_str)
    #         num_str = ""
    #         is_number = False
    return sol


print(a("day_3/input.txt"))
