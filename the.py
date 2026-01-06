"""
Texas Hold'Em

Rules:
- Every player gets two hole cards.
- Three communal cards are dealt ('the flop')
- One more communal card is dealt ('the turn')
- A final communal card is dealt ('the river')
- All remaining players reveal their best five-card hand, using all seven available cards.
- Possible to call (don't add more money) / fold (someone raised) / raise (add more money to the pot) / all in (put all your money in the pot)
"""

import random

class The:
    def __init__(self):
        self.players = [[100], [],1]  # First part is money left, second part is current cards, third part is if he decided to play
        self.deck = [k+s for k in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] for s in ["♣","♠","♡","♢"]]
        random.shuffle(self.deck)
        print(self.deck)
        self.match()

    def match(self):
        self.flop()
        self.turn()
        self.river()

The()