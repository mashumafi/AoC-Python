"""Solutions for the day"""
from functools import reduce

import numpy as np

from aoc.puzzles import test, split, lower, higher


def parse_mat(raw: list[str]) -> np.array:
    return np.array([list(map(int, row.split())) for row in raw])


@test([({"sample": "test"}, "4512")], higher(473))
def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    sample = data["sample"]
    nums = [int(num) for num in sample[0].split(",")]
    tickets = [parse_mat(sample[i+1:i+6]) for i in range(1, len(sample), 6)]
    for num in nums:
        for ticket in tickets:
            for i, row in enumerate(ticket):
                for j, cell in enumerate(row):
                    if ticket[i][j] == num:
                        ticket[i][j] = -1

        for ticket in tickets:
            win_v = np.matmul(ticket, np.array([[1], [1], [1], [1], [1]]))
            win_v = [cell==-5 for cell in np.nditer(win_v)]

            win_h = np.matmul(np.array([1, 1, 1, 1, 1]), ticket)
            win_h = [cell==-5 for cell in np.nditer(win_h)]

            if any(win_v) or any(win_h):
                return str(sum(num if num > 0 else 0 for num in np.nditer(ticket)) * num)

    return str()


@test([({"sample": "test"}, "1924")])
def solve1(data: list[str]) -> str:
    """Second solution"""
    sample = split(data["sample"], str)
    sample = data["sample"]
    nums = [int(num) for num in sample[0].split(",")]
    tickets = [parse_mat(sample[i+1:i+6]) for i in range(1, len(sample), 6)]
    count = 0
    won = set()
    for num in nums:
        for ticket in tickets:
            for i, row in enumerate(ticket):
                for j, cell in enumerate(row):
                    if ticket[i][j] == num:
                        ticket[i][j] = -1

        for i, ticket in enumerate(tickets):
            win_v = np.matmul(ticket, np.array([[1], [1], [1], [1], [1]]))
            win_v = [cell==-5 for cell in np.nditer(win_v)]

            win_h = np.matmul(np.array([1, 1, 1, 1, 1]), ticket)
            win_h = [cell==-5 for cell in np.nditer(win_h)]

            if (any(win_v) or any(win_h)) and i not in won:
                won |= {i}
                count += 1
                if count == len(tickets):
                    return str(sum(num if num > 0 else 0 for num in np.nditer(ticket)) * num)

    return str()
