"""Exercise five - Easter Egg hunt!."""

from __future__ import annotations

__author__: str = "730564797"


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializes instances of Node class."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Overrides print fn default habit."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Tells u the value!."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Finds max value in linked list, and returns it."""
    if head is None:
        raise ValueError("Cannot call max with None")
    else:
        if head.next is None:
            return head.value
        else:
            maximum: int = max(head.next)
            if maximum < head.value:
                return head.value
            else:
                return maximum


def linkify(items: list[int]) -> Node | None:
    """Turns list into NOdes!."""
    if len(items) == 0:
        return None
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Scales every value in linked list and returns scaled list."""
    if head is None:
        return None
    else:
        new_node: Node = Node(head.value * factor, scale(head.next, factor))
        return new_node
