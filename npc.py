#NPC Class for GV-ZORK: Sophia Brown
class NPC:
    def __init__(self, name: str, description: str):
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("NPC name cannot be blank.")

        if not isinstance(description, str) or description.strip() == "":
            raise ValueError("NPC description cannot be blank.")

        self._name = name  # making these protected and not private
        self._description = description
        self._messages = []  # empty list so we can go back later
        self._message_number = 0

    @property
    def name(self) -> str:  # having this be a string because it wouldn't be int
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("NPC name can't be blank.")
        self._name = value

    @property
    def description(self) -> str:
        return self._description  # I'm just doing all of them as protected let me know if thi is an issue

    @description.setter
    def description(self, value: str) -> None:
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("NPC description cannot be blank.")
        self._description = value

    @property
    def message_number(self) -> int:  # doing this as an int
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
            return "..."  # If the NPC has no messages, return a placeholder message, instead of causing an IndexError from accessing an empty because it kept giving me errors list.

        current_message = self._messages[self._message_number]

        self._message_number += 1

        if self._message_number >= len(self._messages):
            self._message_number = 0

        return current_message

    def __str__(self) -> str:
        return self._name
#NPC Class for GV-ZORK: Sophia Brown