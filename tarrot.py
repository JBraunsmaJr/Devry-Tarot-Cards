import random
import sys, time, os
import json
from card import Card

# import everything in this file... we will use card_handler as an object that references everything in that file
# card_handler.load_cards() -- for instance
import card_handler as card_handler
import validator as validator

print(".------..------..------..------..------.     .------..------..------..------..------..------.")
print("|T.--. ||A.--. ||R.--. ||O.--. ||T.--. |.-.  |R.--. ||E.--. ||A.--. ||D.--. ||E.--. ||R.--. |")
print("| :/\: || (\/) || :(): || :/\: || :/\: ((5)) | :(): || (\/) || (\/) || :/\: || (\/) || :(): |")
print("| (__) || :\/: || ()() || :\/: || (__) |'-.-.| ()() || :\/: || :\/: || (__) || :\/: || ()() |")
print("|-'--'T|| '--'A|| '--'R|| '--'O|| '--'T| ((1)) '--'R|| '--'E|| '--'A|| '--'D|| '--'E|| '--'R|")
print("`------'`------'`------'`------'`------'  '-'`------'`------'`------'`------'`------'`------'")
print("")
print("")
print("")

# typewriter text for message.
message = " Welcome to tarot reader 0.1, made in python v3.6 by Darren Lindsey and Jon Braunsma. \n "

for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)


def get_sign(month, day):
    """
    Based on the given month / day - return the appropriate sign
    """
    a_sign = ""
    if month == 'december':
        a_sign = 'Sagittarius' if (day < 22) else 'Capricorn'  # aSign = Astrological sign
    elif month == 'january':
        a_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 'february':
        a_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 'march':
        a_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 'april':
        a_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 'may':
        a_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 'june':
        a_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 'july':
        a_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 'august':
        a_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 'september':
        a_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 'october':
        a_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 'november':
        a_sign = 'scorpio' if (day < 22) else 'Sagittarius'

    return a_sign


# Load all the cards in the cards.json file
card_handler.load_cards()

# can either explicity pass parameter name + value, or the function will set the values based on the order you defined
# above we defined month first, day second. So if we pass
# get_sign("september", 12)
# it will put the values into month,
# day

sign_name = input("What is your name: \n")
sign_month = validator.input_month("What month were you born?: \n")
sign_year = validator.input_number("What year were you born?: \n")
sign_day = validator.input_day_of_month("What day were you born?: \n", sign_month, sign_year)

sign = get_sign(sign_month, sign_day)

print("Hello", sign_name, "your sun sign is", sign, "\n")

print(card_handler.random_card(),
      "\n \n This is The Problem card \n \n Something that you need to resolve in order to make progress forward. ")

# constants
proceed_text = "Ready for next card? Y/N:"

# start tarot reading function
question = input("What is your question?: ")

while not validator.input_bool("is this the question that you would like the spirits to answer? Y/N: "):
    question = input("What is your question?: ")

# store selected cards
selected_cards = []

prompts = [
    "is your Present Position. This position reveals the current situation, and what is now happening",
    "is the Problem. Something that they need to resolve in order to move forward",
    "is the Past. Here we see the the past events, and also how they have shaped the current situation. \n This can give us some information on influences in the past that have lead up to this state of affairs.",
    "is the Future. This card represents what could be a likely turn of events, given that nothing changes.\n These are usually short term happenings, and doesn’t represent the final resolution of these events.",
    "is The Conscious. This card explores what you are focused on, and where your mind is.\n This can represent your goals and your desires regarding this situation, as well as what your assumptions are.",
    "is The Unconscious. The unconscious reveals what is truly driving this situation; the feelings, the beliefs and the values that perhaps the querent doesn’t even understand yet.\n Sometimes this card may be a surprise, and can also represent a hidden influence.",
    "is Your Influence. This card can be interpreted somewhat broadly - but in general, relates to how you see yourself,\n and how that perception can influence how this situation plays out.\n What beliefs about yourself do you carry?\n Do you expand yourself, or limit yourself?",
    "is your External Influence. This card represents the world around you and how it affects this situation.\n It may represent the social and emotional environment that you are operating in, as well as how others perceive you.",
    "are your Hopes and Fears. One of the harder positions in this spread to decode, this card can represent both what you secretly desire, as well as what you may be trying to avoid.\n Human nature is often paradoxical, and what we fear the most is sometimes what we also truly have been hoping for all along.",
    "is your Outcome. This card is meant to be a summary of all the previous cards.\n Given all that is happening, what is the likely resolution of this event? \nShould you find a card here that does not have a favorable outcome, you can analyze the remainder of the spread to find another course of action."
]


def tarrot_function():
    for i in range(0, len(prompts)):
        card = card_handler.random_card()
        selected_cards.append(card)
        prompt = prompts[i]

        print(card, prompt)

        # force the user to wait until they're ready for the next card. DO NOTHING just ensures the iteration
        # will not continue until they're ready...
        while not validator.input_bool("Are you ready for the next card? Y/N: "):
            pass

tarrot_function()
# output random 10 cards in this order
# note Previous cards should stay present on the screen
# (randomcard) is your Present Postion print("This position reveals the current situation, and what is now happening.")
# ask user if they would like a descrpition of the card ??? to much work???