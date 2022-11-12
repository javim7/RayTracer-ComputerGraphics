from rayTracer import *

ray = Raytracer(1000, 700)

rubber = Material(diffuse=color(100, 0, 0), albedo=[0.9, 0.1, 0, 0], spec=10)
ivory = Material(diffuse=color(255, 255, 255),
                 albedo=[0.6, 0.3, 0.1, 0], spec=50)
mirror = Material(diffuse=color(255, 255, 255),
                  albedo=[0, 1, 0.8, 0], spec=1425)
glass = Material(diffuse=color(150, 180, 200), albedo=[
                 0, 0.5, 0.1, 0.8], spec=125, refractive_index=1.5)


ray.light = Light(
    position=V3(-20, 20, 20),
    intensity=2,
    color=color(255, 255, 255)
)

ray.scene = [
    # Sphere(V3(0, -1.5, -10), 1.5, ivory),
    # Sphere(V3(0, 0, -5), 0.5, glass),
    # Sphere(V3(1, 1, -8), 1.7, rubber),
    # Sphere(V3(-2, 1, -10), 2, mirror),
    # Plane(V3(0, 2.2, -5), 2, 2, glass),
]

ray.envmap = Envmap('./RT3/texturas/minecraft1.bmp')

ray.render()
ray.write('./RT3/proyecto2.bmp')
