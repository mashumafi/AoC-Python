from aoc import AdventOfCode
from os.path import join, normpath as np

aoc = AdventOfCode(year=2022, day=7)

def get_dirs(data: list[str]) -> dict[str, int]:
    """Process command and collect directory sizes"""
    cwd = "/"
    dirs = {}
    for line in data:
        if line[0] == "$":
            command, *args = line[1:].strip().split(" ")
            match command.strip():
                case "cd":
                    if args[0] == "/":
                        cwd = "/"
                    else:
                        cwd = np(join(cwd, args[0]))
                    dirs[cwd] = dirs.get(cwd, 0)
        else:
            size, _ = line.split()
            if size != "dir":
                for k, _ in dirs.items():
                    if cwd.startswith(k):
                        dirs[k] += int(size)
    return dirs

@aoc(expected="95437")
def puzzle1(data: list[str]) -> str:
    """Solve puzle 1"""
    dirs = get_dirs(data)
    return str(sum([dir for dir in dirs.values() if dir < 100000]))

@aoc(expected="24933642")
def puzzle2(data: list[str]) -> str:
    """Solve puzle 2"""
    dirs = get_dirs(data)
    used = dirs["/"]
    needed = 70000000 - 30000000
    big = [(v,k) for k,v in dirs.items() if used - v < needed]
    big.sort()
    return str(big[0][0])
