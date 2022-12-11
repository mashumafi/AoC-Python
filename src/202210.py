from aoc import AdventOfCode, split, parse

aoc = AdventOfCode(year=2022, day=10)

def compute_strengths(data: list[str]) -> list[int]:
    X = 1 # register
    strengths = []
    for line in data:
        if line.startswith("addx"):
            addx, num = parse(line.split(" "), [str, int])
            strengths += [X, X]
            X += num
        elif line.startswith("noop"):
            strengths += [X]

    return strengths

@aoc(expected=13140)
def puzzle1(data: list[str]) -> str:
    """Solve puzle 1"""
    strengths = compute_strengths(data)

    interesting = [strengths[i] * (i+1) for i in range(19, len(strengths), 40)]
    return str(sum(interesting))

@aoc(expected=None)
def puzzle2(data: list[str]) -> str:
    """Solve puzle 2"""
    strengths = compute_strengths(data)

    for i in range(0, len(strengths), 40):
        print("".join([
            "#" if strength-1 <= j <= strength+1 else " "
            for j, strength in enumerate(strengths[i:i+40])
        ]))
