import random

# Character classes with unique stats
class Character:
    """
    Represents a player character in the RPG game with unique stats 
    based on their chosen character class.
    """
    def __init__(self, name, char_class):
        """
        Initializes a new character with basic attributes.

        :param name: The character's name
        :param char_class: The character's class (Warrior, Mage, or Rogue)
        """
        self.name = name
        self.char_class = char_class
        self.level = 1
        self.experience = 0
        self.inventory = []
        self.stats = {
            "Strength": 0,
            "Agility": 0,
            "Magic": 0,
            "HP": 100
        }
        self.set_stats()

    def set_stats(self):
        """Sets the character's stats based on their class."""
        if self.char_class == "Warrior":
            self.stats["Strength"] = 15
            self.stats["Agility"] = 10
            self.stats["Magic"] = 5
        elif self.char_class == "Mage":
            self.stats["Strength"] = 5
            self.stats["Agility"] = 8
            self.stats["Magic"] = 15
        elif self.char_class == "Rogue":
            self.stats["Strength"] = 10
            self.stats["Agility"] = 15
            self.stats["Magic"] = 5

    def show_stats(self):
        """Displays the character's stats and inventory."""
        print(f"\n{self.name} the {self.char_class} - Stats:")
        print(f"Level: {self.level}")
        for stat, value in self.stats.items():
            print(f"{stat}: {value}")
        print("\nInventory:", self.inventory)

    def attack(self):
        """Calculates the damage dealt based on character's class and stats."""
        base_damage = random.randint(5, 10)
        if self.char_class == "Warrior":
            damage = base_damage + self.stats["Strength"]
        elif self.char_class == "Mage":
            damage = base_damage + self.stats["Magic"]
        elif self.char_class == "Rogue":
            damage = base_damage + self.stats["Agility"]
        return damage

    def defend(self):
        """Calculates the defense value for damage reduction."""
        defense_value = random.randint(3, 7)
        print(f"{self.name} defends, reducing damage by {defense_value} points!")
        return defense_value

    def level_up(self):
        """Levels up the character, improving their stats."""
        self.level += 1
        self.stats["Strength"] += 2
        self.stats["Agility"] += 2
        self.stats["Magic"] += 2
        self.stats["HP"] += 10
        print(f"\nCongratulations! {self.name} leveled up to Level {self.level}!")
        print("Your stats have increased!")

    def gain_experience(self, points):
        """
        Adds experience points and levels up if enough experience is gained.

        :param points: Experience points to add
        """
        self.experience += points
        print(f"{self.name} gained {points} experience!")
        if self.experience >= 10:  # Example level-up threshold
            self.level_up()
            self.experience = 0  # Reset experience after leveling up

