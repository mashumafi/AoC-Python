from aoc import AdventOfCode

aoc = AdventOfCode(year=2021, day=8)

@aoc(expected=26)
def puzzle1(data: list[str]) -> str:
    """Solve puzle 1"""
    count = 0
    for line in data:
        signals, patterns = line.split("|")
        signals = [set(signal.strip()) for signal in signals.strip().split(" ")]
        patterns = [set(pattern.strip()) for pattern in patterns.strip().split(" ")]

        count += len([pattern for pattern in patterns if len(pattern) in [2, 3, 4, 7]])
    return str(count)

@aoc(expected=61229)
def puzzle2(data: list[str]) -> str:
    """Solve puzle 2"""
    return str()
