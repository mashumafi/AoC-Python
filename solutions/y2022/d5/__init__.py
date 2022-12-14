"""Solutions for the day"""
from functools import reduce
from collections import defaultdict

import numpy as np

from aoc.puzzles import test, split, lower, higher, equals


@test([({"sample": "test"}, "CMZ")], equals("JRVNHHCSJ"))
def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    sample = data["sample"]
    end_stacks = sample.index("")
    stacks = sample[:end_stacks - 1]
    layout = defaultdict(lambda : [])
    for stack in stacks:
        stack = [stack[i+1:i+2:i+4] for i in range(0, len(stack), 4)]
        for i, stack in enumerate(stack):
            if stack != " ":
                layout[i] += stack

    moves = sample[end_stacks + 1:]

    for move in moves:
        _, num, _, src, _, dest = move.split()
        num = int(num)
        src = int(src)-1
        dest = int(dest)-1
        for i in range(num):
            layout[dest] = [layout[src].pop(0)] + layout[dest]

    stack = list([stack for stack in layout.items()])
    stack.sort()
    return "".join([col[0] for i, col in stack])


@test([({"sample": "test"}, "MCD")], equals("GNFBSBJLH"))
def solve1(data: list[str]) -> str:
    """Second solution"""
    sample = data["sample"]
    end_stacks = sample.index("")
    stacks = sample[:end_stacks - 1]
    layout = defaultdict(lambda : [])
    for stack in stacks:
        stack = [stack[i+1:i+2:i+4] for i in range(0, len(stack), 4)]
        for i, stack in enumerate(stack):
            if stack != " ":
                layout[i] += [stack]

    moves = sample[end_stacks + 1:]

    for move in moves:
        _, num, _, src, _, dest = move.split()
        num = int(num)
        src = int(src)-1
        dest = int(dest)-1
        layout[dest] = layout[src][0:num] + layout[dest]
        for i in range(num):
            layout[src].pop(0)

    stack = list([stack for stack in layout.items()])
    stack.sort()
    return "".join([col[0] for i, col in stack])
