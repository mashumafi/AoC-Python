"""Solutions for the day"""
from functools import reduce

import numpy as np

from aoc.puzzles import test, split


def parse_range(r: str) -> set[int]:
    low, high = r.split("-")
    return set(range(int(low), int(high) + 1))


@test([({"sample": "test"}, "2")])
def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    sample = [(parse_range(left), parse_range(right)) for left, right in [line.split(",") for line in  data["sample"]]]
    count = 0
    for range1, range2 in sample:
        if range1 | range2 in [range1, range2]:
            count += 1

    return str(count)


@test([({"sample": "test"}, "4")])
def solve1(data: list[str]) -> str:
    """Second solution"""
    sample = [(parse_range(left), parse_range(right)) for left, right in [line.split(",") for line in  data["sample"]]]
    count = 0
    for range1, range2 in sample:
        if range1 & range2:
            count += 1

    return str(count)
