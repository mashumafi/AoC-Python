"""Helper functions for AoC puzzles"""
from os import listdir, path

def readall(file: str) -> bytes:
    """Read an entire file"""
    with open(f"{file}", "r") as file:
        return file.read().split("\n")

def get_input(package: str) -> dict[str, list[str]]:
    """Loads data from a url or cache"""
    inputs = [filename for filename in listdir(package) if filename.endswith(".txt")]
    return {filename.replace(".txt", ""): readall(path.join(package, filename)) for filename in inputs}

def test(tests: list[tuple[dict[str, str], str]]):
    """Runs tests"""
    def decorator(func):
        """Runs tests or throws on error"""
        def internal(original_data: dict[str, list[str]]):
            for aliases, expected in tests:
                data = {}
                for src, dst in aliases.items():
                    data[src] = original_data[dst]
                result = func(data)
                if expected != result:
                    raise Exception(f"{repr(expected)} != {repr(result)}")
            return func(original_data)

        return internal
    return decorator

def parse(line: list[str], *convert) -> tuple:
    return [c(l) for c, l in zip(*convert, line)]

def split(data: list[str], *convert) -> tuple:
    return [parse(line.split(), convert) for line in data]
