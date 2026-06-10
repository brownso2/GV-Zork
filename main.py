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

class NPC:
    def __init__(self, name: str, description: str):
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("NPC name cannot be blank.")

        if not isinstance(description, str) or description.strip() == "":
            raise ValueError("NPC description cannot be blank.")

        self._name = name #making these protected and not private 
        self._description = description
        self._messages = [] #empty list so we can go back later 
        self._message_number = 0

    @property
    def name(self) -> str: #having this be a string because it wouldn't be int
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("NPC name can't be blank.")
        self._name = value

    @property
    def description(self) -> str:
        return self._description #I'm just doing all of them as protected let me know if thi is an issue

    @description.setter
    def description(self, value: str) -> None:
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("NPC description cannot be blank.")
        self._description = value

    @property
    def message_number(self) -> int: #doing this as an int
        return self._message_number

    @property
    def messages(self) -> list[str]:
        return self._messages

    def add_message(self, message: str) -> None:
        if not isinstance(message, str) or message.strip() == "":
            raise ValueError("Message cannot be blank.")

        self._messages.append(message)

    def get_message(self) -> str:
        if len(self._messages) == 0:
            return "..." #If the NPC has no messages, return a placeholder message, instead of causing an IndexError from accessing an empty because it kept giving me errors list.

        current_message = self._messages[self._message_number]

        self._message_number += 1

        if self._message_number >= len(self._messages):
            self._message_number = 0

        return current_message

    def __str__(self) -> str:
        return self._name
   