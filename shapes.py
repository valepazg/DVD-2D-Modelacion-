# Código obtenido del ejemplo Círculo del Aux3
import numpy as np
from OpenGL.GL import *

SIZE_IN_BYTES = 4

# Clase que define los vértices de una figura y sus índices para poder formarla y dibujarla
class Shape:
    def __init__(self, vertexData, indexData):
        self.vertexData = vertexData
        self.indexData = indexData


def createPlumbob(r, g, b): # diamante que cambia de color en el logo
    vertexData = np.array([ #definición de vértices
        #positions          colors
        0.0,   0.0, 0.0,    r * 0.2,  g * 0.2,  b * 0.2,
        0.25,  0.5, 0.0,    r * 0.8,  g * 0.8,  b * 0.8,
        0.125, 0.0, 0.0,    r * 0.95, g * 0.95, b * 0.95,
        0.375, 0.0, 0.0,    r * 0.9,  g * 0.9,  b * 0.9,
        0.5,   0.0, 0.0,    r * 0.2,  g * 0.2,  b * 0.2,
        0.25, -0.5, 0.0,    r * 0.1,  g * 0.1,  b * 0.1], dtype = np.float32)

    indexData = np.array( #definición de índices
        [0, 1, 2,
         2, 1, 3,
         3, 1, 4,
         0, 5, 2,
         2, 5, 3,
         3, 5, 4], dtype= np.uint32)

    return Shape(vertexData, indexData)


def createCuadro(r, g, b): #creación de la HitBox

    vertexData = np.array([
    #   positions            colors
        -0.2, -0.2, 0.0,     r, g, b,
         0.2, -0.2, 0.0,     r, g, b,
         0.2,  0.2, 0.0,     r, g, b,
        -0.2,  0.2, 0.0,     r, g, b,
        ], dtype = np.float32)

    indexData = np.array(
        [0, 1, 2,
         2, 3, 0], dtype= np.uint32)

    return Shape(vertexData, indexData)



def createRect(r, g, b): #rectángulo para formar las letras D

    vertexData = np.array([
    #   positions             colors
        -0.04, -0.398, 0.0,   r, g, b,
         0.08, -0.398, 0.0,   r, g, b,
         0.12,  0.16,  0.0,   r, g, b,
         0.0,   0.16,  0.0,   r, g, b,
        ], dtype = np.float32)

    indexData = np.array(
        [0, 1, 2,
         2, 3, 0], dtype= np.uint32)

    return Shape(vertexData, indexData)

def createCircle(N, r, g, b): #medio círculo desde -pi/2 hasta pi/2 para formar las letras D

    vertexData = [
        # posicion          # color
        0.0, 0.0, 0.0,      r, g, b
    ]

    indexData = []

    dtheta = np.pi / N

    R = 0.5

    for i in range(N):
        theta = i * dtheta
        theta = theta - np.pi/2

        x = R * np.cos(theta)
        y = R * np.sin(theta)
        z = 0

        vertexData += [
            # pos    # color
            x, y, z, r, g, b
        ]

        indexData += [0, i, i+1]

    indexData += [0, N, 1]
    return Shape(vertexData, indexData)


def createTriangle(r, g, b):
    vertexData = np.array([  #   positions                   colors
        0.69, -0.5, 0.0,  r, g, b,
        0.3,   0.4, 0.0,  r, g, b,
        1.13,  0.4, 0.0,  r, g, b,
        ], dtype = np.float32)

    indexData = np.array(
        [0, 1, 2,], dtype= np.uint32)

    return Shape(vertexData, indexData)


def createEllipse(N, r, g, b):

    vertexData = [
        # posicion     # color
        0.0, 0.0, 0.0, r, g, b
    ]

    indexData = []

    dtheta = 2 * np.pi / N

    Rx = 0.5
    Ry = 0.5

    for i in range(N):
        theta = i * dtheta

        x = Rx * np.cos(theta)
        y = Ry * np.sin(theta)
        z = 0

        vertexData += [
            # pos    # color
            x, y, z, r, g, b
        ]

        indexData += [0, i, i+1]

    indexData += [0, N, 1]

    return Shape(vertexData, indexData)
