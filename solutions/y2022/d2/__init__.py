"""Solutions for the day"""
from aoc.puzzles import test, split

from functools import reduce

# A/X - Rock + 1
# B/Y - Paper + 2
# C/Z - Scissors + 3

# lost +0
# draw +3
# win +6

def get_value(choice: str) -> int:
    match choice:
        case "X": return 1
        case "Y": return 2
        case "Z": return 3
    print("E1", choice)

def get_score(opponent, player) -> int:
    if opponent == "A":
        if player == "X":
            return 3
        if player == "Y":
            return 6
        if player == "Z":
            return 0

    if opponent == "B":
        if player == "X":
            return 0
        if player == "Y":
            return 3
        if player == "Z":
            return 6

    if opponent == "C":
        if player == "X":
            return 6
        if player == "Y":
            return 0
        if player == "Z":
            return 3

    print("E2", opponent, player)


def get_shape(opponent, player) -> bytes:
    # X lose
    # Y draw
    # Z win
    if opponent == "A":
        if player == "X":
            return "Z"
        if player == "Y":
            return "X"
        if player == "Z":
            return "Y"

    if opponent == "B":
        if player == "X":
            return "X"
        if player == "Y":
            return "Y"
        if player == "Z":
            return "Z"

    if opponent == "C":
        if player == "X":
            return "Y"
        if player == "Y":
            return "Z"
        if player == "Z":
            return "X"

    print("E3", opponent, player)


@test([({"sample": "test"}, "15")])
def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    sample = data["sample"]
    return str(sum([get_score(o, p) + get_value(p) for o, p in split(sample, str, str)]))


@test([({"sample": "test"}, "12")])
def solve1(data: list[str]) -> str:
    """Second solution"""
    sample = data["sample"]
    return str(sum([get_score(o, get_shape(o, p)) + get_value(get_shape(o, p)) for o, p in split(sample, str, str)]))
