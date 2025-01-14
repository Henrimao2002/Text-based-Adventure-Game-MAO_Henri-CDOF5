# adventure_game.py

def start_game():
    print("Welcome to the Adventure Game!")
    print("Your journey begins in a dark forest. You can go 'left' or 'right'.")
    choice = input("Which way will you go? ").lower()

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Try again.")
        start_game()


def left_path():
    print("You walk down the left path and encounter a river.")
    print("You can 'swim' across or 'build' a raft.")
    choice = input("What will you do? ").lower()

    if choice == "swim":
        print("You try to swim but the current is too strong. You drown. Game Over.")
    elif choice == "build":
        print("You build a raft and successfully cross the river. You win!")
    else:
        print("Invalid choice. Try again.")
        left_path()


def right_path():
    print("You walk down the right path and find a cave.")
    print("You can 'enter' the cave or 'keep walking'.")
    choice = input("What will you do? ").lower()

    if choice == "enter":
        print("Inside the cave, you find a treasure chest. You win!")
    elif choice == "keep walking":
        print("You keep walking and fall into a trap. Game Over.")
    else:
        print("Invalid choice. Try again.")
        right_path()


# Start the game
if __name__ == "__main__":
    start_game()
