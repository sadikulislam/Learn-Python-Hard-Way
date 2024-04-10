from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    choice = input("> ")
    if choice.isdigit():
        how_much = int(choice)
        if how_much < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
        else:
            dead("You greedy bastard!")
    else:
        dead("Man, learn to type a number.")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("THe fat bear is in forn of another door.")
    print("How are you going to move the bear?")


def bear_room():
    bear_moved = False
    while True:
        print("There is a bear here.")
        print("The bear has a bunch of honey.")
        print("The fat bear is in front of another door.")
        print("How are you going to move the bear?")
        choice = input("> ")
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear":
            if not bear_moved:
                print("The bear has moved from the door.")
                print("You can go through it now.")
                bear_moved = True
            else:
                dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def devil_room():
    while True:
        print("Here you see the great evil Pillu.")
        print("He, it, whatever stares at you and you go insane.")
        print("Do you flee for your life or eat your head?")
        choice = input("> ")
        if "flee" in choice:
            start()
        elif "head" in choice:
            dead("Well that was tasty!")
        else:
            print("Invalid choice.")

def dead(why):
    print(why, "Game Over!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        devil_room()
    else:
        print("Invalid choice.")

start()