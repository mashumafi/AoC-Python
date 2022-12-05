"""Solutions for the day"""
from functools import reduce

import numpy as np

from aoc.puzzles import test, split, lower, higher, equals


def parse_mat(raw: list[str]) -> np.array:
    return np.array([list(map(int, row.split())) for row in raw])


@test([({"sample": "test"}, "4512")], higher(473), equals(23177))
def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    sample = data["sample"]
    nums = [int(num) for num in sample[0].split(",")]
    tickets = [parse_mat(sample[i+1:i+6]) for i in range(1, len(sample), 6)]
    for num in nums:
        tickets = [np.array(
            [-1 if cells==num else cells for cells in np.nditer(ticket)]
        ).reshape(5, 5) for ticket in tickets]

        for ticket in tickets:
            win_v = any([cell==-5 for cell in np.nditer(np.matmul(ticket, np.array([[[1]]*5])))])
            win_h = any([cell==-5 for cell in np.nditer(np.matmul(np.array([1]*5), ticket))])

            if win_v or win_h:
                return str(sum(num if num > 0 else 0 for num in np.nditer(ticket)) * num)

    return str()


@test([({"sample": "test"}, "1924")], equals(6804))
def solve1(data: list[str]) -> str:
    """Second solution"""
    sample = split(data["sample"], str)
    sample = data["sample"]
    nums = [int(num) for num in sample[0].split(",")]
    tickets = [parse_mat(sample[i+1:i+6]) for i in range(1, len(sample), 6)]
    for num in nums:
        tickets = [np.array(
            [-1 if cells==num else cells for cells in np.nditer(ticket)]
        ).reshape(5, 5) for ticket in tickets]

        def is_loser(ticket):
            win_v = any([cell==-5 for cell in np.nditer(np.matmul(ticket, np.array([[[1]]*5])))])
            win_h = any([cell==-5 for cell in np.nditer(np.matmul(np.array([1]*5), ticket))])

            return not(win_v or win_h)

        value = sum(num if num > 0 else 0 for num in np.nditer(tickets[-1])) * num
        tickets = list(filter(is_loser, tickets))
        if not list(tickets):
            return str(value)

    return str()
