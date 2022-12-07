from aoc import AdventOfCode
from os import path

aoc = AdventOfCode(year=2022, day=7)

@aoc(expected="95437")
def puzzle1(data: list[str]) -> str:
    """Solve puzle 1"""
    cwd = "/"
    dirs = {}
    total = 0
    for line in data:
        if line[0] == "$":
            command, *args = line[1:].strip().split(" ")
            #print(f"'{command}' {' '.join(args)}")
            match command.strip():
                case "cd":
                    if args[0] == "/":
                        cwd = "/"
                    elif args[0] == "..":
                        cwd = "/".join(cwd[:-1].split("/")[:-1]) + "/"
                    else:
                        cwd += args[0] + "/"
                    #print("cwd", cwd)
                    dirs[cwd] = dirs.get(cwd, 0)
                case "ls":
                    pass
        else:
            size, name = line.split()
            if size == "dir":
                pass
            else:
                #dirs[cwd] += int(size)
                for k, v in dirs.items():
                    if cwd.startswith(k):
                        dirs[k] += int(size)
    
    return str(sum([dir for dir in dirs.values() if dir < 100000]))

@aoc(expected="24933642")
def puzzle2(data: list[str]) -> str:
    """Solve puzle 2"""
    cwd = "/"
    dirs = {}
    total = 0
    for line in data:
        if line[0] == "$":
            command, *args = line[1:].strip().split(" ")
            #print(f"'{command}' {' '.join(args)}")
            match command.strip():
                case "cd":
                    if args[0] == "/":
                        cwd = "/"
                    elif args[0] == "..":
                        cwd = "/".join(cwd[:-1].split("/")[:-1]) + "/"
                    else:
                        cwd += args[0] + "/"
                    print("cwd", cwd)
                    dirs[cwd] = dirs.get(cwd, 0)
                case "ls":
                    pass
        else:
            size, name = line.split()
            if size == "dir":
                pass
            else:
                for k, v in dirs.items():
                    if cwd.startswith(k):
                        dirs[k] += int(size)

    used = dirs["/"]
    needed = 70000000 - 30000000
    big = [(v,k) for k,v in dirs.items() if used - v < needed]
    big.sort()
    print(big[0][0])
    return str(big[0][0])
