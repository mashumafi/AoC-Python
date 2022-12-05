"""Solutions for the day"""
from functools import reduce

import numpy as np

from aoc.puzzles import test, split, lower, higher, equals

def parse_points(p: tuple[str, str]) -> tuple[tuple[int, int], tuple[int, int]]:
    return tuple(map(int, p[0].split(","))), tuple(map(int, p[1].split(",")))

def parse_line(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    return parse_points(line.split("->"))


@test([({"sample": "test"}, "5")], equals(5294))
def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    sample = data["sample"]
    lines = list(map(parse_line, sample))
    points = {}
    for p0, p1 in lines:
        x1, y1 = p0
        x2, y2 = p1
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points[(x1, y)] = points.get((x1, y), 0) + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[(x, y1)] = points.get((x, y1), 0) + 1

    count = 0
    for k, v in points.items():
        if v >= 2:
            count += 1

    return str(count)


@test([({"sample": "test"}, "12")])
def solve1(data: list[str]) -> str:
    """Second solution"""
    sample = data["sample"]
    lines = list(map(parse_line, sample))
    points = {}
    for p0, p1 in lines:
        x1, y1 = p0
        x2, y2 = p1
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points[(x1, y)] = points.get((x1, y), 0) + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[(x, y1)] = points.get((x, y1), 0) + 1
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                y = min(y1, y2) + (x - min(x1, x2))
                points[(x, y)] = points.get((x, y), 0) + 1

    count = 0
    for k, v in points.items():
        if v >= 2:
            count += 1

    return str(count)
