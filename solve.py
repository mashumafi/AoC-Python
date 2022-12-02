"""Solution loader main"""
from sys import argv
from importlib import import_module
from aoc.puzzles import get_input

y, d, s = argv[1:]

solutions = import_module(f"solutions.y{y}.d{d}")
sample = get_input(f"solutions/y{y}/d{d}")

if s == "2":
    print(solutions.solve1(sample))
else:
    print(solutions.solve0(sample))
