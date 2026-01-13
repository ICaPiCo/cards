import random

class The:
    def __init__(self):
        self.deck = [k+s for k in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] for s in ["♣","♠","♡","♢"]]
        self.initial_deck = self.deck.copy()
        random.shuffle(self.deck)
        self.cards_on_table = []
        self.pot = 0
        self.players = {"Alice":[100,[],1,0],"Bob":[100,[],1,0]}
        self.match()
        print(f"Table: {self.cards_on_table}")
        print(f"Players: {self.players}")

    def setup(self):
        # Reset deck for new match
        self.deck = self.initial_deck.copy()
        random.shuffle(self.deck)
        self.cards_on_table = []
        self.players = {"Alice":[100,[],1,0],"Bob":[100,[],1,0]}
        for player in self.players:
            self.players[player][1] = [self.draw_card_player() for _ in range(2)]

    def do_bets(self):
        betting_active = True
        while betting_active:
            active_players = [p for p in self.players.values() if p[2] != 0]
            bets = [p[3] for p in active_players]

            changes_made = False
            for n in self.players.keys():
                if self.players[n][2] != 0:
                    current_high = max([p[3] for p in self.players.values()], default=0)

                    # Skip if player already matched the high bet (unless round just started)
                    if self.players[n][3] == current_high and current_high > 0 and not changes_made:
                        continue

                    print(f"{n}, Wallet: {self.players[n][0]} | Your Bet: {self.players[n][3]} | High: {current_high}")
                    d = input("Action (fold/call/raise/all-in): ").strip().lower()

                    if d == "fold":
                        self.players[n][2] = 0

                    elif d == "call":
                        diff = current_high - self.players[n][3]
                        self.players[n][0] -= diff
                        self.players[n][3] += diff

                    elif d == "raise":
                        amount = int(input("Amount to ADD on top of current high? "))
                        total_req = (current_high - self.players[n][3]) + amount
                        self.players[n][0] -= total_req
                        self.players[n][3] += total_req
                        changes_made = True

                    elif d == "all-in":
                        money = self.players[n][0]
                        self.players[n][0] = 0
                        self.players[n][3] += money
                        changes_made = True

            active_bets = [p[3] for p in self.players.values() if p[2] != 0]
            if len(active_bets) <= 1 or (len(set(active_bets)) == 1 and not changes_made):
                betting_active = False

        self.pot += sum([p[3] for p in self.players.values()])
        print(f"Pot: {self.pot}")
        for p in self.players.values():
            p[3] = 0

    def draw_card_player(self):
        return self.deck.pop(0)

    def draw_card_on_table(self):
        self.cards_on_table.append(self.deck.pop(0))

    def sort_cards(self, cards):
        # Your original sorting logic
        cards = sorted(cards, key=self.initial_deck.index, reverse=True)
        return cards

    def check_win(self):
        for p in self.players.keys():
            # Shows the sorted 7-card pool for each player
            hand = self.sort_cards(self.players[p][1] + self.cards_on_table)
            print(f"{p}'s full hand: {hand}")

            #royal flush ?
            #straight flush ?
            #four of a kind ?
            #full house ?
            #flush ?
            #straight ?
            #three of a kind ?
            #two pairs ?
            #pair ?
            #high card ?

    def match(self):
        self.setup()
        self.do_bets() # Pre-flop

        for _ in range(3): self.draw_card_on_table() # Flop
        print(f"Flop: {self.cards_on_table}")
        self.do_bets()

        self.draw_card_on_table() # Turn
        print(f"Turn: {self.cards_on_table}")
        self.do_bets()

        self.draw_card_on_table() # River
        print(f"River: {self.cards_on_table}")
        self.do_bets()

        self.check_win()

The()