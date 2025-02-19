class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        if self.rank in ['10', 'J', 'Q', 'K']:
            return 10
        else:
            return ' A23456789'.index(str(self.rank))

    def get_rank(self):
        return self.rank

    def __str__(self):
        return f'{self.rank}{self.suit}'
