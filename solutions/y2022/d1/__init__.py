"""Solutions for the day"""

def solve0(data: dict[str, list[str]]) -> str:
    """First solution"""
    total = 0
    high = 0
    for num in data["sample"]:
        if num:
            num = int(num)
            total += num
        else:
            high = max(high, total)
            total = 0
    return str(high)


def solve1(data: dict[str, list[str]]) -> str:
    """Second solution"""
    total = 0
    sums = []
    for num in data["sample"]:
        if num:
            num = int(num)
            total += num
        else:
            sums += [total]
            total = 0
    sums.sort()
    return str(sum(sums[len(sums)-3:]))
