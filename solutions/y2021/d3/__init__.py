"""Solutions for the day"""
from aoc.puzzles import test

from functools import reduce


def invert(bits: list[int]) -> list[int]:
    """Negate all numbers"""
    return [-bit for bit in bits]


def to_bits1(bits: list[int]) -> list[int]:
    """Convert rational numbers to bits"""
    return [1 if bit >= 0 else 0 for bit in bits]


def to_bits2(bits: list[int]) -> list[int]:
    """Convert rational numbers to bits"""
    return [1 if bit < 0 else 0 for bit in bits]


def bits_to_int(bits: list[int]) -> int:
    """Convert bits to int"""
    bits = bits.copy()
    bits.reverse()
    return reduce(lambda a, b: a + pow(2, b[0]) * b[1], enumerate(bits), 0)


@test([({"sample": "test"}, "198")])
def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    sample = data["sample"]
    bits = [[-1 if bit==ord("0") else 1 for bit in bits] for bits in sample]
    common_bits = reduce(lambda a, b: [a + b for a, b in zip(a, b)], bits)
    gamma = bits_to_int(to_bits1(common_bits))
    epsilon = bits_to_int(to_bits1(invert(common_bits)))
    return str(gamma * epsilon)


def reduce_bits(transform_bits, to_bits, bits: list[list[int]]) -> list[int]:
    """Filter bits until one remains"""
    remaining = bits.copy()
    i = 0
    while len(remaining) > 1:
        common_bits = [[-1 if bit else 1 for bit in bits] for bits in remaining]
        common_bits = reduce(lambda a, b: [a + b for a, b in zip(a, b)], common_bits)
        common_bits = to_bits(transform_bits(common_bits))
        remaining = [remaining for remaining in remaining if remaining[i] == common_bits[i]]
        print(common_bits, remaining, "\n")

        i += 1

    print(remaining[0])
    return remaining[0]


@test([({"sample": "test"}, "230")])
def solve1(data: list[str]) -> str:
    """Second solution"""
    sample = data["sample"]
    bits = [[0 if bit==ord("0") else 1 for bit in bits] for bits in sample]
    o2 = bits_to_int(reduce_bits(invert, to_bits2, bits))
    co2 = bits_to_int(reduce_bits(lambda a: a, to_bits2, bits))
    print(o2, co2)
    return str(o2 * co2)
