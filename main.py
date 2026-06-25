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
   


class Game:

    def _create_world(self):
        

        elf = NPC(
            "Elf",
            "A magical elf who loves food and can break the troll's spell."
        )
        elf.add_message("Have you brought me something to eat?")
        elf.add_message("I'm starving")
        elf.add_message("The fate of campus rests in your hands!")

        professor = NPC(
            "Professor",
            "A tired professor surrounded by stacks of assignments."
        )
        professor.add_message("Have you started the project yet?")
        professor.add_message("Remember to test your code.")
        professor.add_message("Office hours are tomorrow.")

        student = NPC(
            "Student",
            "A stressed student carrying several textbooks."
        )
        student.add_message("I haven't slept in two days.")
        student.add_message("Do you know where the library is?")
        student.add_message("I have 3 assignments due tonight")

        janitor = NPC(
            "Janitor",
            "A friendly janitor cleaning the hallway."
        )
        janitor.add_message("Campus has been quiet today.")
        janitor.add_message("I think I saw something near the ravines.")
        janitor.add_message("Stay safe out there.")

        barista = NPC(
            "Barista",
            "A cheerful barista serving coffee."
        )
        barista.add_message("Need a coffee?")
        barista.add_message("I think they want a latte")
        barista.add_message("Good luck saving campus!")



"""Main file for GV-ZORK. Starts the game."""

from game import Game


def main():
    """Creates and starts the game."""

    game = Game()

    #TO DO GROUP:
    #Replace this with game.play()
    #once the play() method is created.
    print("Game created successfully.")


if __name__ == "__main__":
    main()