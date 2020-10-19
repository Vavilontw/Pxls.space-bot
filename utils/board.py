import math

import requests


def get_board_data():
    boardurl = f"https://pxls.space/boarddata"
    return requests.get(boardurl).content


def get_board_info():
    boardurl = f"https://pxls.space/info"
    return requests.get(boardurl).text


def board2list(board, width, art_size, artx, arty):
    board = [board[x : x + width] for x in range(0, len(board), width)]
    boardlist = []
    for x in range(art_size[0]):
        for y in range(art_size[1]):
            b = board[arty + y][artx + x]
            #print(arty + y,artx + x)
            xx = artx + x
            yy = arty + y
            boardlist.append((xx, yy, b)) 
    return boardlist
