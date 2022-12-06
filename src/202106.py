from aoc import AdventOfCode

aoc = AdventOfCode(year=2021, day=6)

@aoc(expected=5934)
def puzzle1(data: list[str]) -> str:
    """Solve puzle 1"""
    timers = [int(timer) for timer in data[0].split(",")]

    for i in range(80):
        timers = [timer-1 for timer in timers]
        spawn = [timer for timer in timers if timer < 0]
        timers += [8 for i in range(len(spawn))]
        timers = [6 if timer < 0 else timer for timer in timers]

    return str(len(timers))

@aoc(expected=26984457539)
def puzzle2(data: list[str]) -> str:
    """Solve puzle 2"""
    timers = [int(timer) for timer in data[0].split(",")]
    fish = [timers.count(i) for i in range(0, 9)]

    for _ in range(256):
        spawn = fish.pop(0)
        fish += [spawn]
        fish[6] += spawn

    return str(sum(fish))
