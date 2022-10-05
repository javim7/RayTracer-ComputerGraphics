'''
archivo main: para poder dibujar las esferas del snowman
'''

from rayTracer import *
import scenes

ray = Raytracer(1000, 1000)

ray.scene = scenes.snowman

ray.render()
ray.write('rt1Snowman.bmp')
