"""Item class for GV-ZORK.

Defines the Item class used to represent objects that can be
picked up, carried, dropped, or given to the elf.
"""

# Item Class for GV-ZORK: Sofie Spitael


class Item:
    """Represents an item that can be found in the game.

    Each item has a name, description, calorie value, and weight.
    """

    def __init__(self, name: str, description: str,
                 calories: int, weight: int):
        """Creates a new Item object."""

        # Assign values using the property setters.
        self.name = name
        self.description = description
        self.calories = calories
        self.weight = weight

    @property
    def name(self) -> str:
        """Returns the item's name."""

        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Sets and validates the item's name."""

        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Item name cannot be blank.")

        self._name = value

    @property
    def description(self) -> str:
        """Returns the item's description."""

        return self._description

    @description.setter
    def description(self, value: str) -> None:
        """Sets and validates the item's description."""

        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Item description cannot be blank.")

        self._description = value

    @property
    def calories(self) -> int:
        """Returns the item's calorie value."""

        return self._calories

    @calories.setter
    def calories(self, value: int) -> None:
        """Sets and validates the item's calorie value."""

        if not isinstance(value, int):
            raise ValueError("Item calories must be an integer.")

        if value < 0 or value > 1000:
            raise ValueError(
                "Item calories must be between 0 and 1000."
            )

        self._calories = value

    @property
    def weight(self) -> int:
        """Returns the item's weight."""

        return self._weight

    @weight.setter
    def weight(self, value: int) -> None:
        """Sets and validates the item's weight."""

        if not isinstance(value, int):
            raise ValueError("Item weight must be an integer.")

        if value < 0 or value > 500:
            raise ValueError(
                "Item weight must be between 0 and 500 pounds."
            )

        self._weight = value

    def __str__(self) -> str:
        """Returns a formatted string describing the item."""

        return (
            f"{self.name} - "
            f"{self.weight} lb - "
            f"{self.description}"
        )


# Item Class for GV-ZORK: Sofie Spitael