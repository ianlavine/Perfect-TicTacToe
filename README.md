# Perfect-TicTacToe

A bot without any knowledge of tictactoe plays against a series of preprogrammed tictactoe bots of varying skill.
The learning bot is connected to a move tree, which keeps track of every move made in each game in a single branch.
At the bottom of every branch, an outcome of either, win, loss, or tie is recorded and sent back up the tree.
The learning bot slowly shifts from making random moves, to making moves that have shown to lead to wins in its move tree.
This continues until the bot makes the optimal move in any situation, and is guranteed to always win or tie against the preprogrammed 'perfect' bot.
