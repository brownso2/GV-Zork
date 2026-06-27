"""Location class for GV-ZORK.

Defines the Location class used to represent areas that the
player can explore throughout the game.
"""

# Location Class for GV-ZORK: Mia Phillips


class Location:
    """Represents a location the player can visit in GV-ZORK."""

    def __init__(self, name: str, description: str) -> None:
        """Creates a new Location object."""

        # Make sure the location has a valid name.
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Location name cannot be blank.")

        # Make sure the location has a valid description.
        if not isinstance(description, str) or description.strip() == "":
            raise ValueError("Location description cannot be blank.")

        # Store the location's basic information.
        self._name = name
        self._description = description

        # Track whether the player has visited this location.
        self._visited = False

        # Store neighboring locations.
        # Example:
        # {"north": library, "east": kirkhof}
        self._neighbors = {}

        # Store all Item objects in this location.
        self._items = []

        # Store all NPC objects in this location.
        self._npcs = []

    # --------------------------------------------------
    # Read Properties
    # --------------------------------------------------

    @property
    def name(self) -> str:
        """Returns the location's name."""

        return self._name

    @property
    def description(self) -> str:
        """Returns the location's description."""

        return self._description

    # --------------------------------------------------
    # Neighbor Functions
    # --------------------------------------------------

    def get_locations(self) -> dict[str, "Location"]:
        """Returns the neighboring locations."""

        return self._neighbors

    def add_location(self, direction: str, location: "Location") -> None:
        """Adds a neighboring location."""

        # Direction cannot be blank.
        if not isinstance(direction, str) or direction.strip() == "":
            raise ValueError("Direction cannot be blank.")

        # Verify that the object is a Location.
        if not isinstance(location, Location):
            raise ValueError("Location must be a Location object.")

        # Convert directions to lowercase.
        direction = direction.lower()

        # Prevent duplicate directions.
        if direction in self._neighbors:
            raise KeyError("That direction already exists.")

        # Add the neighboring location.
        self._neighbors[direction] = location

    # --------------------------------------------------
    # Item Functions
    # --------------------------------------------------

    def add_item(self, item) -> None:
        """Adds an item to this location."""

        self._items.append(item)

    def remove_item(self, item) -> None:
        """Removes an item from this location."""

        if item in self._items:
            self._items.remove(item)

    def get_items(self) -> list:
        """Returns all items in this location."""

        return self._items

    # --------------------------------------------------
    # NPC Functions
    # --------------------------------------------------

    def add_npc(self, npc) -> None:
        """Adds an NPC to this location."""

        self._npcs.append(npc)

    def get_npcs(self) -> list:
        """Returns all NPCs in this location."""

        return self._npcs

    # --------------------------------------------------
    # Visited Functions
    # --------------------------------------------------

    def set_visited(self) -> None:
        """Marks the location as visited."""

        # Once a location is visited, it remains visited.
        self._visited = True

    def get_visited(self) -> bool:
        """Returns whether the location has been visited."""

        return self._visited

    # --------------------------------------------------
    # String Function
    # --------------------------------------------------

    def __str__(self) -> str:
        """Returns the location's name and description."""

        return f"{self._name} - {self._description}"


# Location Class for GV-ZORK: Mia Phillips
