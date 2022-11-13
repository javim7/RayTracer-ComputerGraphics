from plane2 import *
from vector import *
from intersect import *


class Cube(object):
    def __init__(self, position, size, material):
        self.position = position
        self.size = size
        self.material = material
        self.planes = []

        halfSize = size / 2

        self.planes.append(
            Plane2((position + V3(halfSize, 0, 0)), V3(1, 0, 0), material))
        self.planes.append(
            Plane2((position + V3(-halfSize, 0, 0)), V3(-1, 0, 0), material))

        self.planes.append(
            Plane2((position + V3(0, halfSize, 0)), V3(0, 1, 0), material))
        self.planes.append(
            Plane2((position + V3(0, -halfSize, 0)), V3(0, -1, 0), material))

        self.planes.append(
            Plane2((position + V3(0, 0, halfSize)), V3(0, 0, 1), material))
        self.planes.append(
            Plane2((position + V3(0, 0, -halfSize)), V3(0, 0, -1), material))

    def ray_intersect(self, orig, direction):

        epsilon = 0.001

        boundsMin = [0, 0, 0]
        boundsMax = [0, 0, 0]

        boundsMin[0] = self.position.x - (epsilon + self.size / 2)
        boundsMax[0] = self.position.x + (epsilon + self.size / 2)
        boundsMin[1] = self.position.y - (epsilon + self.size / 2)
        boundsMax[1] = self.position.y + (epsilon + self.size / 2)
        boundsMin[2] = self.position.z - (epsilon + self.size / 2)
        boundsMax[2] = self.position.z + (epsilon + self.size / 2)

        t = float('inf')
        intersect = None

        for plane in self.planes:

            planeInter = plane.ray_intersect(orig, direction)

            if planeInter is not None:

                if planeInter.point.x >= boundsMin[0] and planeInter.point.x <= boundsMax[0]:
                    if planeInter.point.y >= boundsMin[1] and planeInter.point.y <= boundsMax[1]:
                        if planeInter.point.z >= boundsMin[2] and planeInter.point.z <= boundsMax[2]:
                            if planeInter.distance < t:
                                t = planeInter.distance
                                intersect = planeInter

        if intersect is None:
            return None

        return Intersect(distance=intersect.distance,
                         point=intersect.point,
                         normal=intersect.normal)
