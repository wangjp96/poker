from blackjack import *

if __name__ == "__main__":
    print("---Welcome to the Poker Game!---")
    print("-" * 20)
    print("Select the game you want to play:")
    game_opt = input("Type 'a' for Blackjack, others to quit: ")
    if game_opt == 'a':
        print("---Blackjack Starts!---")
        game = Blackjack()
        game.add_player()
        game.show_assets()
        init_card_num = game.deck.card_num
        while not game.quit_flag:
            game.init_deal()
            for player in game.players:
                if player.is_me:
                    game.player_action(player)
                    print("-" * 20)
                    game.game_result(player)
            if len(game.players) == 0:
                print("All players have been eliminated! The game ends.")
                break
            if game.deck.card_num < init_card_num / 2:
                game.deck.shuffle()
            game.show_assets()
            if input("Type 'q' to quit, others to play again: ") == 'q':
                game.quit_game()
