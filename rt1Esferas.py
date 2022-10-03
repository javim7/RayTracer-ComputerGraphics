'''
archivo main: para poder dibujar las esferas del snowman
'''

from rayTracer import *
from material import *
# import snowman

rubber = Material(diffuse=color(255, 0, 0), albedo=[0.9])
ivory = Material(diffuse=color(255, 255, 255), albedo=[0.6])

ray = Raytracer(800, 800)
ray.light = Light(V3(-3, -2, 0), 1)
ray.scene = [
    Sphere(V3(-3, 0, -16), 2, rubber),
    Sphere(V3(2.8, 0, -10), 2., ivory)
]

ray.render()
ray.write('prueba.bmp')
