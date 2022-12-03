"""Solutions for the day"""
from aoc.puzzles import test, split

from functools import reduce


@test([({"sample": "test"}, "157")])
def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    sample = split(data["sample"], str)
    total = 0
    for line, in sample:
        compartment1, compartment2 = (line[0:int(len(line)/2)], line[int(len(line)/2):])
        items1 = {key: True for key in compartment1}
        for item in compartment2:
            if item in items1:
                if ord(item) >= ord('a'):
                    total += ord(item) - ord('a') + 1
                elif ord(item) >= ord('A'):
                    total += ord(item) - ord('A') + 27
                break
    return str(total)


@test([({"sample": "test"}, "70")])
def solve1(data: list[str]) -> str:
    """Second solution"""
    sample = data["sample"]
    total = 0
    print(sample)
    for i in range(0, len(sample), 3):
        compartment1, compartment2, compartment3 = sample[i:i+3]
        items1 = set(compartment1)
        items2 = set(compartment2)
        items3 = set(compartment3)

        solo = next(iter(items1 & items2 & items3))
        
        if ord(solo) >= ord('a'):
            total += ord(solo) - ord('a') + 1
        elif ord(solo) >= ord('A'):
            total += ord(solo) - ord('A') + 27

    return str(total)
