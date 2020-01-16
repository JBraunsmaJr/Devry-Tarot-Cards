import json
import random
from card import Card


cards = []


def load_cards():
    with open("cards.json", "r") as card_file:
        data = json.loads(card_file.read())
    # have to check this later, but we should iterate over each card
    # and put it into the array above by shoving each object's data into an object
    # of type "Card"
    for item in data["cards"]:
        card = Card(item["name"], item["description"])
        cards.append(card)


def random_card():
    """
    Return a random card from the cards array
    If no cards have been loaded... None is returned
    """
    if len(cards) == 0:
        return None
    else:
        return cards[random.randint(0, len(cards))]



