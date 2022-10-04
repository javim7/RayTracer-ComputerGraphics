'''
clase para poder controlar el color del raytracing.
'''


class color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __mul__(self, other):
        r = self.r
        g = self.g
        b = self.b

        if(type(other) == int or type(other) == float):
            r *= other
            g *= other
            b *= other
        else:
            r *= other.r
            g *= other.g
            b *= other.b

        r = min(255, max(r, 0))
        g = min(255, max(g, 0))
        b = min(255, max(b, 0))

        if r < 0:
            r = 0
        if r > 255:
            r = 255

        return color(int(r), int(g), int(b))

    def __add__(this, other):
        return color(
            this.r + other.r,
            this.g + other.g,
            this.b + other.b)

    def toBytes(self):
        return bytes([self.b, self.g, self.r])

    def ___repr__(self):
        return "color(%s, %s, %s)" % (self.r, self.g, self.b)
