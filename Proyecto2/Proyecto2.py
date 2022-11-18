from rayTracer import *

'''
Instanciando el raytracer
'''
ray = Raytracer(600, 600)

'''
Materiales a utilizar
'''
metallic = Material(diffuse=color(128, 128, 128),
                    albedo=[0.7, 0.3, 0.0, 0.0], spec=10)
metallicDark = Material(diffuse=color(100, 100, 100),
                        albedo=[0.7, 0.3, 0.0, 0.0], spec=10)
red = Material(diffuse=color(255, 0, 0), albedo=[0.9, 0.2, 0, 0], spec=100)
orange = Material(diffuse=color(255, 166, 0),
                  albedo=[0.9, 0.2, 0, 0], spec=100)
white = Material(diffuse=color(255, 255, 255),
                 albedo=[1, 1, 1, 0], spec=100)
black = Material(diffuse=color(0, 0, 0),
                 albedo=[1, 1, 1, 0], spec=100)
yellow = Material(diffuse=color(255, 255, 0),
                  albedo=[0.9, 0.1, 0, 0], spec=100)
green = Material(diffuse=color(0, 255, 0),
                 albedo=[0.9, 0.2, 0, 0], spec=100)
blue = Material(diffuse=color(0, 0, 255),
                albedo=[0.9, 0.2, 0, 0], spec=100)
skyBlue = Material(diffuse=color(135, 206, 235),
                   albedo=[0.9, 0.2, 0, 0], spec=100)
mirror = Material(diffuse=color(255, 255, 255),
                  albedo=[0, 1, 0.8, 0], spec=1430)
glass = Material(diffuse=color(150, 180, 200), albedo=[
                 0, 0.5, 0.1, 0.8], spec=125, refractive_index=1.5)

'''
Ajustando la luz
'''
ray.light = Light(
    position=V3(-20, 20, 20),
    intensity=2,
    color=color(255, 255, 255)
)


'''
Creando la escena
'''
ray.scene = [

    # --------------------PISO-----------------------#
    Plane(V3(0.0, -2.4, -5), 1.5, 1.5, white),  # central
    Plane(V3(1.5, -2.4, -5), 1.5, 1.5, red),  # derecha
    Plane(V3(3.0, -2.4, -5), 1.5, 1.5, white),  # derecha
    Plane(V3(-1.5, -2.4, -5), 1.5, 1.5, red),  # izquierda
    Plane(V3(-3.0, -2.4, -5), 1.5, 1.5, white),  # izquierda

    Plane(V3(0.0, -2.4, -6), 1.5, 3.0, red),  # central
    Plane(V3(1.5, -2.4, -6), 1.5, 3.0, white),  # deracha
    Plane(V3(3.0, -2.4, -6), 1.5, 3.0, red),  # derecha
    Plane(V3(4.5, -2.4, -6), 1.5, 3.0, white),  # tile extra derecha
    Plane(V3(-1.5, -2.4, -6), 1.5, 3.0, white),  # izquierda
    Plane(V3(-3.0, -2.4, -6), 1.5, 3.0, red),  # izquierd
    Plane(V3(-4.5, -2.4, -6), 1.5, 3.0, white),  # tile extra izquierda

    Plane(V3(0.0, -2.4, -8), 1.5, 4.5, white),  # central
    Plane(V3(1.5, -2.4, -8), 1.5, 4.5, red),  # derecha
    Plane(V3(3.0, -2.4, -8), 1.5, 4.5, white),  # derecha
    Plane(V3(4.5, -2.4, -8), 1.5, 4.5, red),  # derecha
    Plane(V3(6.0, -2.4, -8), 1.5, 4.5, white),  # tile extra derecha
    Plane(V3(-1.5, -2.4, -8), 1.5, 4.5, red),  # izquierda
    Plane(V3(-3.0, -2.4, -8), 1.5, 4.5, white),  # izquierda
    Plane(V3(-4.5, -2.4, -8), 1.5, 4.5, red),  # izquierda
    Plane(V3(-6.0, -2.4, -8), 1.5, 4.5, white),  # tile extra izquierda

    # --------------------MESA-----------------------#
    Plane(V3(0, -1.5, -6), 3.5, 1.5, glass),  # mesa de vidrio
    Sphere(V3(0, 1.0, -5), 0.3, mirror),  # adorno esferico

    Cube(V3(-1.5, 1.5, -5), 0.2, metallic),  # pata izquierda frontal
    Cube(V3(-1.5, 1.7, -5), 0.2, metallic),  # pata izquierda frontal
    Cube(V3(-1.5, 1.9, -5), 0.2, metallic),  # pata izquierda frontal
    Cube(V3(-1.5, 2.1, -5), 0.2, metallic),  # pata izquierda frontal

    Cube(V3(-1.5, 1.8, -6), 0.2, metallicDark),  # pata izquierda trasera
    Cube(V3(-1.5, 2.0, -6), 0.2, metallicDark),  # pata izquierda trasera

    Cube(V3(1.5, 1.5, -5), 0.2, metallic),  # pata derecha frontal
    Cube(V3(1.5, 1.7, -5), 0.2, metallic),  # pata derecha frontal
    Cube(V3(1.5, 1.9, -5), 0.2, metallic),  # pata derecha frontal
    Cube(V3(1.5, 2.1, -5), 0.2, metallic),  # pata derecha frontal

    Cube(V3(1.5, 1.8, -6), 0.2, metallicDark),  # pata derecha trasera
    Cube(V3(1.5, 2.0, -6), 0.2, metallicDark),  # pata derecha trasera

    # --------------------RUBKIS CUBES-----------------------#
    Cube(V3(0.9, 1.3, -5), 0.15, yellow),  # fila abajo
    Cube(V3(1.05, 1.3, -5), 0.15, white),  # fila abajo
    Cube(V3(1.2, 1.3, -5), 0.15, orange),  # fila abajo

    Cube(V3(0.9, 1.15, -5), 0.15, blue),  # fila enmedio
    Cube(V3(1.05, 1.15, -5), 0.15, red),  # fila enmedio
    Cube(V3(1.2, 1.15, -5), 0.15, green),  # fila enmedio

    Cube(V3(0.9, 1.0, -5), 0.15, orange),  # fila arriba
    Cube(V3(1.05, 1.0, -5), 0.15, green),  # fila arriba
    Cube(V3(1.2, 1.0, -5), 0.15, yellow),  # fila arriba

    # --------------------PINTURA-----------------------#
    Triangle([V3(-3.5, -0.5, -10), V3(0, -2, -10),
             V3(3.5, -0.5, -10), V3(-3.5, -0.5, -10)], metallic),  # triangulo 1
    Triangle([V3(-3.5, -3.5, -10), V3(0, -2, -10),
             V3(3.5, -3.5, -10), V3(-3.5, -3.5, -10)], metallic),  # triangulo 2
    Triangle([V3(-3.5, -0.5, -10), V3(-3.5, -3.5, -10),
             V3(0, -2, -10), V3(-3.5, -0.5, -10)], metallicDark),  # triangulo 3
    Triangle([V3(0, -2, -10), V3(3.5, -3.5, -10),
             V3(3.5, -0.5, -10), V3(0, -2, -10)], metallicDark),  # triangulo 4

]


'''
Agregando fondo y escribiendo la escena
'''
ray.envmap = Envmap('./Proyecto2/texturas/white.bmp')
ray.render()
ray.write('./Proyecto2/proyecto2.bmp')
