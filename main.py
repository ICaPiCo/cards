import math,random

def matrix(m):
    for i in m:
        print(i)

def sum_deck(deck):
    """give the sum of all the cards left in a deck"""
    sumd = 0
    for d in deck:
        sumd += d.index(1)+1
    return sumd


def get_winner(cpus):
    """get the winner out of all the playing bots"""
    winner = None
    best_score = 0

    for n, player in enumerate(cpus):
        cards = player[1]
        score = sum(c.index(1) + 1 for c in cards)
        if score <= 21:
            if score > best_score:
                best_score = score
                winner = n
            elif score == best_score and best_score > 0:
                winner=str(winner)+","+str(n)
            print(n, score)
        else:
            print(n, score, "bust!")

    return winner


class Blackjack:
    def __init__(self, cpus):
        self.cpus = [[[100],[],1] for i in range(cpus)] #First part is money left, second part is current cards, third part is if he decided to play
        self.players = len(self.cpus)
        self.pot = 0
        self.deck = [[int(k==j%13) for k in range(13)] for j in range(52)]
        self.bot_match()

    def bot_match(self):
        random.shuffle(self.deck)
        while self.players > 1:
            self.players = 0

            for c,n in zip(self.cpus,range(len(self.cpus))): #check if they want to play and give cards
                if c[2] == 1:
                    self.players +=1
                    if self.deck:
                        c[1].append(self.deck[-1])
                        self.deck.pop(-1)
                    else:
                        c[2] = 0

            for c,n in zip(self.cpus,range(len(self.cpus))): #make they actually play after every one gets a card
                if c[2]:
                    self.bot_act(c,n)
        print("Winning bot:", get_winner(self.cpus))

    def bot_act(self,bot,number):
        money = bot[0]
        cards = bot[1]
        normal_card = []
        for c in cards:
            normal_card.append(c.index(1)+1)
        average_left = sum_deck(self.deck)/(52-len(cards))

        if average_left+sum(normal_card) < 21:
            print(f"Bot {number}, decides to hit, with the cards: {normal_card}")
        else:
            print(f"Bot {number}, decides to stand, current cards: {normal_card}")
            bot[2] = 0


Blackjack(2)