from cards import *

class Player():
    def __init__(self, player_id=1, is_me=True, init_asset=1000):
        self.player_id = player_id
        self.is_me = is_me
        self.bet = 0
        self.hand = []
        self.asset = init_asset

    def see_card(self, card):
        print("You have drawn a " + card.suit + ' ' + card.point)

    def add_hand(self, card):
        self.hand.append(card)
        if self.is_me:
            self.see_card(card)

    def clear_hand(self):
        self.hand = []

    def show_hand(self, index='all'):
        if index == 'all':
            for card in self.hand:
                card.is_revealed = True
                print(card.suit + ' ' + card.point)
        else:
            self.hand[index].is_revealed = True
            print(self.hand[index].suit + ' ' + self.hand[index].point)

    def set_bet(self):
        print("Please select your bet for this round (type others for 50):")
        flag = input("'a'. 50, 'b'. 100, 'c'. 200, 'd'. 500:" )
        if flag == 'a' or flag == '50':
            self.bet = 50
        elif flag == 'b' or flag == '100':
            self.bet = 100
        elif flag == 'c' or flag == '200':
            self.bet = 200
        elif flag == 'd' or flag == '500':
            self.bet = 500
        else:
            self.bet = 50

    def double_bet(self):
        self.bet = 2 * self.bet

    def win(self):
        print("Player #" + str(self.player_id) + " wins the game!")
        self.asset += self.bet

    def lose(self):
        print("Player #" + str(self.player_id) + " loses the game!")
        self.asset -= self.bet

    def draw_game(self):
        print("Draw game!")

class Banker():
    def __init__(self):
        self.hand = []

    def add_hand(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def show_hand(self, index='all'):
        if index == 'all':
            for card in self.hand:
                card.is_revealed = True
                print(card.suit + ' ' + card.point)
        else:
            self.hand[index].is_revealed = True
            print(self.hand[index].suit + ' ' + self.hand[index].point)
