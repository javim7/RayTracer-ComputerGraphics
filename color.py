'''
archivo para poder controlar el color del raytracing.
'''

def color(r, g, b):
  return bytes([b, g, r])


def clamping(numero):
    return int(max(min(numero, 255), 0))

def color_range(r, g, b):
  return color(clamping(r*255), clamping(g*255), clamping(b*255))

