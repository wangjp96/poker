from cards import *
from player import *

def calc_value(hand):
    result = 0
    aces = 0
    for card in hand:
        if card.point == 'J' or card.point == 'Q' or card.point == 'K':
            result += 10
        elif card.point != 'A':
            result += int(card.point)
        elif card.point == 'A':
            aces += 1
    if aces == 0:
        return result
    elif (result + aces - 1) <= 10:
        result += 10 + aces
        return result
    else:
        result += aces
        return result

class Blackjack():
    def __init__(self, pack_num=1):
        self.players = []
        self.banker = Banker()
        self.deck = Deck(pack_num=pack_num)
        self.quit_flag = False

    def add_player(self, tokens=1000):
        self.players.append(Player(init_asset=tokens))

    def show_assets(self):
        print("-" * 20)
        for player in self.players:
            print("Player #" + str(player.player_id) +
                "'s remaining asset is: " + str(player.asset))
        print("-" * 20)

    def remove_player(self, player):
        self.players.remove(player)

    def init_deal(self):
        print("---Get ready for a new game!---")
        for player in self.players:
            player.clear_hand()
            player.set_bet()
        self.banker.clear_hand()
        self.deck.shuffle()
        for i in range(2):
            for player in self.players:
                player.add_hand(self.deck.draw())
            self.banker.add_hand(self.deck.draw())
        for player in self.players:
            if not player.is_me:
                print("Player #" + str(player.player_id) + "'s upcard is: ")
                player.show_hand(0)
        print("The banker's upcard is: ")
        self.banker.show_hand(0)

    def player_action(self, player):
        if calc_value(player.hand) == 21:
            return
        print("---Please decide your action: ---")
        while True:
            if len(player.hand) == 2:
                act = input("Type 'h' to hit, 's' to stand, 'd' for double down: ")
            else:
                act = input("Type 'h' to hit, 's' to stand: ")
            if act == 'h':
                player.add_hand(self.deck.draw())
            elif act == 's':
                break
            elif act == 'd':
                player.double_bet()
                player.add_hand(self.deck.draw())
                break
            else:
                print("Invalid action input!")
            value = calc_value(player.hand)
            if value >= 21:
                break

    def banker_action(self):
        self.banker.show_hand()
        while True:
            if calc_value(self.banker.hand) >= 17:
                break
            else:
                self.banker.add_hand(self.deck.draw())
                self.banker.show_hand(-1)
        return calc_value(self.banker.hand)

    def game_result(self, player):
        player.show_hand()
        value = calc_value(player.hand)
        print("The hand value of Player #" + str(player.player_id) +
            " is: " + str(value))
        banker_value = self.banker_action()
        print("The hand value of the banker is: " + str(banker_value))
        if value == 21:
            if banker_value == 21:
                player.draw_game()
            else:
                player.win()
        elif value > 21:
            player.lose()
        elif value < 21:
            if value > banker_value or banker_value > 21:
                player.win()
            elif value < banker_value:
                player.lose()
            else:
                player.draw_game()
        if player.asset <= 0:
            print("Player #" + str(player.player_id) + " is bankrupt!")
            print("Player #" + str(player.player_id) + " is eliminated.")
            self.remove_player(player)

    def quit_game(self):
        self.quit_flag = True
