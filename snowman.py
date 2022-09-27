'''
archivo con las esferas para crear al snowman
'''
from rayTracer import *

'''
Colores a utilizar
'''
BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
ORANGE = color(255, 140, 0)
RED = color(255, 0, 0)
GREEN = color(0, 255, 0)

'''
Creando al snowman
'''
snowman = [
    # ---Esfera de arriba con sus adornos
    # ojos
    Sphere(V3(-0.4, -3.3, -15), 0.2, BLACK),
    Sphere(V3(0.4, -3.3, -15), 0.2, BLACK),
    # nariz
    Sphere(V3(0, -2.8, -15), 0.2, ORANGE),
    # bola de nieve 1
    Sphere(V3(0, -3, -15), 1.5, WHITE),

    # ---Esfera de en medio con sus adornos
    # botones
    Sphere(V3(0, -0.6, -15), 0.22, GREEN),
    Sphere(V3(0, 0.4, -15), 0.22, RED),
    # bola de nieve 2
    Sphere(V3(0, 0, -15), 2.0, WHITE),

    # ---Esfera de abajo con sus adornos
    # botones
    Sphere(V3(0, 2.5, -15), 0.25, GREEN),
    Sphere(V3(0, 3.5, -15), 0.25, RED),
    Sphere(V3(0, 4.5, -15), 0.25, GREEN),
    # bola de nieve 3
    Sphere(V3(0, 3, -15), 2.5, WHITE),
]
