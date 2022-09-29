'''
archivo main: para poder dibujar las esferas del snowman
'''

from rayTracer import *
from material import *
# import snowman

red = Material(diffuse=color(255, 0, 0))
white = Material(diffuse=color(255, 255, 255))

ray = Raytracer(800, 800)
ray.light = Light(V3(-3, -2, 0), 1)
ray.scene = [
    Sphere(V3(-3, 0, -16), 2, red),
    Sphere(V3(2.8, 0, -10), 2., white)
]

ray.render()
ray.write('prueba.bmp')
