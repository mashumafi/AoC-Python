"""Solutions for the day"""
from functools import reduce

import numpy as np

from aoc.puzzles import test, split


def parse_range(r: str) -> tuple[int, int]:
    low, high = r.split("-")
    return int(low), int(high)


@test([({"sample": "test"}, "2")])
def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    sample = [(parse_range(left), parse_range(right)) for left, right in [line.split(",") for line in  data["sample"]]]
    count = 0
    for range1, range2 in sample:
        low1, high1 = range1
        low2, high2 = range2

        if low2 <= low1 and high1 <= high2:
            count += 1
        elif low1 <= low2 and high2 <= high1:
            count += 1
    return str(count)


@test([({"sample": "test"}, "4")])
def solve1(data: list[str]) -> str:
    """Second solution"""
    sample = [(parse_range(left), parse_range(right)) for left, right in [line.split(",") for line in  data["sample"]]]
    count = 0
    for range1, range2 in sample:
        low1, high1 = range1
        low2, high2 = range2

        if (low2 <= low1 and low1 <= high2) or (low2 <= high1 and high1 <= high2):
            count += 1
        elif (low1 <= low2 and low2 <= high1) or (low1 <= high2 and high2 <= high1):
            count += 1
    return str(count)
