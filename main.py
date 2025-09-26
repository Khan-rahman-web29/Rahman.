# 1 import the randm module 
# 2 create the subjects

import random
import random

# Funny and diverse subjects
subjects = [
    "Rahman Khan", 
    "Arshan Khan",
    "Mumbai Cat",
    "Arif Ansari",
    "Kaimganj Dogs",
    "Nirmala Sitaraman",
    "Narendra Modi",
    "Alien from Mars",
    "AI Robot GPT-5000",
    "A Flying Rickshaw",
    "Invisible Man",
    "Baba ka Dhaba Owner",
    "Kaimganj's Donkey"
]

# Wild & funny actions
actions = [
    "launches",
    "eats",
    "dances with",
    "declares war on",
    "celebrates",
    "is celebrating",
    "is sad about",
    "steals",
    "paints",
    "hacks",
    "buys",
    "sings to",
    "slaps"
]

# Weird & random things
things = [
    "a red fort",
    "the Taj Mahal",
    "public transport",
    "a plate of samosa",
    "something inside parliament",
    "the Ram Mandir",
    "Jatwara",
    "a flying cow",
    "a packet of Kurkure",
    "modi ji's chappal",
    "Arshan's tiffin box",
    "a spaceship full of pani puri",
    "a very angry parrot",
    "a haunted dosa"
]

# Start the headline generation loop 
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    thing = random.choice(things)

    headline = f"BREAKING NEWS: {subject} {action} {thing}!"
    print("\n" + headline)

    user = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user == "no":
        break

# Goodbye message
print("\nThanks for using Fake News Headline Generator. Have a hilarious day! 😄")

    









 
