print("Welcome to Treasure Island. Your mission is to find the treasure.")
direction = input("Where do you want to go? Left or Right?:")
dir = direction.lower()
if(dir == "left"):
    action = str(input("Do you want to swim across or wait for a boat? Swim or Wait?:"))
    act = action.lower()
    if(act == "wait"):
        color = input("Which door do you wish to choose? Red, Blue or Yellow?: ")
        door = color.lower()
        if(door == "yellow"):
            print("You Win!")
        else:
            print("Game Over")          
    else:
        print("Game Over")
else:
    print("Game Over")