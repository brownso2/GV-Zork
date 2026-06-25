#Game Class for GV-ZORK

from item import Item
from location import Location
from npc import NPC

#(SOFIE)
class Game:
    """Main game class for GV-ZORK.
    Controls inventory, item handling, and elf calories."""


    def __init__(self):
        #stores items the player is carrying.
        self._inventory = []

        #tracks the total weight of carried items.
        self._current_weight = 0

        #calories still needed by the elf.
        self._elf_calories_needed = 500

        #stores all locations in the game.
        self._locations = []

        #stores the player's current location.
        self._current_location = None

        #controls whether the game is running.
        self._in_progress = True

        #sophia's command dictionary.
        self._commands = self.setup_commands()

    # /////////////
    #WORLD CREATION (SOPHIA)
    """Creates NPCs, locations, and places
     everything into the game world."""

    def create_world(self):

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

    # TODO MIA:
    # Create locations, connect locations.
    # Add NPCs to locations.
    # Place items in locations.
    # Create random starting location.

    # /////////////
    #SOFIE'S SECTION

    def take(self, target: str) -> None:

        #check every item in the current room.
        for item in self._current_location.get_items():
            if item.name.lower() == target.lower():

                if self._current_weight + item.weight > 30:
                    print("You can't carry that much weight.")
                    return

                #add item to inventory.
                self._inventory.append(item)

                #update weight.
                self._current_weight += item.weight

                #remove item from room.
                self._current_location.remove_item(item)

                print(f"You picked up {item.name}.")
                return

        print("That item is not here.")

    def give(self, target: str) -> None:
        """Removes an item from inventory.
        If the player is with the elf, the item is given to the elf.
        Otherwise, it is dropped and left in the room."""

        #search inventory for the requested item.
        for item in self._inventory:

            if item.name.lower() == target.lower():

                #remove from inventory.
                self._inventory.remove(item)

                self._current_weight -= item.weight

                # TODO MIA:
                #Replace "woods" with actual elf location.
                if self._current_location.name.lower() == "woods":

                    #feed food items to the elf, only food items have calories.
                    if item.calories > 0:

                        self._elf_calories_needed -= item.calories

                        print(
                            f"The elf eats the {item.name}."
                        )

                        print(
                            f"Calories still needed: "
                            f"{self._elf_calories_needed}"
                        )

                        #check if the elf has enough food.
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

                    #drop item in current room.
                    self._current_location.add_item(item)

                    print(
                        f"You dropped {item.name}."
                    )
                return

        print("You do not have that item.")

    def show_items(self) -> None:

        #show the current weight carried.
        print(
            f"Current weight: "
            f"{self._current_weight}/30 lbs"
        )

        #check for an empty inventory.
        if len(self._inventory) == 0:
            print("Inventory is empty.")
            return

        print("Inventory:")

        #display every item being carried.
        for item in self._inventory:
            print(f"- {item}")

#ITEM CREATION (SOFIE)
    def create_items(self):

        #food items that can be fed to the elf.
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

        #non-food items.
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
    # SOPHIA'S SECTION

    def setup_commands(self) -> dict: #btw some of this is stealing from Mia's class so it may need a super_init or something to stop the underlines once Mia writes it
        """Creates command dictionary."""

        commands = {
        "help": self.help,
        "?": self.help,

        "look": self.look,

        "go": self.go,
        "leave": self.go,

        "take": self.take,
        "get": self.take,
        "grab": self.take,
        "pickup": self.take,

        "give": self.give,
        "drop": self.give,
        "toss": self.give,

        "items": self.show_items,
        "inventory": self.show_items,

        "talk": self.talk,
        "meet": self.meet,

        "quit": self.quit,
        "exit": self.quit
    }
        return commands

#I am going to over explain myself here because I want to make sure everyone understand what I'm doing because it took me hours
    def help(self, args=None):
    #this displays all the valid commands 
        print("Valid commands are:")
        for command in self._commands:
            print("-", command) #running it as a for loop so it'll print them out at once

    def go(self, target: str) -> None:
   #trying to attempt moving the player to a new location

    # Marking this location as visited:
        self._current_location.set_visited()
    # Check if one of the directions exists:
        locations = self._current_location.get_locations()

        if target.lower() in locations:
            self._current_location = locations[target.lower()] #this moves the player
            print(f"You are now in {self._current_location}.")

        else:
            print("Sorry, you can't go that way.")

    # talk()
    def talk(self, target: str) -> None:
        for npc in self._current_location.get_npcs(): #checks everybody
            if npc.name.lower() == target.lower():
                print(npc.get_message()) #this is checking to make sure everybody is there
                return
            print("They are not here.")

    # meet()
    def meet(self, target: str) -> None:
         for npc in self._current_location.get_npcs():
             if npc.name.lower() == target.lower():
                 print(npc.description)
                 return
         print("They're not here.")


    # /////////////
    # MIA'S SECTION

    # TODO MIA:
    # opening_screen()

    # TODO MIA:
    # random_start_location()

    # TODO MIA:
    # teleport_player()

    # /////////////
    # GROUP SECTION
    def quit(self, args=None):
        """Ends the game."""

        print("Thanks for playing! :)")
        self._in_progress = False

    # TODO:
    # play()

    # TODO:
    # win condition

    # TODO:
    # loss condition

    # TODO:
    # custom command #1

    # TODO:
    # custom command #2