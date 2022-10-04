from rayTracer import *
from material import *
import scenes

ray = Raytracer(1500, 1000)
ray.light = Light(
    position=V3(0, 0, 0),
    intensity=2,
    color=color(255, 255, 255)
)
ray.scene = scenes.bears

ray.render()
ray.write('rt2Bears.bmp')
