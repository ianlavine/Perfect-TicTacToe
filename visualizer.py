"""visualizes game in python"""
import pygame as py

py.init()
screen = py.display.set_mode([3 * 85, 3 * 85])
font = py.font.Font('freesansbold.ttf', 3 * 16)


def player_move(board, side) -> None:
    """single move for player"""
    frame = board.frame
    running = True
    while running:

        for event in py.event.get():

            if event.type == py.QUIT:
                py.quit()

            if event.type == py.MOUSEBUTTONDOWN:
                for tile in range(len(frame)):
                    if frame[tile].hover_check(py.mouse.get_pos()) and not frame[tile].occupied:
                        board.occupy(tile, side)
                        running = False
                        break


def show_board(frame) -> None:
    """just shows board for entirety of time"""

    for tile in frame:
        img = font.render(tile.visual, True, (255, 255, 255))
        screen.blit(img, tile.position)

    py.display.flip()


