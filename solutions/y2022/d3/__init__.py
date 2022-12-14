"""Solutions for the day"""
from functools import reduce

import numpy as np

from aoc.puzzles import test, split, lower, higher, equals


@test([({"sample": "test"}, "157")])
def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    sample = data["sample"]
    total = 0
    for line in sample:
        compartment1, compartment2 = (line[0:int(len(line)/2)], line[int(len(line)/2):])
        items1 = set(compartment1)
        items2 = set(compartment2)
        solo = next(iter(items1 & items2))
        total += ord(solo) - ord('a') + 1 if ord(solo) >= ord('a') else ord(solo) - ord('A') + 27

    return str(total)


@test([({"sample": "test"}, "70")])
def solve1(data: list[str]) -> str:
    """Second solution"""
    sample = data["sample"]
    total = 0
    for i in range(0, len(sample), 3):
        compartment1, compartment2, compartment3 = sample[i:i+3]
        items1 = set(compartment1)
        items2 = set(compartment2)
        items3 = set(compartment3)
        solo = list(items1 & items2 & items3)[0]
        total += ord(solo) - ord('a') + 1 if ord(solo) >= ord('a') else ord(solo) - ord('A') + 27

    return str(total)
