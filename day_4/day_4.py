def a(input):
    lines = open(input, "r").readlines()
    sol = 0
    for line in lines:
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


def b(input):
    lines = open(input, "r").readlines()
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        x, y = map(str.split, line.split("|"))
        n = len(set(x) & set(y))
        for j in range(i + 1, min(i + 1 + n, len(lines))):
            cards[j] += cards[i]

    return sum(cards)


print(f"sol a: {a('day_4/input.txt')} sol b: {b('day_4/input.txt')}")
