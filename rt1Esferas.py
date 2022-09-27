'''
archivo main: para poder dibujar las esferas del snowman
'''

from rayTracer import *
import snowman

ray = Raytracer(1000, 1000)

ray.scene = snowman.snowman

ray.render()
ray.write('rt1Snowman.bmp')
