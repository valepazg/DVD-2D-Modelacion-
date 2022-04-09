# Código obtenido del ejemplo Círculo del Aux3
import numpy as np

def translate(tx, ty, tz): #matriz de traslación en coordenadas homogéneas 
    #se le aplica una traslación tx, ty y tz a cada coordenada respectivamente
    return np.array([
        [1,0,0,tx],
        [0,1,0,ty],
        [0,0,1,tz],
        [0,0,0,1]], dtype = np.float32)


def scale(sx, sy, sz): #matriz de escalamiento en coordenadas homogéneas 
    #se le aplica un escalamiento sx, sy y sz a cada coordenada respectivamente
    return np.array([
        [sx,0,0,0],
        [0,sy,0,0],
        [0,0,sz,0],
        [0,0,0,1]], dtype = np.float32)


def rotationX(theta): #matriz de rotación en coordenadas homogéneas, con respecto a la coordenada x, segun un angulo theta
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    return np.array([
        [1,0,0,0],
        [0,cos_theta,-sin_theta,0],
        [0,sin_theta,cos_theta,0],
        [0,0,0,1]], dtype = np.float32)


def rotationY(theta): #matriz de rotación en coordenadas homogéneas, con respecto a la coordenada y, según un ángulo theta
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    return np.array([
        [cos_theta,0,sin_theta,0],
        [0,1,0,0],
        [-sin_theta,0,cos_theta,0],
        [0,0,0,1]], dtype = np.float32)


def rotationZ(theta): #matriz de rotación en coordenadas homogéneas, con respecto a la coordenada x, segun un angulo theta
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    return np.array([
        [cos_theta,-sin_theta,0,0],
        [sin_theta,cos_theta,0,0],
        [0,0,1,0],
        [0,0,0,1]], dtype = np.float32)


def matmul(mats):
    out = mats[0]
    for i in range(1, len(mats)):
        out = np.matmul(out, mats[i])

    return out