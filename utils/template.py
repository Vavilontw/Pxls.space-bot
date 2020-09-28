from PIL import Image


def find_color(x, y, cord, scale):
        for xx in range(scale):
            for yy in range(scale):
                if not cord[x + xx, y + yy] == (0,0,0,0) and cord[x + xx, y + yy][3] == 255:
                    return cord[x + xx, y + yy]
        return (0,0,0,0)

 
def detemplatize(image, scale):  
    cord = image.load()

    width = int(image.size[0] / scale)
    height = int(image.size[1] / scale)

    new_image = Image.new("RGBA", (width, height))
    new_cord = new_image.load()
        
    for x in range(0, image.size[0], scale):
        for y in range(0, image.size[1], scale):
            new_cord[x / scale, y / scale] = find_color(x, y, cord, scale)

    return new_image


def scale_detect(image):
    cord = image.load()
    return abs(cord[0,0][3] - cord[0,1][3])

