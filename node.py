class Node:
    """one node in a tree"""

    def __init__(self, parent, myturn, move) -> None:
        self.parent = parent
        self.children = dict()
        self.myturn = myturn
        self.move = move
        self.winp = 0

    def update_winp(self, perp=None) -> None:
        """updates win percentage of node, and all parent nodes"""
        if perp is None:
            children_winp = [self.children[x].winp for x in self.children]
            if self.myturn:
                lowest = min(children_winp)
                print('updating ' + str(self.move) + ' lowest: ' + str(lowest) + ' of ' + str(
                    children_winp))
                self.winp = lowest
            else:
                average = sum(children_winp) / len(children_winp)
                print('updating ' + str(self.move) + ' average: ' + str(average) + ' of '
                      + str(children_winp))
                self.winp = average
        else:
            print('updating child ' + str(self.move) + ': ' + str(perp))
            self.winp = perp

        if self.parent.parent is not None:
            self.parent.update_winp()
        else:
            print('Parent Node')

    def add_child(self, move) -> None:
        """adds a single child"""
        self.children[move] = Node(self, not self.myturn, move)

    def print_kids(self) -> None:
        """prints kids"""
        print([(self.children[x].move, self.children[x].winp) for x in self.children])
        print('_______')
        if len(self.children) > 1:
            for x in self.children:
                self.children[x].print_kids()
                print('######')
