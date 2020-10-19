import random
import math 


class Pattern:


    def __init__(self, art_size, artx, arty):
        self.art_size = art_size
        self.artx = artx
        self.arty = arty
   

    def circle(self, e):
        center = ((self.artx + (self.artx + self.art_size[0]))//2, (self.arty + (self.arty + self.art_size[1]))//2)
        x2 = e[0]
        y2 = e[1]
        return math.sqrt((center[0] - x2) ** 2 + (center[1] - y2) ** 2)


    def snake_top(self, e):
        if e[1] % 2 == 0:
            return e[1], e[0]
        else:
            return e[1], -1 * e[0]


    def snake_left(self, e):
        if e[0] % 2 == 0:
            return e[0], e[1]
        else:
            return e[0], -1 * e[1]


    def snake_down(self, e):
        if e[1] % 2 == 0:
            return e[1] * -1, e[0]
        else:
            return e[1] * -1, -1 * e[0]


    def snake_right(self, e):
        if e[0] % 2 == 0:
            return e[0] * -1, e[1]
        else:
            return e[0] * -1, -1 * e[1]


    def chess_snake_top(self, e):
        if e[1] % 2 == 0:
            return (e[0] + e[1]) % 2, e[1], e[0]
        else:
            return (e[0] + e[1]) % 2, e[1], -1 * e[0]


    def chess_snake_left(self, e):
        if e[0] % 2 == 0:
            return (e[0] + e[1]) % 2, e[0], e[1]
        else:
            return (e[0] + e[1]) % 2, e[0], -1 * e[1]


    def chess_snake_down(self, e):
        if e[1] % 2 == 0:
            return (e[0] + e[1]) % 2, e[1] * -1, e[0]
        else:
            return (e[0] + e[1]) % 2, e[1] * -1, -1 * e[0]


    def chess_snake_right(self, e):
        if e[0] % 2 == 0:
            return (e[0] + e[1]) % 2, e[0] * -1, e[1]
        else:
            return (e[0] + e[1]) % 2, e[0] * -1, -1 * e[1]



    def smoothdiagonal(self, e):
        return e[1] * e[0], e[0]


    def diagonal_left_top(self, e):
        return e[0] + e[1], e[0]


    def diagonal_right_top(self, e):
        return e[0] * -1 + e[1], e[0]

        
    def diagonal_left_down(self, e):
        return e[0] + e[1] * -1, e[0]


    def diagonal_right_down(self, e):
        return e[0] * -1 + e[1] * -1, e[0]


    def chess_top(self, e):
        return (e[0] + e[1]) % 2, e[1], e[0]


    def chess_down(self, e):
        return (e[0] + e[1]) % 2, e[1] * -1, e[0]


    def chess_left(self, e):
        return (e[0] + e[1]) % 2, e[0], e[1]


    def chess_right(self, e):
        return (e[0] + e[1]) % 2, e[0] * -1, e[1]    


    def lbl_left(self, e):
        return e[0], e[1]


    def lbl_right(self, e):
        return e[0] * -1, e[1]


    def lbl_top(self, e):
        return e[1], e[0]


    def lbl_down(self, e):
        return e[1] * -1, e[0]       
        

    def rand(self, e):
        return random.random()