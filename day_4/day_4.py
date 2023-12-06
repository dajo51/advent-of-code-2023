def a(input):
    with open(input) as f:
        sol = 0
        for line in f:
            points = 1
            numbers = line.strip().split(": ")[1]
            win = set([i for i in numbers.split("|")[0].split(" ") if i.isdigit()])
            game = set([i for i in numbers.split("|")[1].split(" ") if i.isdigit()])
            wins = len(win.intersection(game))
            if wins:
                for i in range(wins - 1):
                    points = points * 2
                sol += points

    return sol


print(a("day_4/input.txt"))
