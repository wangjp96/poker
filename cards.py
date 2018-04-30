import random

class Card():
    def __init__(self, suit, point):
        self.suit = suit
        self.point = point
        self.is_revealed = False

def build_deck(suits, points, pack_num=1):
    deck = []
    for i in range(pack_num):
        for suit in suits:
            for point in points:
                deck.append(Card(suit, point))
    return deck

class Deck():
    def __init__(self, pack_num=1):
        self.suits = ('heart', 'spade', 'club', 'diamond')
        self.points = ('A', '2', '3', '4', '5', '6',
            '7', '8', '9', '10', 'J', 'Q', 'K')
        self.pack_num = pack_num
        self.deck = build_deck(self.suits, self.points, self.pack_num)
        self.card_num = len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def reset(self):
        self.deck = build_deck(self.suits, self.points, self.pack_num)
        self.shuffle()
        self.card_num = len(self.deck)

    def draw(self):
        if self.card_num == 0:
            self.reset()
        card = self.deck.pop(0)
        self.card_num = len(self.deck)
        return card
