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
        self.deck = [k+s for k in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] for s in ["♣","♠","♡","♢"]]
        random.shuffle(self.deck)
        print(self.deck)
        self.cards_on_table = []
        self.players = {"Alice":[100,[],1],"Bob":[100,[],1]} # "John Doe":[money left,[current cards in hand],wants to play]
        self.match()
        self.check_win()

    def setup(self):
        for player in self.players:
            self.players[player] = [self.draw_card() for i in range(2)]

    def draw_card_on_table(self):
        self.cards_on_table.append(self.deck[0])
        self.deck.pop(0)

    def check_win(self):
        pass

    def match(self):
        self.setup()
        self.do_bets()
        for _ in range(3):
            self.draw_card_on_table()
        self.do_bets()
        self.draw_card_on_table()
        self.do_bets()
        self.draw_card_on_table()


The()