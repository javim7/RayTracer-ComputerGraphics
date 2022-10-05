from rayTracer import *

ray = Raytracer(1000, 1000)

rubber = Material(diffuse=color(100, 0, 0), albedo=[0.9, 0.1, 0], spec=10)
ivory = Material(diffuse=color(255, 255, 255), albedo=[0.6, 0.3, 0], spec=50)
mirror = Material(diffuse=color(255, 255, 255), albedo=[0, 1, 0.8], spec=1425)

ray = Raytracer(800, 600)

ray.light = Light(
    position=V3(-20, 20, 20),
    intensity=2,
    color=color(255, 255, 255)
)

ray.scene = [
    Sphere(V3(0, -1.5, -10), 1.5, ivory),
    Sphere(V3(-2, -1, -12), 2, mirror),
    Sphere(V3(1, 1, -8), 1.7, rubber),
    Sphere(V3(-2, 2, -10), 2, mirror)
]

ray.render()
ray.write('prueba.bmp')
