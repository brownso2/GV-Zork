#Game Class for GV-ZORK

from item import Item
from location import Location
from npc import NPC


class Game:
    """Main game class for GV-ZORK.
    Controls inventory, item handling, and elf calories."""


    def __init__(self):
        #Stores items the player is carrying.
        self._inventory = []

        #Tracks the total weight of carried items.
        self._current_weight = 0

        #Calories still needed by the elf.
        self._elf_calories_needed = 500

        #Stores all locations in the game.
        self._locations = []

        #Stores the player's current location.
        self._current_location = None

        #Controls whether the game is running.
        self._in_progress = True

        # TODO SOPHIA:
        #Create command dictionary.
        self._commands = {}

        # TODO MIA:
        #Create world and starting location.

    # /////////////
    #SOFIE'S SECTION

    def take(self, target: str) -> None:
        """Picks up an item from the current location
        and adds it to the player's inventory."""

        #Check every item in the current room.
        for item in self._current_location.get_items():
            # Look for a matching item name.
            if item.name.lower() == target.lower():

                if self._current_weight + item.weight > 30:
                    print("You can't carry that much weight.")
                    return

                #Add item to inventory.
                self._inventory.append(item)

                #Update weight.
                self._current_weight += item.weight

                #Remove item from room.
                self._current_location.remove_item(item)

                print(f"You picked up {item.name}.")
                return

        print("That item is not here.")

    def give(self, target: str) -> None:
        """Removes an item from inventory.
        If the player is with the elf, the item is given to the elf.
        Otherwise, it is dropped and left in the room."""

        #Search inventory for the requested item.
        for item in self._inventory:

            if item.name.lower() == target.lower():

                #Remove from inventory.
                self._inventory.remove(item)

                #Update weight.
                self._current_weight -= item.weight

                # TODO MIA:
                #Replace "woods" with actual elf location.
                if self._current_location.name.lower() == "woods":

                    #Feed food items to the elf, only food items have calories.
                    if item.calories > 0:

                        self._elf_calories_needed -= item.calories

                        print(
                            f"The elf eats the {item.name}."
                        )

                        print(
                            f"Calories still needed: "
                            f"{self._elf_calories_needed}"
                        )

                        #Check if the elf has enough food.
                        if self._elf_calories_needed <= 0:

                            print(
                                "The elf has enough food! :D"
                            )

                            self._in_progress = False

                    else:
                        print(
                            "The elf refuses to eat that."
                        )

                        # TODO MIA:
                        #Teleport player to random location.

                else:

                    #Drop item in current room.
                    self._current_location.add_item(item)

                    print(
                        f"You dropped {item.name}."
                    )
                return

        #Item was not found in inventory.
        print("You do not have that item.")

    def show_items(self) -> None:
        """Displays the player's inventory."""

        #Show current weight carried.
        print(
            f"Current weight: "
            f"{self._current_weight}/30 lbs"
        )

        #Check for an empty inventory.
        if len(self._inventory) == 0:
            print("Inventory is empty.")
            return

        print("Inventory:")

        #Display every item being carried.
        for item in self._inventory:
            print(f"- {item}")

#ITEM CREATION
    def create_items(self):
        """Creates all items used in the game."""

        #Food items that can be fed to the elf.
        pizza = Item(
            "Pizza Slice",
            "A greasy slice of pizza.",
            300,
            2
        )

        burger = Item(
            "Burger",
            "A cheeseburger.",
            450,
            3
        )

        apple = Item(
            "Apple",
            "A fresh apple.",
            95,
            1
        )

        chips = Item(
            "Bag of Chips",
            "A salty snack.",
            200,
            1
        )

        doughnut = Item(
            "Doughnut",
            "A glazed doughnut.",
            250,
            1
        )

        energy_drink = Item(
            "Energy Drink",
            "Keeps students awake.",
            150,
            1
        )

        #Non-food items.
        rusty_nail = Item(
            "Rusty Nail",
            "A rusty nail.",
            0,
            1
        )

        textbook = Item(
            "Textbook",
            "A heavy school textbook.",
            0,
            8
        )

        laptop = Item(
            "Laptop",
            "A student's laptop.",
            0,
            5
        )

        bulldog_collar = Item(
            "Bulldog Collar",
            "Brutus's missing collar.",
            0,
            2
        )

        return [
            pizza,
            burger,
            apple,
            chips,
            doughnut,
            energy_drink,
            rusty_nail,
            textbook,
            laptop,
            bulldog_collar
        ]

    # /////////////
    # MIA'S SECTION


    # TODO MIA:
    # create_world()

    # TODO MIA:
    # connect_locations()

    # TODO MIA:
    # opening_screen()

    # TODO MIA:
    # look()

    # TODO MIA:
    # random_start_location()

    # TODO MIA:
    # teleport_player()

    # /////////////
    # SOPHIA'S SECTION


    # TODO SOPHIA:
    # setup_commands()

    # TODO SOPHIA:
    # help()

    # TODO SOPHIA:
    # go()

    # TODO SOPHIA:
    # talk()

    # TODO SOPHIA:
    # meet()

    # TODO SOPHIA:
    # command aliases

    # /////////////
    # GROUP SECTION


    # TODO:
    # play()

    # TODO:
    # quit()

    # TODO:
    # custom command #1

    # TODO:
    # custom command #2