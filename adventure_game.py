# adventure_game.py

def start_game():
    print("Welcome to the Adventure Game!")
    print("Your journey begins in a dark forest. You can go 'left', 'right', or 'straight'.")
    choice = input("Which way will you go? ").lower()

    if choice == "left":
        left_path(
    elif choice == "right":
        right_path()
    elif choice == "straight":
        straight_path()
    else:
        print("Invalid choice. Try again.")
        start_game()

def left_path():
    print("You walk down the left path and encounter a river.")
    print("You can 'swim' across, 'build' a raft, or 'follow' the river downstream.")
    choice = input("What will you do? ").lower()

    if choice == "swim":
        print("You try to swim but the current is too strong. You drown. Game Over.")
    elif choice == "build":
        print("You build a raft and successfully cross the river.")
        print("On the other side, you find a village and are welcomed as a hero. You win!")
    elif choice == "follow":
        print("You follow the river downstream and find a waterfall. Hidden behind it is a cave with treasure. You win!")
    else:
        print("Invalid choice. Try again.")
        left_path()

def right_path():
    print("You walk down the right path and find a cave.")
    print("You can 'enter' the cave, 'keep walking', or 'climb' the rocks nearby.")
    choice = input("What will you do? ").lower()

    if choice == "enter":
        print("Inside the cave, you find a treasure chest. You win!")
    elif choice == "keep walking":
        print("You keep walking and fall into a trap. Game Over.")
    elif choice == "climb":
        print("You climb the rocks and discover a hidden plateau with ancient ruins. You win!")
    else:
        print("Invalid choice. Try again.")
        right_path()

def straight_path():
    print("You head straight into the forest and find a mysterious hut.")
    print("You can 'knock' on the door, 'sneak' around to the back, or 'ignore' it and keep going.")
    choice = input("What will you do? ").lower()

    if choice == "knock":
        print("A friendly wizard answers and gives you a magic amulet. You win!")
    elif choice == "sneak":
        print("You sneak around and find a bag of gold, but the wizard catches you. Game Over.")
    elif choice == "ignore":
        print("You keep going and stumble into a pack of wolves. Game Over.")
    else:
        print("Invalid choice. Try again.")
        straight_path()

# Start the game
if __name__ == "__main__":
    start_game()