'''
clase para poder crear objetos tipo rayTracer
'''
from math import *
import random
from envmap import *
from lib import *
from sphere import *
from color import *
from vector import *
from material import *
from light import *
from plane import *

LIGHTBLUE = color(173, 216, 230)
BLUE = color(0, 0, 255)
WHITE = color(255, 255, 255)
BLACK = color(0, 0, 0)

MAX_RECURSION_DEPTH = 3


class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color = BLUE
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

    def get_background(self, direction):
        if self.envmap:
            return self.envmap.get_color(direction)
        else:
            return self.background_color

    def cast_ray(self, origin, direction, recursion=0):

        if recursion >= MAX_RECURSION_DEPTH:
            return self.get_background(direction)

        material, intersect = self.scene_intersect(origin, direction)

        if material is None:
            return self.get_background(direction)

        light_dir = (self.light.position - intersect.point).normalize()

        # reflection
        if material.albedo[2] > 0:
            reverse_direction = direction * -1
            reflect_direction = reflect(
                reverse_direction, intersect.normal)
            reflect_bias = -0.5 if reflect_direction @ intersect.normal < 0 else 0.5
            reflect_origin = intersect.point + \
                (intersect.normal * reflect_bias)
            reflect_color = self.cast_ray(
                reflect_origin, reflect_direction, recursion + 1)
        else:
            reflect_color = color(0, 0, 0)

        reflection = reflect_color * material.albedo[2]

        # refraction
        if material.albedo[3] > 0:
            refract_direction = refract(
                direction, intersect.normal, material.refractive_index)
            refract_bias = -0.5 if refract_direction @ intersect.normal < 0 else 0.5
            refract_origin = intersect.point + \
                (intersect.normal * refract_bias)
            refract_color = self.cast_ray(
                refract_origin, refract_direction, recursion + 1)
        else:
            refract_color = color(0, 0, 0)

        refraction = refract_color * material.albedo[3]

        shadow_bias = 1.1
        shadow_origin = intersect.point + (intersect.normal * shadow_bias)
        shadow_material, shadow_intersect = self.scene_intersect(
            shadow_origin, light_dir)

        shadow_intensity = 0
        if shadow_material:
            shadow_intensity = 0.7
        # aca termina codigo rt3

        dIntensity = light_dir @ intersect.normal
        diffuse = material.diffuse * dIntensity * \
            material.albedo[0] * \
            (1 - shadow_intensity)  # shadow intensity es de rt3

        light_dir = reflect(light_dir, intersect.normal)
        rIntensity = max(0, light_dir @ direction)
        specularI = self.light.intensity * rIntensity ** material.spec
        specular = self.light.color * specularI * material.albedo[1]

        return diffuse + specular + reflection + refraction

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
