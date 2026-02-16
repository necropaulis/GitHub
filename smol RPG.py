name = input("Type your name ")
print("Welcome ", name, "to this adventure!")

answer = input("You are on a dirt road, and can go left of right, which way are you going to go? ").lower()

if answer == "left":
    answer = input ("You come to a river, you can walk around, or swim across. Type 'walk' to walk around, or 'swim' to swim across: ").lower()
    
    if answer == "swim":
        print("Surprise, you can't swim!")
        
    elif answer == "walk":
        print("you died of thirst, bring water next time")

    else:
        print("Not valid")
    

elif answer == "right":
    answer = input ("You come to a bridge, there's a troll. You can run, or you can fight. Type 'run' to run or 'fight' to fight: ").lower()
    
    if answer == "run":
        print("You run for the woods, and get eaten by wolves!")
        
    elif answer == "fight":
        print("You die. That's a troll, man!")

    else:
        print("Not valid")

else:
    print("Not Valid, try again")

print("The game was rigged from the start")