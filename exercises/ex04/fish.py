"""File to define Fish class."""


class Fish:
    """Details of Fish in the river."""

    age: int

    def __init__(self):
        """Initialize a fish -self object."""
        self.age: int = 0
        return None

    def one_day(self):
        """One scaley day."""
        self.age += 1
        return None
