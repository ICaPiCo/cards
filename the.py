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
        self.cards_on_table = []
        self.pot = 0
        self.last_raise = 0
        self.players = {"Alice":[100,[],1],"Bob":[100,[],1]} # "John Doe":[money left,[current cards in hand],wants to play]
        self.match()
        self.check_win()
        print(self.cards_on_table)
        print(self.players)

    def setup(self):
        for player in self.players:
            self.players[player][1] = [self.draw_card_player() for _ in range(2)]

    def do_bets(self):
        for n in self.players.keys():
            print(f"{n}, do your bets! (fold,call,raise,all-in)")
            d = int(input())
            if d == "fold":
                self.players[n][2] = 0
            elif d == "call":
                self.players[n][2] = 1
            elif d == "raise":
                self.players[n][2] = 1
                bet = int(input("How much?: "))
                self.players[n][0] -= bet
                self.pot += bet
                self.last_raise = bet
            elif d == "all-in":
                alibaba = self.players[0]
                self.player[2] = 1
                self.players[0] -= alibaba
                self.pot += alibaba
                self.last_raise = alibaba


    def draw_card_player(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card

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