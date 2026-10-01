class MagicCard:
    DEFAULT_SET = "Core Set"

    COLORS = ("White", "Blue", "Black", "Red", "Green")
    CARD_TYPES = (
        "Creature", "Instant", "Sorcery", "Artifact",
        "Enchantment", "Land", "Planeswalker", "Battle"
    )
    RARITIES = ("Common", "Uncommon", "Rare", "Mythic Rare")
    STARTING_LIFE_TOTAL = 20
    MAX_HAND_SIZE = 7
    MIN_CONSTRUCTED_DECK_SIZE = 60

    def __init__(self, card_name, mana_cost, type_line, rules_text, flavor_text, power_toughness, DEFAULT_SET=None):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.type_line = type_line
        self.rules_text = rules_text
        self.flavor_text = flavor_text
        self.power_toughness = power_toughness

        if DEFAULT_SET is None:
            self.DEFAULT_SET = MagicCard.DEFAULT_SET
        else:
            self.DEFAULT_SET = DEFAULT_SET

    def display_card(self):
        print("-" * 100)
        print(f"Card Name: {self.card_name}")
        print(f"Mana Cost: {self.mana_cost}")
        print(f"Type Line: {self.type_line}")
        print(f"Rules Text: {self.rules_text}")
        print(f"Flavor Text: {self.flavor_text}")
        print(f"Power/Toughness: {self.power_toughness}")
        print(f"Default Set: {self.DEFAULT_SET}")
        print("-" * 100)


card_1 = MagicCard(
    "Thornscape Battlemage",
    "2",
    "Creature - Human Wizard",
    "Kicker {2} (You may pay an additional 2 as you cast this spell.) "
    "If this spell was kicked, destroy target enchantment.",
    "Balance is a discipline as much as a philosophy.",
    "2/2"
)

card_1.DEFAULT_SET = "Object Oriented Programming"

card_2 = MagicCard(
    "Winter, Misanthropic Guide",
    "4",
    "Legendary Creature - Human Advisor",
    "Whenever Winter attacks, defending player mills two cards. "
    "You may cast a card milled this way this turn.",
    "The cold doesn't lie to you. People do.",
    "3/4"
)


def main():
    global input_user_name

    print("-" * 100)
    input_user_name = input("Enter your name: ")
    print(f"Welcome, {input_user_name}!")
    print("-" * 100)

    print("-" * 100)
    print("ATTRIBUTE SHADOWING")
    print("-" * 100)

    print(f"Class DEFAULT_SET:  {MagicCard.DEFAULT_SET}")
    print(f"Card 1 DEFAULT_SET: {card_1.DEFAULT_SET}")
    print(f"Card 2 DEFAULT_SET: {card_2.DEFAULT_SET}")

    print("-" * 100)
    print("GAME RULES (shared class attributes)")
    print("-" * 100)

    print(f"Colors:                  {', '.join(MagicCard.COLORS)}")
    print(f"Card Types:              {', '.join(MagicCard.CARD_TYPES)}")
    print(f"Rarities:                {', '.join(MagicCard.RARITIES)}")
    print(f"Starting Life Total:     {MagicCard.STARTING_LIFE_TOTAL}")
    print(f"Max Hand Size:           {MagicCard.MAX_HAND_SIZE}")
    print(f"Min Constructed Deck:    {MagicCard.MIN_CONSTRUCTED_DECK_SIZE} cards")

    print("-" * 100)

    print("Available Characters:")

    print("Character 1:")
    card_1.display_card()

    print("Character 2:")
    card_2.display_card()


def choose_character():
    while True:
        print("-" * 100)

        choice = input(
            "Choose a character (character_1 or character_2): "
        ).lower()

        if choice == "character_1" or choice == "1":
            print("You selected Thornscape Battlemage!")
            card_1.display_card()
            break

        elif choice == "character_2" or choice == "2":
            print("You selected Winter, Misanthropic Guide!")
            card_2.display_card()
            break

        else:
            print(
                "Invalid choice. Please choose either "
                "'character_1' or 'character_2'."
            )


def start_game():
    global Health
    global Opponent_Health
    global card_in_hand
    global Opponent_card_in_hand
    global opponent_name

    Health = MagicCard.STARTING_LIFE_TOTAL
    Opponent_Health = MagicCard.STARTING_LIFE_TOTAL
    card_in_hand = MagicCard.MAX_HAND_SIZE - 2
    Opponent_card_in_hand = MagicCard.MAX_HAND_SIZE - 2
    opponent_name = "Terrorblade"


def players_status():
    print("-" * 100)
    print(f"{input_user_name}'s Health: {Health}")
    print(f"{opponent_name}'s Health: {Opponent_Health}")
    print(f"{input_user_name}'s Cards in Hand: {card_in_hand}")
    print(f"{opponent_name}'s Cards in Hand: {Opponent_card_in_hand}")
    print("-" * 100)


def play_turn():
    global Health
    global Opponent_Health
    global card_in_hand
    global Opponent_card_in_hand

    while True:
        print("Choose an action:")
        print("1. Declare Attacker")
        print("2. Block")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            Opponent_Health -= 3

            if Opponent_card_in_hand > 0:
                Opponent_card_in_hand -= 1

            print(
                "You declare an attacker and your opponent "
                "receives 3 damage!"
            )
            break

        elif choice == "2":
            Health -= 2

            if card_in_hand > 0:
                card_in_hand -= 1

            print(
                "You declare a blocker and you receive 2 damage!"
            )
            break

        else:
            print(
                "Invalid choice. Please choose either '1' or '2'."
            )

    print("-" * 100)
    print("Updated Game Status:")
    players_status()


def check_winner():
    if Health <= 0:
        print(f"{input_user_name} has been defeated!")
        print("Better luck next time!")
        return True

    if Opponent_Health <= 0:
        print(f"{opponent_name} has been defeated!")
        print("Congratulations! You win the game!")
        return True

    return False


def continuation():
    while True:
        if check_winner():
            return

        choice = input(
            "Do you want to continue playing? (yes / no): "
        ).lower()

        if choice == "yes":
            play_turn()

        elif choice == "no":
            print("Thank you for playing!")
            return

        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
    choose_character()
    start_game()
    players_status()
    play_turn()
    continuation()