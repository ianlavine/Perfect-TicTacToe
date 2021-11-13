"""individual tile class"""


class Tile:
    """represents a tile"""
    def __init__(self, position) -> None:

        self.position = position
        self.x_start = position[0]
        self.x_end = position[0] + 75
        self.y_start = position[1]
        self.y_end = position[1] + 75

        self.occupied = False
        self.visual = ''

    def occupy(self, letter) -> None:
        """occupies tile"""
        self.occupied = True
        self.visual = letter

    def hover_check(self, position) -> bool:
        """checks if tile hovered over"""
        if self.x_start < position[0] < self.x_end:
            if self.y_start < position[1] < self.y_end:
                return True
        return False
