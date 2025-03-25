"""Exercise 03!"""

__author__: str = "730564797"


def invert(start: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values for an inverted dictionary"""
    finish: dict[str, str] = {}
    for key in start:
        swap_one = start[key]
        if swap_one in finish:
            raise KeyError(f"Duplicate key found when inverting- this is prohibited :(")
        finish[swap_one] = key
    return finish


def count(param_1: list[str]) -> dict[str, int]:
    """Returns a dictionary that displays how many times an item was in a provided list"""
    result: dict[str, int] = {}
    idx: int = 0
    while idx < len(param_1):
        if param_1[idx] in result:
            result[param_1[idx]] += 1
        else:
            result[param_1[idx]] = 1
        idx += 1
    return result


def favorite_color(n_and_c: dict[str, str]) -> str:
    """To find how many times each color appears"""
    record_match: dict[str, int] = {}
    for key in n_and_c:
        if n_and_c[key] in record_match:
            record_match[n_and_c[key]] += 1
        else:
            record_match[n_and_c[key]] = 1
    """to find most popular color"""
    high_count: int = 0
    most_pop: str = ""
    for key in n_and_c:
        if record_match[n_and_c[key]] > high_count:
            high_count = record_match[n_and_c[key]]
            most_pop = n_and_c[key]
    return most_pop


def bin_len(canvas: list[str]) -> dict[int, set[str]]:
    """Sorts a list of strings into a dictionary with length and set of strings of that length"""
    result: dict = {}
    for str in canvas:
        length = len(str)
        if length in result:
            result[length].add(str)
        else:
            result[length] = {str}
    return result
