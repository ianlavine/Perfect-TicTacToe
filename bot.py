"""runs game and plays for x"""
import random
import node
import visualizer

corners = [0, 2, 6, 8]
ninety = {1: 3, 2: 0, 5: 1, 8: 2, 7: 5, 6: 8, 3: 7, 0: 6}
two_seventy = {3: 1, 0: 2, 1: 5, 2: 8, 5: 7, 8: 6, 7: 3, 6: 0}
one_eighty = {0: 8, 8: 0, 2: 6, 6: 2, 1: 7, 7: 1, 3: 5, 5: 3}
win_possibilities = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),
                     (2, 4, 6)]
opp = {'o': 'x', 'x': 'o'}


class Bot:
    """a round"""

    def __init__(self, board, side, name="Lame James", trainer=False) -> None:

        self.board = board
        self.frame = board.frame
        self.name = name
        self.side = side
        self.opp_side = opp[side]
        self.opp = None
        self.orientation = 0
        self.rotation_set = False

        self.trainee = trainer

        if trainer:
            move1 = node.Node(None, False, None)
            move2 = node.Node(None, True, None)
            self.moves = [move1, move2]
            self.on_path = True
            self.node = None
            self.probability = 50

    def check_win(self) -> bool:
        """checks if game was won"""
        for poss in win_possibilities:
            if self.frame[poss[0]].visual == self.frame[poss[1]].visual == self.frame[
             poss[2]].visual != "":
                return True
        return False

    def power_move(self) -> bool:
        """makes proper first move"""
        if not self.frame[4].occupied:
            self.board.occupy(4, self.side)
            return True
        random.shuffle(corners)
        for corner in corners:
            if not self.frame[corner].occupied:
                self.board.occupy(corner, self.side)
                return True
        return False

    def check_win_chance(self, char) -> int:
        """checks if win in one move for player char"""
        for poss in win_possibilities:
            for x in range(0, 3):
                if self.frame[poss[x % 3]].visual == self.frame[poss[(x + 1) % 3]].visual == char \
                        and not self.frame[poss[(x + 2) % 3]].occupied:
                    return poss[(x + 2) % 3]
        return 9

    def check_finish(self, choices) -> bool:
        """call check_win_chance for each player """
        for letter in choices:
            num = self.check_win_chance(letter)
            if num != 9:
                self.board.occupy(num, self.side)
                return True
        return False

    def check_to_random(self, choices) -> None:
        """check_finish. if not then makes random move"""
        if not self.check_finish(choices):
            self.random_move()

    def random_move(self) -> None:
        """makes random move"""
        while True:
            tile = random.randint(0, 8)
            if not self.frame[tile].occupied:
                self.board.occupy(tile, self.side)
                break

    def take_turn(self, turn) -> None:
        """takes a turn"""
        if self.trainee:
            self.tree_move(turn)
        else:
            self.standard_move(turn)

    def standard_move(self, turn) -> None:
        """makes a non-tree move"""
        if self.name == 'God Bot':
            if not self.check_finish([self.side, self.opp_side]):
                if not self.power_move():
                    self.random_move()
        elif self.name == 'Julio':
            if turn == 1 or turn == 2:
                self.power_move()
            else:
                self.check_to_random([self.side, self.opp_side])
        elif self.name == 'Jung Julio':
            self.check_to_random([self.side, self.opp_side])
        elif self.name == 'Odd Bot':
            if not self.power_move():
                if not self.check_finish([self.side, self.opp_side]):
                    self.random_move()
        elif self.name == 'Defender':
            self.check_to_random([self.opp_side])
        elif self.name == 'Striker':
            self.check_to_random([self.side])
        elif self.name == 'Lame James':
            self.random_move()
        elif self.name == 'Player':
            visualizer.show_board(self.frame)
            visualizer.player_move(self.board, self.side)

        self.opp.update_node()

    def tree_move(self, turn) -> None:
        """checks if tree move can be made"""

        if turn == 0:
            self.node = self.moves[0]
            if self.opp.trainee:
                self.opp.node = self.opp.moves[1]

        chance = random.randint(0, 100)

        if self.on_path and chance < self.probability and len(self.node.children) >= 1:
            child_sort = sorted(self.node.children, key=lambda x: self.node.children[x].winp)
            self.board.occupy(child_sort[-1], self.side)
            self.opp.update_node()
            print('tree move made')
        else:
            self.standard_move(turn)

        self.update_node()

    def set_rotation(self) -> None:
        """sets rotation"""
        val = self.board.last_move()
        if val != 4:
            if val == 2 or val == 5:
                self.orientation = ninety
            if val == 3 or val == 6:
                self.orientation = two_seventy
            if val == 7 or val == 8:
                self.orientation = one_eighty
            self.rotation_set = True

    def rotate(self, val) -> int:
        """rotates given value"""
        if self.orientation == 0 or val == 4:
            return val
        elif isinstance(self.orientation, dict):
            return self.orientation[val]

    def update_node(self) -> None:
        """goes to next node"""
        if self.trainee:
            if not self.rotation_set:
                self.set_rotation()
            move_made = self.rotate(self.board.last_move())
            if move_made not in self.node.children:
                self.on_path = False
                self.node.add_child(move_made)
            self.node = self.node.children[move_made]

    def update_and_reset(self, winner) -> None:
        """updates tree's winp's"""
        if self.trainee:

            if winner == 'tie':
                self.node.update_winp(0.5)
            else:
                self.node.update_winp(int(winner == self.name))

            self.on_path = True
            self.node = None

        self.orientation = 0
        self.rotation_set = False

    def print_tree(self) -> None:
        """prints trees"""
        for move in self.moves:
            print('++++++++++++++++++ THIS +++++++++++++++++++')
            for node in move.children:
                print(str(node) + ': ' + str(move.children[node].winp))
                print('#########')
                for node2 in move.children[node].children:
                    print(str(node2))
                print('---------------------')





