#TODO: Create a Useless Hack
#Create any silly, unnecessary, or useless hack!

from emoji import emojize
import random

def emoji_talk():
    """
    A silly project for people to talk through emoji 🤗"""

    Sad_emoji = ["😮‍💨", "🫤", "😖", "🥺", "☹"]
    random_emoji = ["👯‍♀️","💆‍♀️", "👩‍🍼", "👸", "🧐", "😆"]

    person1 = input("Base on the options above, tell me how are your feellings today?:\n-Happy\n-Sad\n-Whatever\n\n").title()
    
    if person1 == "Sad":
        print(f"{random.choice(Sad_emoji)}")
        print(f"computer says {random.choice(random_emoji)}")
              
emoji_talk()         
