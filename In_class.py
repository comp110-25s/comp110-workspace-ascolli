SECRET: str = "punk"


def guess_secret(word: str, secret: str, idx: int = 0) -> bool:
    if len(word) != len(secret):
        print("Words are different lengths.")
        return False
    if idx < len(word):
        if word[idx] != secret[idx]:
            print(f"{word[idx]} isn't the secret word's next letter.")
            return False
        else:
            print(
                f"{word[idx]} is at index {idx} for both words! Checking next letters..."
            )

            return guess_secret(word=word, secret=secret, idx=idx + 1)

    print("They are the same word!")
    return True


print(guess_secret(word="punt", secret="punk"))


def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 != 0:
        return "fizz"
    elif n % 5 == 0 and n % 3 != 0:
        return "buzz"
    elif n % 5 == 0 and n % 3 == 0:
        return "fizzbuzz"
    return str(n)


print(f"C{'OM'}P{100+10}")

"""SETS SYNTAX"""
pids: set[int] = {710000000, 712345678}

pids.add(730564797)

"""Dictionaries Syntax"""
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 4}
ice_cream["vanilla"] += 110
"""to add elements to a dictionary"""
ice_cream["mint"] = 3

"""to access a value (in repl)"""
ice_cream["mint"]

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint")

"""Removing elements in dictionary"""
ice_cream.pop("vanilla")

"""for , in loop"""
for key in ice_cream:
    print(key)


class Line:
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translation(self, dy: float) -> None:
        self.y += dy

    def __str__(self) -> str:
        """Magic method that prints string representation of Point obj"""
        return f"({self.x}, {self.y})"