# Monster class with varying difficulty levels
class Monster:
    """
    Represents a monster with different ranks that determine difficulty.
    """
    def __init__(self, name, rank):
        """
        Initializes a monster with its name, rank, and stats.

        :param name: The monster's name
        :param rank: The monster's difficulty rank
        """
        self.name = name
        self.rank = rank
        self.stats = {
            "Strength": 5 * rank,
            "HP": 20 * rank
        }
        self.drop_item = random.choice(["Potion", "Elixir", "Magic Scroll"]) if rank > 1 else None

    def attack(self, player_strength):
        """
        Calculates the monster's attack damage against the player.

        :param player_strength: The player's strength for calculating damage reduction
        :return: The effective damage after applying player's strength-based reduction
        """
        base_damage = random.randint(3, 6) + (self.rank * 2)
        reduced_damage = max(1, base_damage - (player_strength // 4))
        return reduced_damage

# Game Locations class
class Location:
    """
    Represents a game location with a unique challenge, items, and possible endings.
    """
    def __init__(self, name, description, challenge, items, possible_endings):
        """
        Initializes the location with its name, description, and other attributes.

        :param name: The name of the location
        :param description: A brief description of the location
        :param challenge: The main challenge associated with the location
        :param items: List of items that can be found here
        :param possible_endings: Possible outcomes for the location
        """
        self.name = name
        self.description = description
        self.challenge = challenge
        self.items = items
        self.possible_endings = possible_endings

    def enter_location(self):
        """Handles the actions when a player enters the location."""
        print(f"\nEntering {self.name}...")
        print(self.description)
        print(self.challenge)
        if self.items:
            print(f"You found items: {self.items}")
        return self.make_choices()

    def make_choices(self):
        """Displays choices and returns the result of the player's choice."""
        print("\nYou have several choices:")
        print("1. Continue the challenge")
        print("2. Explore more")
        print("3. Leave the location")

        choice = input("What will you do? ").strip()

        if choice == "1":
            return self.handle_challenge()
        elif choice == "2":
            return self.handle_exploration()
        elif choice == "3":
            self.handle_leave()
        else:
            print("Invalid choice. Try again.")
            return self.make_choices()

    def handle_challenge(self):
        """Handles the main challenge within the location."""
        print("You choose to face the challenge head-on!")
        if random.choice([True, False]):
            print("A monster appears! Prepare for battle.")
            return "monster"
        else:
            print("You overcome the challenge and gain treasure!")
            if self.items:
                print(f"You found {random.choice(self.items)}!")
            self.end_location()

    def handle_exploration(self):
        """Handles further exploration within the location."""
        print("You decide to explore further.")
        if random.choice([True, False]):
            print("You find a hidden passage!")
            self.end_location()
        else:
            print("You find nothing and return to your path.")
            return self.make_choices()

    def handle_leave(self):
        """Handles leaving the location."""
        print("You decide to leave the location.")
        self.end_location()

    def end_location(self):
        """Ends the location sequence and displays a random ending."""
        print("\nThe location has come to an end.")
        print("Your adventure continues...")
        self.trigger_ending()

    def trigger_ending(self):
        """Selects and displays a random ending from possible endings."""
        ending = random.choice(self.possible_endings)
        print(f"\nEnding: {ending}")

# Main Game Class
class Game:
    """
    Represents the main game logic, handling player interactions and location exploration.
    """
    def __init__(self, player):
        """
        Initializes the game with a player and available locations.

        :param player: The player's character
        """
        self.player = player
        self.locations = {
            "Dragon's Lair": Location(
                "Dragon's Lair",
                "A terrifying cave filled with smoke and the scent of fire.",
                "Defeat the Dragon and claim its treasure.",
                ["Gold Chest", "Dragon Scale"],
                [
                    "You bravely slay the dragon and take its hoard, becoming the hero of the land.",
                    "You attempt to fight the dragon but are overwhelmed. Your adventure ends here.",
                    "You discover the dragon's weakness and escape with its treasure, becoming a legend."
                ]
            ),
            "The Black Forest": Location(
                "The Black Forest",
                "A dense, eerie forest with creatures lurking in the shadows.",
                "Survive the forest and defeat the mythical beasts.",
                ["Healing Herb", "Enchanted Leaf"],
                [
                    "You survive the forest's dangers and become the guardian of its secrets.",
                    "The creatures of the forest overpower you. Your journey ends here.",
                    "You discover an ancient relic hidden in the forest, gaining great power."
                ]
            ),
            "King's Castle": Location(
                "King's Castle",
                "A grand castle, now threatened by traitorous nobles.",
                "Defeat the traitors and restore the kingdom.",
                ["Royal Sword", "Crown of the King"],
                [
                    "You defeat the traitors and restore peace to the kingdom, becoming a hero.",
                    "You fail to defeat the traitors and are betrayed. The kingdom falls into ruin.",
                    "You uncover the real plot behind the treason and expose the truth, saving the kingdom."
                ]
            ),
        }
        self.current_monster = None

    def start_game(self):
        """Begins the game and displays initial player stats."""
        print("Welcome to the RPG Adventure!")
        self.player.show_stats()
        self.choose_action()

    def choose_action(self):
        """Main loop for player actions during the game."""
        while True:
            if self.player.stats["HP"] <= 0:
                print("\nYou have been defeated! Game over.")
                print("The only option now is to 'Quit'.")
                action = input("What would you like to do? ").strip().lower()
                if action == "quit":
                    print("Exiting game. Goodbye!")
                    break
                else:
                    print("Invalid command. Please try again.")
                continue

            if self.current_monster is not None:
                print("\nActions: 'Attack', 'Defend', 'Check Stats', 'Quit'")
                action = input("What would you like to do? ").strip().lower()
                if action == "attack":
                    self.battle(self.current_monster, action)
                elif action == "defend":
                    self.battle(self.current_monster, action)
                elif action == "check stats":
                    self.player.show_stats()
                elif action == "quit":
                    print("Exiting game. Goodbye!")
                    break
                else:
                    print("Invalid command. Please try again.")
            else:
                print("\nActions: 'Explore', 'Check Stats', 'Inventory', 'Quit'")
                action = input("What would you like to do? ").strip().lower()
                if action == "explore":
                    self.explore()
                elif action == "check stats":
                    self.player.show_stats()
                elif action == "inventory":
                    print("Inventory:", self.player.inventory)
                elif action == "quit":
                    print("Exiting game. Goodbye!")
                    break
                else:
                    print("Invalid command. Please try again")

    def explore(self):
        """Allows the player to choose a location to explore."""
        print("\nChoose a location to explore:")
        for i, location in enumerate(self.locations.keys(), 1):
            print(f"{i}. {location}")

        choice = input("Enter the number of the location you want to explore: ").strip()
        try:
            choice_index = int(choice) - 1
            location_name = list(self.locations.keys())[choice_index]
            location = self.locations[location_name]
            result = location.enter_location()

            if result == "monster":
                self.current_monster = Monster(location_name + " Monster", random.randint(1, 3))
                print(f"A {self.current_monster.name} has appeared!")
            else:
                self.current_monster = None

        except (IndexError, ValueError):
            print("Invalid choice. Try again.")
            self.explore()

    def battle(self, monster, action):
        """
        Handles the battle logic between the player and a monster.

        :param monster: The current monster the player is battling
        :param action: The player's chosen action ('attack' or 'defend')
        """
        if action == "attack":
            damage = self.player.attack()
            print(f"{self.player.name} attacks and deals {damage} damage!")
            monster.stats["HP"] -= damage
            if monster.stats["HP"] <= 0:
                print(f"The {monster.name} is defeated!")
                self.player.gain_experience(monster.rank * 2)
                if monster.drop_item:
                    self.player.inventory.append(monster.drop_item)
                    print(f"You found a {monster.drop_item}!")
                self.current_monster = None
            else:
                self.monster_attack(monster)
        elif action == "defend":
            defense_value = self.player.defend()
            self.monster_attack(monster, defense_value)

    def monster_attack(self, monster, defense_value=0):
        """
        Handles the monster's attack on the player.

        :param monster: The monster attacking the player
        :param defense_value: Defense points to reduce the incoming damage
        """
        monster_damage = monster.attack(self.player.stats["Strength"])
        effective_damage = max(0, monster_damage - defense_value)
        self.player.stats["HP"] -= effective_damage
        print(f"The {monster.name} attacks and deals {effective_damage} damage!")
        if self.player.stats["HP"] <= 0:
            print("\nYou have been defeated! Game over.")

# Main game setup and start
def main():
    """
    Main function to start the game.
    Prompts the player for their character's name and class, then begins the game.
    """
    name = input("Enter your character's name: ")
    char_class = input("Choose your class (Warrior, Mage, Rogue): ").capitalize()
    if char_class not in ["Warrior", "Mage", "Rogue"]:
        print("Invalid class. Defaulting to Warrior.")
        char_class = "Warrior"

    player = Character(name, char_class)
    game = Game(player)
    game.start_game()

if __name__ == "__main__":
    main()
