'''
archivo con las esferas para crear al snowman
'''
from rayTracer import *
from material import *
from light import *
from color import *

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

'''
Creando los osos
'''

# colores para los osos en si
white = Material(diffuse=color(255, 255, 255), albedo=[1, 0], spec=0)
black = Material(diffuse=color(0, 0, 0), albedo=[0.9, 0.1], spec=30)
lightBrown = Material(diffuse=color(200, 158, 130), albedo=[1, 0], spec=0)
darkerBrown = Material(diffuse=color(178, 95, 3), albedo=[1, 0], spec=0)

# colores para las esferas metalicas
metalRed = Material(diffuse=color(255, 0, 0), albedo=[0.7, 0.3], spec=60)
metalGray = Material(diffuse=color(250, 250, 250), albedo=[0.9, 0.1], spec=60)

# dibujando las esferas
bears = [
    # cabezas
    Sphere(V3(-3.5, -2.4, -10), 1.8, white),
    Sphere(V3(3.5, -2.4, -10), 1.8, lightBrown),

    # orejas
    Sphere(V3(-4.8, -3, -9.1), 0.9, white),
    Sphere(V3(-1.4, -3.1, -9.9), 0.9, white),
    Sphere(V3(4.8, -3, -9.1), 0.9, darkerBrown),
    Sphere(V3(1.4, -3.1, -9.9), 0.9, darkerBrown),

    # bocas
    Sphere(V3(-3.2, -2.2, -9), 0.9, white),
    Sphere(V3(3.2, -2.2, -9), 0.9, darkerBrown),

    # narices
    Sphere(V3(-2.9, -2.1, -8), 0.2, black),
    Sphere(V3(2.9, -2.1, -8), 0.2, black),

    # Ojos
    Sphere(V3(-3.5, -2.8, -8), 0.2, black),
    Sphere(V3(-2.2, -2.7, -8), 0.2, black),
    Sphere(V3(3.5, -2.8, -8), 0.2, black),
    Sphere(V3(2.2, -2.7, -8), 0.2, black),

    # cuerpos
    Sphere(V3(-3.5, 0, -10), 2.2, metalGray),
    Sphere(V3(3.5, 0, -10), 2.2, metalRed),

    # brazos
    Sphere(V3(-4.9, -0.5, -8.7), 1, white),
    Sphere(V3(-1.3, -0.5, -9.4), 1, white),
    Sphere(V3(4.9, -0.5, -8.7), 1, darkerBrown),
    Sphere(V3(1.3, -0.5, -9.4), 1, darkerBrown),

    # piernas
    Sphere(V3(-4.5, 1.4, -8.5), 1, white),
    Sphere(V3(-1.6, 1.6, -9.1), 1, white),
    Sphere(V3(4.5, 1.4, -8.5), 1, darkerBrown),
    Sphere(V3(1.6, 1.6, -9.1), 1, darkerBrown),
]
