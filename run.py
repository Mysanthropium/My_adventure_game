print("Escape Room!\n\nHow to play: \n\nYou need to find the key to get out.")
print("You will start with 3 lives, whenever you reach 0, you're dead and GAME OVER.\n\n")

name = input("Enter your name to start the game:\n")
print(f'Welcome to the Escape Room, {name}!')

escape_room()




"""
Function for the players life. 
If player has 1 or more lives left, keep playing.
If player run out of lives, game over, print you're dead
"""
lives = [3]

def player_life():
    if lives < 1:
        print("You're Dead!")
    else:
        startGame()


"""
The game functions
"""

def escape_room():
    print("\nYou find yourself in a small room with no windows, only a door.\n\nYou see a closet, a chest, a bed, a lantern and a pitch black corner at the other end of the room")
    

def closet():
    print("You open the closet carefully...\n\nAll you see is some old shirts and a skateboard.")


    



