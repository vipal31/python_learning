# traesure island game
print("*"*10 + "Welcome to the Treasure Island, your mission is to find the treasure" + "*"*10)

direction = input("Which way you would like to go? Left or right: ").lower()

if direction == "left":
    action = input('Would you like to Swim or wait? type "Swim" or "Wait": ').lower()
    if action == 'wait':
        door = input("Which door you would like to go? 'Read' or 'Blue' or 'Yellow': ").lower()
        if door == 'red':
            print("You are burned by fire, Game Over!")
        elif door == 'blue':
            print("Eaten by beasts, Game Over!")
        else:
            print("Hurray, You won!")
    else:
        print("You are attacked by Crocodile, Game Over!")
                
else:
    print("You faill in to the hole, Game Over, thanks for playing")
