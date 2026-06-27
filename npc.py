"""NPC class for GV-ZORK.

Defines the NPC class used to represent non-player characters
that the player can meet and talk to throughout the game.
"""

# NPC Class for GV-ZORK: Sophia Brown


class NPC:
    """Represents a non-player character in GV-ZORK."""

    def __init__(self, name: str, description: str):
        """Creates a new NPC object."""

        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("NPC name cannot be blank.")

        if not isinstance(description, str) or description.strip() == "":
            raise ValueError("NPC description cannot be blank.")

        # Store the NPC's basic information.
        self._name = name
        self._description = description

        # Store the NPC's dialogue.
        self._messages = []

        # Track which message should be displayed next.
        self._message_number = 0

    @property
    def name(self) -> str:
        """Returns the NPC's name."""

        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Sets and validates the NPC's name."""

        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("NPC name can't be blank.")

        self._name = value

    @property
    def description(self) -> str:
        """Returns the NPC's description."""

        return self._description

    @description.setter
    def description(self, value: str) -> None:
        """Sets and validates the NPC's description."""

        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("NPC description cannot be blank.")

        self._description = value

    @property
    def message_number(self) -> int:
        """Returns the current message index."""

        return self._message_number

    @property
    def messages(self) -> list[str]:
        """Returns the NPC's list of messages."""

        return self._messages

    def add_message(self, message: str) -> None:
        """Adds a message to the NPC's dialogue."""

        if not isinstance(message, str) or message.strip() == "":
            raise ValueError("Message cannot be blank.")

        self._messages.append(message)

    def get_message(self) -> str:
        """Returns the next message from the NPC.

        Cycles through the NPC's messages in order.
        """

        # Return a placeholder if the NPC has no dialogue.
        if len(self._messages) == 0:
            return "..."

        # Get the current message.
        current_message = self._messages[self._message_number]

        # Move to the next message.
        self._message_number += 1

        # Restart at the beginning once all messages are shown.
        if self._message_number >= len(self._messages):
            self._message_number = 0

        return current_message

    def __str__(self) -> str:
        """Returns the NPC's name."""

        return self._name


# NPC Class for GV-ZORK: Sophia Brown