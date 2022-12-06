from aoc import AdventOfCode

aoc = AdventOfCode(year=2021, day=7)

@aoc(expected=37)
def puzzle1(data: list[str]) -> str:
    """Solve puzle 1"""
    crabs = [int(crab) for crab in data[0].split(",")]
    lowest = 1_000_000_000
    for i in range(min(crabs), max(crabs) + 1):
        lowest = min(lowest, sum([abs(crab-i) for crab in crabs]))
    return str(lowest)

@aoc(expected=168)
def puzzle2(data: list[str]) -> str:
    """Solve puzle 2"""
    crabs = [int(crab) for crab in data[0].split(",")]
    lowest = 1_000_000_000
    for i in range(min(crabs), max(crabs) + 1):
        lowest = min(lowest, sum([sum(range(1, abs(crab-i)+1)) for crab in crabs]))
    return str(lowest)
