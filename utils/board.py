import math

import requests


def get_board_data():
    boardurl = f"https://pxls.space/boarddata"
    return requests.get(boardurl).content


def get_board_info():
    boardurl = f"https://pxls.space/info"
    return requests.get(boardurl).text


def board2list(board, width):
    board_size = len(board)
    height = board_size / width
    height = math.floor(height)
    boardlist = []
    for i in range(board_size):
        b = board[i]
        if b == b'':
            break
        x = i % width
        y = math.floor(i / width)
        boardlist.append((x,y,b))
    return boardlist

