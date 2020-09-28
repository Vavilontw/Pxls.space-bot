from PIL import ImageColor

def art2xy(art):
    xy=[]
    for pxl in art:
        xy.append((pxl[0], pxl[1]))
    return xy


def get_diff(art, board):
    board = set(board)
    art = set(art)
    return list(art.difference(board))


def art2list(file, palette, artx, arty):

    pic = []
    newpic = []
    rgba = []
    cord = file.load()

    for i in palette:
        palette.insert(palette.index(i), i + "FF")
        palette.remove(i)

    for x in range(file.size[0]):
        for y in range(file.size[1]):
            pic.append((x, y, cord[x, y]))

    for i in range(len(palette)):
        palette[i] = (ImageColor.getcolor(palette[i], "RGBA"))
        rgba.append(palette[i]) 

    for i in pic:
        if i[2] in rgba:
            newpic.append((i[0], i[1], rgba.index(i[2])))

    return [(i[0]+artx, i[1]+arty, i[2]) for i in newpic]

