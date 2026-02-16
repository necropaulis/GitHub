import random

top_of_range  = input("Give a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("This is not a number I can work with")
        quit()
else:
    print("Type a number")
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1 
    user_guess =input("Give it a try: ")
    if user_guess.isdigit():
       user_guess = int(user_guess)
    else:
       print("Type a number")
       continue

    if user_guess == random_number:
        print("you got it")
        break
    elif user_guess > random_number:
        print("Too hot")
    else:
        print("Too cold")  
              
print("You got it in", guesses, "guesses")
        
        