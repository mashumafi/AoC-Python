"""Helper for downloading, running, and submitting AoC solutions."""
from aocd import submit
from aocd.models import Puzzle

class AdventOfCode(object):
    def __init__(self, *, year, day) -> None:
        self.puzzle = Puzzle(year=year, day=day)
        self.solver_count = 0

    def __call__(self, *, expected) -> str:
        def decorator(solver):
            if expected:
                result = solver(self.puzzle.example_data.split("\n"))
                if str(result) != str(expected):
                    print(f"Unexpected answer {result} != {expected}")
                    return

            result = solver(self.puzzle.input_data.split("\n"))
            if not result:
                print(f"Skip submitting {repr(result)}")
                return

            self.solver_count += 1
            if self.solver_count == 1:
                if self.puzzle.answered_a:
                    print(f"Skip submitting {repr(result)}")
                    return
            elif self.solver_count == 2:
                if not self.puzzle.answered_a or self.puzzle.answered_b:
                    print(f"Skip submitting {repr(result)}")
                    return
            else:
                return

            submit(result, year=self.puzzle.year, day=self.puzzle.day, reopen=False)

        return decorator
