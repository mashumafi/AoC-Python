"""Solutions for the day"""
from functools import reduce

import numpy as np

from aoc.puzzles import test, split

m1 = np.array([[4, 8, 3],
               [1, 5, 9],
               [7, 2, 6]])

m2 = np.array([[3, 4, 8],
               [1, 5, 9],
               [2, 6, 7]])

def build_m(data: list[tuple[int, int]]) -> np.array:
    """Create a mtrix from the input data"""
    matrix = np.array([[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]])
    for opponent, player in data:
        matrix[opponent - ord("A")][player - ord("X")] += 1
    return matrix

@test([({"sample": "test"}, "15")])
def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    sample = split(data["sample"], ord, ord)
    return str(np.sum(m1 * build_m(sample)))


@test([({"sample": "test"}, "12")])
def solve1(data: list[str]) -> str:
    """Second solution"""
    sample = split(data["sample"], ord, ord)
    return str(np.sum(m2 * build_m(sample)))
