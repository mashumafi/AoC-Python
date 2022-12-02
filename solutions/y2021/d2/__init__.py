"""All puzzle solutions"""


def solve1(data: dict[str, list[str]]) -> str:
    """Sleigh position"""
    def str_to_dir(s: str) -> tuple[int, int]:
        match s:
            case "down": return (0, 1)
            case "up": return (0, -1)
            case "forward": return (1, 0)

    sample = [sample.split() for sample in data["sample"]]
    sample = [(str_to_dir(dir), int(num)) for dir, num in sample]

    pos = (0, 0)
    aim = 0
    for dir, mag in sample:
        aim += dir[1] * mag
        pos = (pos[0] + dir[0] * mag, pos[1] + dir[0] * mag * aim)

    return str(pos[0]*pos[1])
