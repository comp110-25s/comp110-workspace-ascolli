"""Calculate the cost and supplies needed for a cozy tea party"""

__author__: str = "730564797"


def main_planner(guests: int) -> None:
    """Based on guests, tells amount of supplies and cost"""
    print("A " + "Cozy " + "Tea " + "Party " + "for " + str(guests) + " People!")
    print("Tea " + "Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """This function specifies how many tea bags are needed"""
    return people * 2


def treats(people: int) -> int:
    """How many treats are needed at the party"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """The total cost of the tea party"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
