from texture import *


class Material:
    def __init__(self, diffuse, albedo, spec, refractive_index=0, textura=None):
        self.refractive_index = refractive_index
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        if textura:
            self.textura = Texture(textura)
        else:
            self.textura = None
