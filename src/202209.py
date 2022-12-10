from aoc import AdventOfCode, split
import numpy as np

aoc = AdventOfCode(year=2022, day=9)

@aoc(expected=88)
def puzzle1(data: list[str]) -> str:
    """Solve puzle 1"""
    head = (0, 0)
    tail = (0, 0)
    visited = {(0, 0)}
    for line in data:
        dir, num = line.split()
        num = int(num)
        for _ in range(num):
            match dir:
                case "L":
                    head = head[0] - 1, head[1]
                case "R":
                    head = head[0] + 1, head[1]
                case "U":
                    head = head[0], head[1] - 1
                case "D":
                    head = head[0], head[1] + 1

            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                match dir:
                    case "L":
                        tail = head[0] + 1, head[1]
                    case "R":
                        tail = head[0] - 1, head[1]
                    case "U":
                        tail = head[0], head[1] + 1
                    case "D":
                        tail = head[0], head[1] - 1
                visited.add(tail)

    return str(len(visited))

def solve(moves: list[tuple[str, int]], rope_len: int) -> int:
    dirs = {
        'R': np.array([1, 0]),
        'U': np.array([0, 1]),
        'L': np.array([-1, 0]),
        'D': np.array([0, -1])
    }
    ropes = [np.array([0, 0]) for _ in range(rope_len)]
    visited = set()

    for move in moves:
        for _ in range(move[1]):
            ropes[0] += dirs[move[0]]
            for i in range(1, rope_len):
                if 2 in np.abs(ropes[i] - ropes[i-1]):
                    ropes[i] += np.sign(ropes[i-1] - ropes[i])
            visited |= {tuple(ropes[-1])}

    return len(visited)

@aoc(expected=36)
def puzzle2(data: list[str]) -> str:
    """Solve puzle 2"""
    moves = split(data, str, int)
    print(solve(moves, 2))
    return str(solve(moves, 10))
