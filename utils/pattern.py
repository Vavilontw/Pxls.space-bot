import random


def snake_top(e):
    if e[1] % 2 == 0:
        return e[1], e[0]
    else:
        return e[1], -1 * e[0]


def snake_left(e):
    if e[0] % 2 == 0:
        return e[0], e[1]
    else:
        return e[0], -1 * e[1]


def snake_down(e):
    if e[1] % 2 == 0:
        return e[1] * -1, e[0]
    else:
        return e[1] * -1, -1 * e[0]


def snake_right(e):
    if e[0] % 2 == 0:
        return e[0] * -1, e[1]
    else:
        return e[0] * -1, -1 * e[1]


def chess_snake_top(e):
    if e[1] % 2 == 0:
        return (e[0] + e[1]) % 2, e[1], e[0]
    else:
        return (e[0] + e[1]) % 2, e[1], -1 * e[0]


def chess_snake_left(e):
    if e[0] % 2 == 0:
        return (e[0] + e[1]) % 2, e[0], e[1]
    else:
        return (e[0] + e[1]) % 2, e[0], -1 * e[1]


def chess_snake_down(e):
    if e[1] % 2 == 0:
        return (e[0] + e[1]) % 2, e[1] * -1, e[0]
    else:
        return (e[0] + e[1]) % 2, e[1] * -1, -1 * e[0]


def chess_snake_right(e):
    if e[0] % 2 == 0:
        return (e[0] + e[1]) % 2, e[0] * -1, e[1]
    else:
        return (e[0] + e[1]) % 2, e[0] * -1, -1 * e[1]



def smoothdiagonal(e):
    return e[1] * e[0], e[0]


def diagonal_left_top(e):
    return e[0] + e[1], e[0]


def diagonal_right_top(e):
    return e[0] * -1 + e[1], e[0]

    
def diagonal_left_down(e):
    return e[0] + e[1] * -1, e[0]


def diagonal_right_down(e):
    return e[0] * -1 + e[1] * -1, e[0]


def chess_top(e):
    return (e[0] + e[1]) % 2, e[1], e[0]


def chess_down(e):
    return (e[0] + e[1]) % 2, e[1] * -1, e[0]


def chess_left(e):
    return (e[0] + e[1]) % 2, e[0], e[1]


def chess_right(e):
    return (e[0] + e[1]) % 2, e[0] * -1, e[1]    


def lbl_left(e):
    return e[0], e[1]


def lbl_right(e):
    return e[0] * -1, e[1]


def lbl_top(e):
    return e[1], e[0]


def lbl_down(e):
    return e[1] * -1, e[0]       
    

def rand(e):
    return random.random()