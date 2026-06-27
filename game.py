#Game Class for GV-ZORK

import random
from datetime import datetime

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

        # creates the map, items, and NPCs
        self.create_world()

        # starts player in a random Location
        self._current_location = self.random_start_location()


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

        # Create locations
        library = Location(
            "Library",
            "A quiet building full of books and frozen students."
        )

        kirkhof = Location(
             "Kirkhof",
             "The student center with food, tables, and empty hallways."
        )

        padnos = Location(
            "Padnos",
            "Lots of science labs are in this building."
        )

        mackinac = Location(
            "Mackinac",
            "A classroom building with many confusing hallways."
        )

        ravines = Location(
            "Ravines",
            "The woods behind campus. The magical elf waits here."
        )

        rec_center = Location(
            "Rec Center",
            "A gym filled with frozen exercise equipment."
        )

        dorms = Location(
            "Dorms",
            "Student housing that feels strangely silent."
        )

        dining_hall = Location(
            "Dining Hall",
            "A place filled with snacks and abandoned plates."
        )

        bus_stop = Location(
            "Bus Stop",
            "The bus is frozen in place by the troll's spell."
        )

        clock_tower = Location(
            "Clock Tower",
            "The clock has stopped, frozen by strange magic."
        )

        self._elf_location = ravines

        # Connect locations
        library.add_location("east", kirkhof)
        kirkhof.add_location("west", library)

        kirkhof.add_location("north", mackinac)
        mackinac.add_location("south", kirkhof)

        kirkhof.add_location("east", padnos)
        padnos.add_location("west", kirkhof)

        padnos.add_location("north", rec_center)
        rec_center.add_location("south", padnos)

        library.add_location("north", dorms)
        dorms.add_location("south", library)

        dorms.add_location("east", dining_hall)
        dining_hall.add_location("west", dorms)

        dining_hall.add_location("south", kirkhof)
        kirkhof.add_location("northwest", dining_hall)

        mackinac.add_location("east", clock_tower)
        clock_tower.add_location("west", mackinac)

        clock_tower.add_location("north", bus_stop)
        bus_stop.add_location("south", clock_tower)

        rec_center.add_location("east", ravines)
        ravines.add_location("west", rec_center)

        # Add NPCs to locations.
        ravines.add_npc(elf)
        mackinac.add_npc(professor)
        library.add_npc(student)
        padnos.add_npc(janitor)
        dining_hall.add_npc(barista)

        # Place items in locations.
        items = self.create_items()

        dining_hall.add_item(items[0])   # Pizza Slice
        kirkhof.add_item(items[1])       # Burger
        library.add_item(items[2])       # Apple
        dorms.add_item(items[3])         # Bag of Chips
        dining_hall.add_item(items[4])   # Doughnut
        bus_stop.add_item(items[5])      # Energy Drink

        padnos.add_item(items[6])        # Rusty Nail
        mackinac.add_item(items[7])      # Textbook
        library.add_item(items[8])       # Laptop
        clock_tower.add_item(items[9])   # Bulldog Collar

        # Add Locations to the game.
        self._locations = [
            library,
            kirkhof,
            padnos,
            mackinac,
            ravines,
            rec_center,
            dorms,
            dining_hall,
            bus_stop,
            clock_tower
        ]

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
                if self._current_location == self._elf_location:

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

                        self.teleport_player()

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

        "map" : self.show_map,
        "search": self.search,

        "quit": self.quit,
        "exit": self.quit
    }
        return commands

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

    # Create random starting location.
    def random_start_location(self):
        """Returns a random starting location."""

        return random.choice(self._locations)
    
    def teleport_player(self):
        """Moves player to a random location."""

        self._current_location = random.choice(self._locations)
        print(f"You have been teleported to {self._current_location.name}!")


    def opening_screen(self):
        """Prints the intro story."""

        print("Welcome to GV-Zork!")
        print()
        print("A troll from Ferris has frozen GVSU in time.")
        print("To save campus, you must bring food to the elf")
        print("in the ravines behind campus.")
        print()
        print("If you feed the elf enough calories, campus is saved.")
        print("If you give the elf something inedible, you get teleported.")
        print()

    # /////////////
    # GROUP SECTION
    def play(self):
        """Runs the game loop."""

        self.opening_screen()
        self.help()
        self.look()

        while self._in_progress:
            response = input(
                "\nWhat is your command "
                "(type 'help' for instructions)? "
            )

            response = response.lower().strip()

            if response == "":
                print("Please enter a command.")
                continue

            tokens = response.split()
            command = tokens[0]
            del tokens[0]
            target = " ".join(tokens)

            if command in self._commands:
                self._commands[command](target)
            else:
                print("I don't understand that command.")

        if self._elf_calories_needed <= 0:
            print()
            print("The elf is appeased!")
            print("Campus begins to return to normal.")
            print("You saved GVSU!")
            print()

    def help(self, args=None):
        """Displays all valid commands."""

        current_time = datetime.now().strftime("%I:%M %p")

        print()
        print(f"Current time: {current_time}")
        print("Valid commands are:")

        for command in self._commands:
            print("-", command)

    def look(self, args=None):
        """Displays current location information."""

        print()
        print(f"Your location is: {self._current_location}")

        items = self._current_location.get_items()

        if len(items) == 0:
            print("There are no items here.")
        else:
            print("You see:")
            for item in items:
                print(f"- {item}")

        npcs = self._current_location.get_npcs()

        if len(npcs) == 0:
            print("You are alone.")
        else:
            print("People here:")
            for npc in npcs:
                print(f"- {npc}")

        print("From here you can go:")

        locations = self._current_location.get_locations()

        for direction in locations:
            neighbor = locations[direction]

            if neighbor.get_visited():
                print(f"- {direction} to {neighbor.name}")
            else:
                print(f"- {direction}")

    def show_map(self, args=None):
        """Custom command 1: shows visited map connections."""

        print("Nearby directions:")

        for direction in self._current_location.get_locations():
            print(f"- {direction}")

    def search(self, args=None):
        """Custom command 2: gives a small hint."""

        if self._current_location == self._elf_location:
            print("The elf is here. Try giving him edible food.")
        elif len(self._current_location.get_items()) > 0:
            print("You find items nearby. Try using look.")
        else:
            print("You search around, but find nothing new.")

    def quit(self, args=None):
        """Ends the game."""

        print()
        print("Thanks for playing! :)")
        print("Campus may need saving another day.")
        self._in_progress = False
