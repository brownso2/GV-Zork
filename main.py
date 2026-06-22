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
   
class Location:
    '''Represents a location the player can visit in GV-Zork.'''

    def __init__(self, name: str, description: str) -> None:

        # Make sure the location has a valid name.
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Location name cannot be blank.")

        # Make sure the location has a valid description.
        if not isinstance(description, str) or description.strip() == "":
            raise ValueError("Location description cannot be blank.")

        # Store basic information.
        self._name = name
        self._description = description

        # Keeps track of whether the player has visited.
        self._visited = False

        # Dictionary of neighboring locations.
        # Example:
        # {'north': library, 'east': kirkhof}
        self._neighbors = {}

        # List that will hold Item objects.
        self._items = []

        # List that will hold NPC objects.
        self._npcs = []


    # Read Properties
    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description


    # Neighbor Functions
    def get_locations(self) -> dict[str, "Location"]:
        '''Returns the dictionary of neighboring locations.'''

        return self._neighbors


    def add_location(self, direction: str, location: "Location") -> None:
        '''Adds a neighboring location.'''

        # Direction cannot be empty.
        if not isinstance(direction, str) or direction.strip() == "":
            raise ValueError("Direction cannot be blank.")

        # Verify the object being added is a Location.
        if not isinstance(location, Location):
            raise ValueError( "Location must be a Location object.")

        # Make all directions lowercase.
        direction = direction.lower()

        # Prevent duplicate directions.
        if direction in self._neighbors:
            raise KeyError("That direction already exists.")

        # Add the new location.
        self._neighbors[direction] = location


    # Item Functions
    def add_item(self, item) -> None:
        '''Adds an item to this location.'''

        self._items.append(item)


    def remove_item(self, item) -> None:
        '''Removes an item from this location.'''

        if item in self._items:
            self._items.remove(item)


    def get_items(self) -> list:
        '''Returns all items in this location.'''

        return self._items


    # NPC Functions
    def add_npc(self, npc) -> None:
        '''Adds an NPC to this location.'''

        self._npcs.append(npc)


    def get_npcs(self) -> list:
        '''Returns all NPCs in this location.'''

        return self._npcs


    # Visited Functions
    def set_visited(self) -> None:
        '''Marks the location as visited.'''

        # Once True, it stays True.
        self._visited = True


    def get_visited(self) -> bool:
        '''Returns the visited status.'''

        return self._visited


    # String Function
    def __str__(self) -> str:
        '''Returns the location name and description.'''

        return (f"{self._name} - " f"{self._description}")