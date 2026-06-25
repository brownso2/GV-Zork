#Item Class for GV-ZORK: Sofie Spitael

class Item:
    """
    Represents an item that can be found in the game.
    Each item has a name, description, calories value, and weight.
    """

    #creates a new item.
    def __init__(self, name: str, description: str,
                 calories: int, weight: int):

        self.name = name
        self.description = description
        self.calories = calories
        self.weight = weight

    #returns the item name.
    @property
    def name(self) -> str:
        return self._name

    #sets and validates the item name.
    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Item name cannot be blank.")
        self._name = value

    #returns the item description.
    @property
    def description(self) -> str:
        return self._description

    #sets and validates the item description.
    @description.setter
    def description(self, value: str) -> None:
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Item description cannot be blank.")
        self._description = value

    #returns the calorie value.
    @property
    def calories(self) -> int:
        return self._calories

    #sets and validates calories.
    @calories.setter
    def calories(self, value: int) -> None:

        if not isinstance(value, int):
            raise ValueError("Item calories must be an integer.")

        if value < 0 or value > 1000:
            raise ValueError("Item calories must be between 0 and 1000.")

        self._calories = value

    #returns the item weight.
    @property
    def weight(self) -> int:
        return self._weight

    #sets and validates weight.
    @weight.setter
    def weight(self, value: int) -> None:

        if not isinstance(value, int):
            raise ValueError("Item weight must be an integer.")

        if value < 0 or value > 500:
            raise ValueError("Item weight must be between 0 and 500 pounds.")

        self._weight = value

    #returns item information.
    def __str__(self) -> str:

        return(
            f"{self.name} - "
            f"{self.weight} lb - "
            f"{self.description}"
        )
#Item Class for GV-ZORK: Sofie Spitael
