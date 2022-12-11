from aoc import AdventOfCode, get_ints
from typing import Self
from functools import reduce
from collections import defaultdict

aoc = AdventOfCode(year=2022, day=11)

class Monkey:
    items: list[int]
    test: int
    true: int
    false: int
    inspected : int = 0

    def process(self, worry_factor, lcm = 1) -> dict[int, list[int]]:
        movements = defaultdict(lambda: [])
        items, self.items = self.items, []
        self.inspected += len(items)
        for old in items:
            new = self.operation(old) % lcm
            if worry_factor != 1:
                new = int(new / worry_factor)

            if new % self.test == 0:
                movements[self.true] += [new]
            else:
                movements[self.false] += [new]

        return movements

    @staticmethod
    def create_operand(text: str):
        if text == "old":
            return lambda old: old
        else:
            i = int(text)
            return lambda _: i

    @staticmethod
    def create_operator(expr: str):
        def add(a, b):
            return lambda old: a(old) + b(old)
        def mult(a, b):
            return lambda old: a(old) * b(old)

        operands = expr.split(" ")
        match operands[1]:
            case "*":
                return mult(Monkey.create_operand(operands[0]),
                    Monkey.create_operand(operands[2]))
            case "+":
                return add(Monkey.create_operand(operands[0]),
                    Monkey.create_operand(operands[2]))

    @staticmethod
    def parse(lines: list[str]) -> Self:
        monkey = Monkey()
        monkey.items = get_ints(lines[1])
        monkey.operation = Monkey.create_operator(lines[2].split("new = ")[1])
        monkey.test = get_ints(lines[3])[0]
        monkey.true = get_ints(lines[4])[0]
        monkey.false = get_ints(lines[5])[0]
        return monkey

@aoc(expected=10605)
def puzzle1(data: list[str]) -> str:
    """Solve puzle 1"""
    monkeys = [Monkey.parse(data[i:i+6]) for i in range(0, len(data), 7)]

    for _ in range(20):
        for monkey in monkeys:
            for i, items in monkey.process(3).items():
                monkeys[i].items += items

    inspected = [monkey.inspected for monkey in monkeys]
    inspected.sort()

    return str(inspected[-1] * inspected[-2])

@aoc(expected=2713310158)
def puzzle2(data: list[str]) -> str:
    """Solve puzle 2"""
    monkeys = [Monkey.parse(data[i:i+6]) for i in range(0, len(data), 7)]

    lcm = reduce(lambda a, b: a * b, [monkey.test for monkey in monkeys], 1)
    for _ in range(10000):
        for monkey in monkeys:
            for i, items in monkey.process(1, lcm=lcm).items():
                monkeys[i].items += items

    inspected = [monkey.inspected for monkey in monkeys]
    inspected.sort()

    return str(inspected[-1] * inspected[-2])
