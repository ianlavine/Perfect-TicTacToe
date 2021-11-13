"""Game"""
import bot
import board


class Game:
    """is a game"""

    def __init__(self, names, training=0) -> None:

        self.main_board = board.Board()

        bot1 = bot.Bot(self.main_board, 'x', names[0], training == 1)
        bot2 = bot.Bot(self.main_board, 'o', names[1], training == 2)
        bot1.opp = bot2
        bot2.opp = bot1

        self.bots = [bot1, bot2]

    def play(self, players) -> str:
        """plays single game"""

        turn = 0
        winner = None
        while winner is None:
            for bot in players:
                if turn == 9:
                    winner = 'tie'
                    break
                bot.take_turn(turn)
                if bot.check_win():
                    winner = bot.name
                    break
                turn += 1

        for bot in players:
            bot.update_and_reset(winner)

        self.main_board.clear()

        return winner

    def tourney(self, players, total=1, swap=False) -> dict:
        """plays many games and keeps track of scores"""

        wins = {players[0].name: 0, players[1].name: 0, 'tie': 0}

        bots = [x for x in players]
        for _ in range(total):
            winner = self.play(bots)
            wins[winner] += 1
            if swap:
                bots = [bots[1], bots[0]]
            self.main_board.clear()

        return wins

    def basic_setup(self) -> None:
        """sets up bots for tourney"""
        print(self.tourney(self.bots))

    def swap_bots(self) -> None:
        """swaps bots"""
        self.bots = [self.bots[1], self.bots[0]]


game = Game(['Player', 'Player'], 1)
game.basic_setup()
