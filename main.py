#TODO: Create a Useless Hack
#Create any silly, unnecessary, or useless hack!

from emoji import emojize
import random

def emoji_talk():
    """
    A silly project for people to talk through emoji 🤗"""

    Sad_emoji = ["😮‍💨", "😖", "🥺", "☹", "😩","😞"]
    random_emoji = ["👯‍♀️","💆‍♀️", "👩‍🍼", "👸", "🧐", "😆"]
    happy= ["😚", "🤩", "😁", "😀", "🤣", "🤩"]

    lets_talk = True

    while lets_talk:

        person_mood = input("Base on the options bellow, tell me how are your feellings today?:\n-Happy\n-Sad\n-Fine or press any key to exit: \n\n").title()
        
        if person_mood == "Sad":
            print(f"\nYou said: {random.choice(Sad_emoji)}")
        elif person_mood == "Happy":
            print(f"\nYou said: {random.choice(happy)}")
        elif person_mood == "Fine":
            print(f"\nYou said: {random.choice(random_emoji)}") 

        else:
            lets_talk = False       

        print(f"computer says: {random.choice(random_emoji)}")

              
emoji_talk()         
