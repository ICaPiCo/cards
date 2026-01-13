import random

class Blackjack:
    def __init__(self,rounds):

        self.training = {}
        self.cw = 0 #cpu wins
        self.aw = 0 #ai wins
        for _ in range(rounds):
            self.init_players()
            self.match()
        print(self.aw/self.cw)
        print(self.training)

    def init_players(self):
        self.cpu = [[100], [], 1] #First part is money left, second part is current cards, third part is if he decided to play
        self.ai = [[100], [], 1]
        self.players = 2
        self.starter = random.choice([0,1])
        self.deck = [k for k in [2,3,4,5,6,7,8,9,10,10,10,11] for _ in range(4)]

    def get_winner(self,cpu, ai):
        c = sum(cpu[1])
        a = sum(ai[1])
        if c == a <= 21 :
            self.update_ai_weights(0)
            return "c, a"
        if c > 21 and a > 21:
            self.update_ai_weights(0)
            return "None"

        if a > 21: a = 0
        if c > 21: c = 0

        if 21 >= a > c:
            self.aw += 1
            self.update_ai_weights(1)
            return "a"
        if 21 >= c > a:
            self.cw += 1
            self.update_ai_weights(0)
            return "c"

        else: return "None"

    def match(self):
        random.shuffle(self.deck)
        while self.players >= 1:
            self.players = 0

            #Check if cpu wants to play
            if self.cpu[2] == 1:
                self.players +=1
                if self.deck:
                    self.cpu[1].append(self.deck[-1])
                    self.deck.pop(-1)
                else:
                    self.cpu[2] = 0

            #check if ai wants to play
            if self.ai[2] == 1:
                self.players +=1
                if self.deck:
                    self.ai[1].append(self.deck[-1])
                    self.deck.pop(-1)
                else:
                    self.ai[2] = 0

            #make him actually play after everyone gets a card
            if self.cpu[2]:
                normal_cards = self.cpu[1]
                average_left = sum(self.deck) / (52 - len(normal_cards))
                if average_left + sum(normal_cards) < 21:
                    pass
                    #print(f"CPU decides to hit, with the cards: {normal_cards}")
                else:
                    #print(f"CPU decides to stand, current cards: {normal_cards}")
                    self.cpu[2] = 0

            if self.ai[2]:
                key = f"{[sum(self.ai[1]), sum(self.cpu[1]), len(self.deck)]}"
                if key in self.training:
                    self.ai[2] = round(self.training.get(key))
                else:
                    self.ai[2] = random.choice([0,1])
                """
                if self.ai[2] == 1:
                    print(f"AI decides to hit,, with the cards: {self.ai[1]}")
                else:
                    print(f"AI decides to stand, with the cards: {self.ai[1]}")
                """

        self.get_winner(self.cpu, self.ai)
        #print("Winner:", )

    def update_ai_weights(self,wol):
        key = f"{[sum(self.ai[1]), sum(self.cpu[1]), len(self.deck)]}"
        if key in self.training:
            if wol == 1:
                self.training[key] = min(self.training[key] + 0.1, 1)
            else:
                self.training[key] = max(self.training[key] - 0.1, 0)
        else:
            if wol == 1:
                self.training[key] = 0.6
            else:
                self.training[key] = 0.4

Blackjack(100000)