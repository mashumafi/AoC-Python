from aoc import AdventOfCode, split, parse

aoc = AdventOfCode(year=2022, day=10)

@aoc(expected=13140)
def puzzle1(data: list[str]) -> str:
    """Solve puzle 1"""
    X = 1 # register
    strengths = []
    for line in data:
        if line.startswith("addx"):
            addx, num = parse(line.split(" "), [str, int])
            strengths += [X, X]
            X += num
        elif line.startswith("noop"):
            strengths += [X]

    interesting = [strengths[19] * 20] + [strengths[i-1] * i for i in range(60, len(strengths), 40)]
    return str(sum(interesting))

@aoc(expected=None)
def puzzle2(data: list[str]) -> str:
    """Solve puzle 2"""
    X = 1 # register
    strengths = []
    for line in data:
        if line.startswith("addx"):
            addx, num = parse(line.split(" "), [str, int])
            strengths += [X, X]
            X += num
        elif line.startswith("noop"):
            strengths += [X]


    for i in range(0, len(strengths), 40):
        row = strengths[i:i+40]
        pixels = set()
        for j, strength in enumerate(row):
            if j in [strength-1, strength, strength+1]:
                pixels.add(j)

        for i in range(40):
            if i in pixels:
                print("#", end="")
            else:
                print(".", end="")
        print()