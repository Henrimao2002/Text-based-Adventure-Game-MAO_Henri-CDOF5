# adventure_game.py

def start_game():
    print("Welcome to the Adventure Game!")
    print("Your journey begins in a dark forest. You can go 'left', 'right', or 'straight'.")
    choice = input("Which way will you go? ").lower()

    if choice == "left":
        left_path()
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
        print("The villagers share tales of an ancient artifact hidden in the mountains. Do you want to 'search' for it or 'stay'? ")
        choice = input("What will you do? ").lower()
        if choice == "search":
            print("You venture into the mountains and find the artifact, unlocking a new adventure. You are the ultimate hero! You win!")
        elif choice == "stay":
            print("You live peacefully in the village, enjoying your new life. You win!")
        else:
            print("Invalid choice. The villagers grow wary of you. Game Over.")
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
        print("However, you also hear a strange noise. Do you 'investigate' or 'leave'? ")
        choice = input("What will you do? ").lower()
        if choice == "investigate":
            print("You find a secret passage leading to an underground city. You win a new adventure!")
        elif choice == "leave":
            print("You leave with the treasure, safe and sound. You win!")
        else:
            print("Invalid choice. The cave collapses. Game Over.")
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
        print("The wizard asks if you'd like to learn a spell. Do you say 'yes' or 'no'? ")
        choice = input("What will you do? ").lower()
        if choice == "yes":
            print("You learn a powerful spell and become a renowned mage. You win a life of adventure!")
        elif choice == "no":
            print("You thank the wizard and continue your journey with the amulet. You win!")
        else:
            print("Invalid choice. The wizard vanishes in frustration. Game Over.")
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
