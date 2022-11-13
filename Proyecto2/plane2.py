from vector import *
from intersect import *


class Plane2(object):
    def __init__(self, position, normal,  material):
        self.position = position
        self.normal = normal.normalize()
        self.material = material

    def ray_intersect(self, orig, dir):
        denom = dir @ self.normal
        if abs(denom) > 0.0001:
            t = (self.normal @ (self.position - orig)) / denom
            if t > 0:
                hit = orig + (dir * t)
                return Intersect(distance=t,
                                 point=hit,
                                 normal=self.normal,
                                 )

        return None
