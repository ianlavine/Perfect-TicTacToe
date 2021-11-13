"""board"""
import tile
import visualizer


class Board:
    """tictactoe board"""
    def __init__(self) -> None:

        self.winner = None
        self.size = 3
        self.frame = []
        for x in range(0, 3):
            for y in range(0, 3):
                self.frame.append(tile.Tile((self.size * (y * 30) + 25, self.size * (x * 30) + 10)))

        self.occupied = []

    def occupy(self, num, letter) -> None:
        """updates whats in occupied and unoccupied"""
        self.occupied.append(num)
        self.frame[num].occupy(letter)

    def last_move(self) -> int:
        """returns last move made"""
        return self.occupied[-1]

    def clear(self) -> None:
        """resets board"""
        self.frame.clear()
        for x in range(0, 3):
            for y in range(0, 3):
                self.frame.append(tile.Tile((self.size * (y * 30) + 25, self.size * (x * 30) + 10)))
        self.occupied.clear()
        visualizer.screen.fill((0, 0, 0))




