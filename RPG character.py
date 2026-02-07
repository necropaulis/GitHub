full_dot = '●'
empty_dot = '○'

def create_character(name, stats):
    if name is not str:
        print("The character name should be a string")
    if len <1:
        print("The character should have a name")
    if len >10:
        print("The character name is too long")
    if '' in name:
        print("The character name should not co0ntain spaces")
    else:
        print(name)

    if stats is not int:
        print("All stats should be integers")
    if stats <1:
        print("All stats should be no less than 1")
    if stats >4:
        print("All stats should be no more than 4")
    if sum != 7:
        print("The character should start with 7 points")
    else:
        print(stats)

create_character("ren", [4, 2, 1])
