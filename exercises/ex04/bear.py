"""File to define Bear class."""


class Bear:
    """Bear details, no pun intended."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize bear - self object."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """One furry day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Updates hunger score based on amt. fish ate."""
        if num_fish > 0:
            self.hunger_score = self.hunger_score + num_fish
        return None
