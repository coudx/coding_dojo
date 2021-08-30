from . import card
import random


class Deck:

    def __init__(self):
        suits = ["spades", "hearts", "clubs", "diamonds"]
        self.cards = []

        for s in suits:
            for i in range(1, 14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append(card.Card(s, i, str_val))

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def draw_card(self):
        user = self.cards.pop(random.randrange(0, len(self.cards)))
        host = self.cards.pop(random.randrange(0, len(self.cards)))
        print("User:")
        user.card_info()
        print("Host:")
        host.card_info()
        if (user.get_pts() > host.get_pts()):
            print("User wins this round")
        elif (user.get_pts() < host.get_pts()):
            print("Host wins this round")
        else:
            print("This round is a draw")

    def hasCard(self):
        return len(self.cards)
