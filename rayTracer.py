'''
clase para poder crear objetos tipo rayTracer
'''
from math import *
import random
from turtle import back
from lib import *
from sphere import *
from color import *
from vector import *
from material import *
from light import *

LIGHTBLUE = color(173, 216, 230)
WHITE = color(255, 255, 255)
BLACK = color(0, 0, 0)


class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color = WHITE
        self.current_color = WHITE
        self.clear()
        self.scene = []
        self.density = 1

    def clear(self):
        self.framebuffer = [
            [self.background_color for x in range(self.width)]
            for y in range(self.height)
        ]

    def point(self, x, y, c=None):
        if y >= 0 and y < self.height and x >= 0 and x < self.width:
            self.framebuffer[y][x] = c.toBytes(
            ) or self.current_color.toBytes()

    def write(self, filename):
        writeBMP(filename, self.width, self.height, self.framebuffer)

    def render(self):
        fov = int(pi/2)
        ar = self.width/self.height
        tana = tan(fov/2)

        for y in range(self.height):
            for x in range(self.width):
                if random.random() < self.density:
                    i = ((2 * (x + 0.5) / self.width) - 1) * ar * tana
                    j = (1 - (2 * (y + 0.5) / self.height)) * tana

                    direction = V3(i, j, -1).normalize()
                    origin = V3(0, 0, 0)
                    c = self.cast_ray(origin, direction)

                    self.point(x, y, c)

    def cast_ray(self, origin, direction):
        material, intersect = self.scene_intersect(origin, direction)

        if material is None:
            return self.background_color

        light_dir = (self.light.position - intersect.point).normalize()

        dIntensity = light_dir @ intersect.normal
        diffuse = material.diffuse * dIntensity * material.albedo[0]

        light_dir = self.reflect(light_dir, intersect.normal)
        rIntensity = max(0, light_dir @ direction)
        specularI = self.light.intensity * rIntensity ** material.spec
        specular = self.light.color * specularI * material.albedo[1]

        return diffuse + specular

    def scene_intersect(self, origin, direction):
        zbuffer = 99999
        material = None
        intersect = None

        for o in self.scene:
            object_intersect = o.ray_intersect(origin, direction)
            if object_intersect:
                if object_intersect.distance < zbuffer:
                    zbuffer = object_intersect.distance
                    material = o.material
                    intersect = object_intersect
        return material, intersect

    def reflect(self, direction, normal):
        return (direction - normal * 2 * (direction @ normal)).normalize()
