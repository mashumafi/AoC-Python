from aoc import AdventOfCode

aoc = AdventOfCode(year=2022, day=6)

@aoc(expected=7)
def puzzle1(data: list[str]) -> str:
    """Solve puzle 1"""
    for i, c in enumerate(data[0]):
        if len(set(data[0][i:i+4])) == 4:
            return str(i+4)
    return str()

@aoc(expected=19)
def puzzle2(data: list[str]) -> str:
    """Solve puzle 2"""
    for i, c in enumerate(data[0]):
        if len(set(data[0][i:i+14])) == 14:
            return str(i+14)
    return str()
