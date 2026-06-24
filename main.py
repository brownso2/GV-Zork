#Item Class for GV-ZORK: Sofie Spitael (6/10/2026)

class Item:
    """
    Represents an item that can be found in the game.
    Each item has a name, description, calories value, and weight.
    """

    # Creates a new Item
    def __init__(self, name: str, description: str,
                 calories: int, weight: int):

        #Use properties so values are checked before being stored.
        self.name = name
        self.description = description
        self.calories = calories
        self.weight = weight

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        #Item name cannot be left blank.
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Item name cannot be blank.")
        #Save the name.
        self._name = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        #Description cannot be left blank.
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Item description cannot be blank.")
        #Save the description.
        self._description = value

    @property
    def calories(self) -> int:
        return self._calories

    @calories.setter
    def calories(self, value: int) -> None:
        #Calories must be an integer (number).
        if not isinstance(value, int):
            raise ValueError("Item calories must be an integer.")
        #Calorie value must be between 0 and 1000.
        if value < 0 or value > 1000:
            raise ValueError("Item calories must be between 0 and 1000.")
        #Save the calories.
        self._calories = value

    @property
    def weight(self) -> int:
        return self._weight

    @weight.setter
    def weight(self, value: int) -> None:
        #Weight must be an integer (number).
        if not isinstance(value, int):
            raise ValueError("Item weight must be an integer.")
        #Weight value must be between 0 and 500 pounds.
        if value < 0 or value > 500:
            raise ValueError("Item weight must be between 0 and 500 pounds.")
        #Save the weight.
        self._weight = value

    def __str__(self) -> str:
        #Returns item information
        return(
            f"{self.name} - "
            f"{self.weight} lb - "
            f"{self.description}"
        )
#Item Class for GV-ZORK: Sofie Spitael (6/10/2026)"""
