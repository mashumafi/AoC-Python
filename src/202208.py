from aoc import AdventOfCode

aoc = AdventOfCode(year=2022, day=8)

def wrong(trees: list[list[int]]):
    height = len(trees)
    seen = set()
    for y in range(height):
        width = len(trees[y])
        previous_height = 0
        for x in range(width):
            if previous_height > trees[y][x]:
                break
            previous_height = trees[y][x]
            seen.add((x, y))

        previous_height = 0
        for x in range(width - 1, -1, -1):
            if previous_height > trees[y][x]:
                break
            previous_height = trees[y][x]
            seen.add((x, y))

        if y == 0:
            previous_height = 0
            for x in range(0, height):
                if previous_height > trees[y][x]:
                    break
                previous_height = trees[y][x]
                seen.add((x, y))

        if y == height - 1:
            previous_height = 0
            for x in range(height - 1, -1, -1):
                if previous_height > trees[y][x]:
                    break
                previous_height = trees[y][x]
                seen.add((x, y))

@aoc(expected=21)
def puzzle1(lines: list[str]) -> str:
    """Solve puzle 1"""
    trees = []
    for line in lines:
        trees += [[int(c) for c in iter(line)]]

    height = len(trees)
    count = 0
    for y1 in range(height):
        width = len(trees[y1])
        for x1 in range(width):
            valid = True
            for x2 in range(x1 + 1, width):
                if trees[y1][x2] >= trees[y1][x1]:
                    valid = False
                    break
                prev = trees[y1][x2]
            if valid:
                count += 1
                continue

            valid = True
            for x2 in range(x1 - 1, -1, -1):
                if trees[y1][x2] >= trees[y1][x1]:
                    valid = False
                    break
                prev = trees[y1][x2]
            if valid:
                count += 1
                continue

            valid = True
            for y2 in range(y1 + 1, height):
                if trees[y2][x1] >= trees[y1][x1]:
                    valid = False
                    break
                prev = trees[y2][x1]
            if valid:
                count += 1
                continue

            valid = True
            for y2 in range(y1 - 1, -1, -1):
                if trees[y2][x1] >= trees[y1][x1]:
                    valid = False
                    break
                prev = trees[y2][x1]
            if valid:
                count += 1
                continue

    return str(count)

@aoc(expected=8)
def puzzle2(lines: list[str]) -> str:
    """Solve puzle 2"""
    trees = []
    for line in lines:
        trees += [[int(c) for c in iter(line)]]

    height = len(trees)
    all_scores = []
    for y1 in range(height):
        width = len(trees[y1])
        for x1 in range(width):
            cur_score = [0, 0, 0, 0]
            for x2 in range(x1 + 1, width):
                cur_score[0] += 1
                if trees[y1][x2] >= trees[y1][x1]:
                    break

            for x2 in range(x1 - 1, -1, -1):
                cur_score[1] += 1
                if trees[y1][x2] >= trees[y1][x1]:
                    break

            for y2 in range(y1 + 1, height):
                cur_score[2] += 1
                if trees[y2][x1] >= trees[y1][x1]:
                    break

            for y2 in range(y1 - 1, -1, -1):
                cur_score[3] += 1
                if trees[y2][x1] >= trees[y1][x1]:
                    break

            all_scores += [cur_score[0] * cur_score[1] * cur_score[2] * cur_score[3]]

    return str(max(all_scores))
