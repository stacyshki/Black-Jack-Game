from cards import Card
from random import shuffle


class Deck:
    def __init__(self):
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
        suits = ['♠️', '♣️', '♥️', '♦️']

        self.cards = [Card(r, s) for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
