class Material:
    def __init__(self, diffuse, albedo, spec, refractive_index=0, textura=None):
        self.refractive_index = refractive_index
        self.diffuse = diffuse
        self.textura = textura
        self.albedo = albedo
        self.spec = spec
