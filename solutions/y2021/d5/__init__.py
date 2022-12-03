"""Solutions for the day"""
from aoc.puzzles import test, split

from functools import reduce


@test([({"sample": "test"}, "")])
def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    sample = split(data["sample"], str)
    return str()


@test([({"sample": "test"}, "")])
def solve1(data: list[str]) -> str:
    """Second solution"""
    sample = split(data["sample"], str)
    return str()
