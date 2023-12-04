def a(input):
    sol_dict = {"red": 12, "green": 13, "blue": 14}
    sol_max = 39
    sol = 0

    with open(input, "r") as f:
        for line in f:

            game_id = int("".join([s for s in line.split(":")[0] if s.isdigit()]))

            sets = line.strip().split(";")
            sets[0] = "".join(sets[0].split(":")[1:])
            g_possible = True

            for set in sets:
                cubes = set.strip().split(",")
                cubes = [[int(item.strip().split(" ")[0]), item.strip().split(" ")[1]] for item in cubes]
                if sum(i[0] for i in cubes) > sol_max:
                    g_possible = False
                    break
                for pair in cubes:
                    for key, val in sol_dict.items():
                        if key in pair and val < pair[0]:
                            g_possible = False
                            break
            if g_possible:
                sol += game_id
        
    return sol


def b(input):
    sol_dict = {"red": 12, "green": 13, "blue": 14}
    sol = 0

    with open(input, "r") as f:
        for line in f:
            game_id = int("".join([s for s in line.split(":")[0] if s.isdigit()]))
            sets = line.strip().split(";")
            sets[0] = "".join(sets[0].split(":")[1:])
            green_min = 0
            red_min = 0
            blue_min = 0

            for set in sets:
                cubes = set.strip().split(",")
                cubes = [[int(item.strip().split(" ")[0]), item.strip().split(" ")[1]] for item in cubes]
                for pair in cubes:
                    for key, val in sol_dict.items():
                        if key in pair:
                            if key == "red":
                                red_min = max(red_min, pair[0])
                            if key == "green":
                                green_min = max(green_min, pair[0])
                            if key == "blue":
                                blue_min = max(blue_min, pair[0])
            sol += red_min * green_min * blue_min
        
    return sol

print(a("day_2/input.txt"))
print(b("day_2/input.txt"))