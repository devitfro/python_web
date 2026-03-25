from typing import Protocol


class Shape(Protocol):
    def area(self) -> float:
        ...