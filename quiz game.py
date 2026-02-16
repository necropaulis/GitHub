print("Welcome to my computer quiz!")

playing = input("Would you like to play a game? ")

if playing.lower() != "yes":
    quit()

print("Okay, let's play")
score = 0

answer = input("What does CPU stand for? ")
if answer.title() == "Central Processing Unit":
    print("Good job!")
    score += 1
else:
    print("WRONG")

answer = input("What does RAM stand for? ")
if answer.title() == "Random Access Memory":
    print("Nice!")
    score += 1
else:
    print("WRONG")

answer = input("What does GPU stand for? ")
if answer.title() == "Graphical Processing Unit":
    print("Sweet!")
    score += 1 
else:
    print("WRONG")

answer = input("What does ROM stand for? ")
if answer.title() == "Read Only Memory":
    print("Good job!")
    score += 1
else:
    print("All Done")

print("You got " + str(score) + " questions corect!")
print("That's " + str((score/4) * 100) + "%!")