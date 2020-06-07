from sys import exit


def gold_room():
    print("This room is full of gold")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("Nice you're not greedy")
        exit(0)
    else:
        dead("You greedy bastard")


def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("The fat bear is in the front of another door")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear slaps face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from door")
            print("You can go through")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulu_room():
    print("Here you see Cthulu")
    print("It stares and youre insane")
    print("Flee or die?")
    choice = input("> ")

    if "flee" in choice:
        start()
    elif "die" in choice:
        dead("Well that was quick")
    else:
        cthulu_room()


def dead(why):
    print(why, "Good Job")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left")
    print("Which one?")

    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you die")


start()
