from vector import *
from intersect import *


class Triangle(object):
    def __init__(self, arrPoints, material):
        self.arrPoints = arrPoints
        self.material = material

    def side(self, v0, v1, v2, origin, direction):
        v0v1 = v1 - v0
        v0v2 = v2 - v0

        N = v0v1.cross(v0v2)

        raydirection = N @ direction

        if abs(raydirection) < 0.0001:
            return None

        d = N @ v0

        t = ((N @ origin) + d) / raydirection

        if t < 0:
            return None

        P = origin + (direction * t)

        U, V, W = self.barycentric(v0, v1, v2, P)

        if U < 0 or V < 0 or W < 0:
            return None
        else:
            return Intersect(distance=d,
                             point=P,
                             normal=N.normalize())

    def ray_intersect(self, origin, direction):
        v0, v1, v2, v3 = self.arrPoints
        sides = [
            self.side(v0, v2, v3, origin, direction),
            self.side(v0, v2, v1, origin, direction),
            self.side(v1, v2, v3, origin, direction),
            self.side(v0, v3, v1, origin, direction)
        ]

        t = float('inf')
        intersect = None

        for side in sides:
            if side is not None:
                if side.distance < t:
                    t = side.distance
                    intersect = side

        if intersect is None:
            return None

        return Intersect(distance=intersect.distance,
                         point=intersect.point,
                         normal=intersect.normal)

    def barycentric(self, A, B, C, P):
        cx, cy, cz = self.cross(
            V3(B.x - A.x, C.x - A.x, A.x - P.x),
            V3(B.y - A.y, C.y - A.y, A.y - P.y)
        )
        try:
            u = cx / cz
            v = cy / cz
            w = 1 - (u + v)
            return(w, v, u)
        except:
            u = - 1
            v = - 1
            w = 1 - u - v
            return (w, v, u)

    def cross(self, v1, v2):
        return (
            v1.y * v2.z - v1.z * v2.y,
            v1.z * v2.x - v1.x * v2.z,
            v1.x * v2.y - v1.y * v2.x
        )
