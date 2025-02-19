class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        result = 0
        aces = 0

        for card in self.cards:
            result += card.card_value()
            if card.get_rank() == 'A':
                aces += 1

        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    def __str__(self):
        text = f'{self.name} ({self.get_value()})'
        for card in self.cards:
            text += str(card) + ' '

        return text
