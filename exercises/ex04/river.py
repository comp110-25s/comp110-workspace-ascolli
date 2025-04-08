"""File to define River class."""

__author__: str = "730564797"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """River class."""

    day: int
    Bears: list[int]
    Fish: list[int]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Ensures only young animals live on."""
        alive_Fish: list[Fish] = []
        alive_Bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                alive_Fish.append(fish)
        self.fish = alive_Fish
        """Same application but for Bears."""
        for Bears in self.bears:
            if Bears.age <= 5:
                alive_Bears.append(Bears)
        self.bears = alive_Bears
        return None

    def bears_eating(self):
        """Hungry Bear."""
        for Bears in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                Bears.eat(3)
        return None

    def check_hunger(self):
        """Checks hunger of bears in river."""
        alive_Bears2: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_Bears2.append(bear)
        self.bears = alive_Bears2
        return None

    def repopulate_fish(self):
        """4 new fish per couple of fish in river."""
        young_fish = len(self.fish) // 2 * 4
        count2: int = 0
        while count2 < young_fish:
            new_fish = Fish()
            self.fish.append(new_fish)
        return None

    def repopulate_bears(self):
        """1 new young bear for every 2 adult bears."""
        young_bears = len(self.bears) // 2
        count: int = 0
        while count < young_bears:
            new_bear = Bear()
            self.bears.append(new_bear)
            count += 1
        return None

    def view_river(self):
        """View the population of animals."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """One week = 7 days."""
        count: int = 0
        while count < 7:
            self.one_river_day()
            count += 1
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes front-most fish from index in the list."""
        if amount > len(self.fish):
            amount = len(self.fish)
        while amount > 0 and len(self.fish):
            self.fish.pop(0)
            amount -= 1
        return None
