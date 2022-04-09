from colors import data_colors
import numpy as np
from random import randint

# Condiciones iniciales de posición
x0 = 0.0
y0 = 0.0

# Valores fijos de escala
scl = 1.0
nscl = 1.5 #(19684903 / 20000000) ** 3 (el valor de enunciado no permite notar el efecto del escalamiento)


# Condiciones de velocidad de la figura
iniciales= "VG"    
alpha = ord(iniciales[0]) * ord(iniciales[1])

x = 350 * np.cos(alpha)
y = 350 * np.sin(alpha)

vx = 2 * (x/800)
vy = 2 * (y/600)


# Condiciones para el color de la figura
tuNombre = "Valeria"
l = len(tuNombre)
r = (ord(tuNombre[0%l]) * ord(tuNombre[1%l]) % 255) / 255
g = (ord(tuNombre[2%l]) * ord(tuNombre[3%l]) % 255) / 255
b = (ord(tuNombre[4%l]) * ord(tuNombre[5%l]) % 255) / 255

color_logo = [r, g, b]
color_hitbox = [10/255, 10/255, 10/255]
color_plumbob0 = [0.0, 1.0, 0.0]


# Condición inicial para la rotación de figuras
phi = 0

# class Controller y class Satellite inspiradas del ejemplo Gravedad Aux3
class Controller: # Clase que permite agrupar los parámetros de posicion, velocidad, color, escala y rotacion de cada figura
    def __init__(self): # Llama a la clase Satellite para agrupar todas las figuras y obtener funciones generales
        self.c0 = Satellite(x0, y0, vx, vy, scl, color_hitbox, phi)
        self.c1 = Satellite(x0, y0, vx, vy, scl, color_logo, phi)
        self.c2 = Satellite(x0, y0, vx, vy, scl, color_hitbox, phi)
        self.c3 = Satellite(x0, y0, vx, vy, scl, color_logo, phi)
        self.v1 = Satellite(x0, y0, vx, vy, scl, color_logo, phi)
        self.v2 = Satellite(x0, y0, vx, vy, scl, color_hitbox, phi)
        self.e1 = Satellite(x0, y0, vx, vy, scl, color_logo, phi)
        self.e2 = Satellite(x0, y0, vx, vy, scl, color_hitbox, phi)
        self.p0 = Satellite(x0, y0, vx, vy, scl, color_plumbob0, phi)
    
    
    # Función que actualiza globalmente las posiciones de todas las figuras
    def update(self, dt):
        self.c0.update(dt)
        self.c1.update(dt)
        self.c2.update(dt)
        self.c3.update(dt)
        self.v1.update(dt)
        self.v2.update(dt)
        self.e1.update(dt)
        self.e2.update(dt)
        self.p0.update(dt)
    

    # Función para llamar los cambios de dirección de cada figura en un solo llamdo en el archivo t1p1.py
    def changeDir(self):
        self.c0.changeDir(self.c0, self.p0)
        self.c1.changeDir(self.c0, self.p0)
        self.c2.changeDir(self.c0, self.p0)
        self.c3.changeDir(self.c0, self.p0)
        self.v1.changeDir(self.c0, self.p0)
        self.v2.changeDir(self.c0, self.p0)
        self.e1.changeDir(self.c0, self.p0)
        self.e2.changeDir(self.c0, self.p0)
        self.p0.changeDir(self.c0, self.p0)

   

class Satellite: # Clase que permite controlar los parámetros de posicion, velocidad, color, escala y rotacion de cada figura
    def __init__(self, x, y, velx, vely, sc, color, rot):
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely
        self.sc = sc
        self.color = color
        self.rot = rot
    

    # Funciones compuestas que actualizan la posición de una figura específica
    def update(self, dt):
        self.updatePos(dt)

    def updatePos(self, dt):
        self.x += self.velx*dt
        self.y += self.vely*dt
        

    # Función que permite setear parámetros de posición, escalamiento y rotación según las condiciones de borde de la ventana
    # Inspirada en el ejemplo collisions.py
    def changeDir(self,figure, plumbob):

    # Right
        if figure.x + 0.2 > 1.0:
            self.velx = -(self.velx) #cambia la dirección de movimiento

            indice = randint(0, len(data_colors)-1) #cambia el color de la figura plumbob de manera aleatoria
            plumbob.color = data_colors[indice]

            #self.rot += np.pi/2 (se deja como comentario ya que al rotar la figura se deforma)

            if self.sc == scl: #cambio de escala de la figura
                self.sc = nscl
            else:
                self.sc = scl
        
    # Lo mismo anterior se repite para los demás bordes de la ventana

    # Left
        if figure.x - 0.2 < -1.0:
            self.velx = -(self.velx)

            indice = randint(0, len(data_colors)-1)
            plumbob.color = data_colors[indice]

            #self.rot += np.pi/2

            if self.sc == scl:
                self.sc = nscl
            else:
                self.sc = scl

    # Top
        if figure.y + 0.2 > 1.0:
            self.vely = -(self.vely)

            indice = randint(0, len(data_colors)-1)
            plumbob.color = data_colors[indice]

            #self.rot += (np.pi/2)

            if self.sc == scl:
                self.sc = nscl
            else:
                self.sc = scl

    # Bottom
        if figure.y - 0.2 < -1.0:
            self.vely = -(self.vely)

            indice = randint(0, len(data_colors)-1)
            plumbob.color = data_colors[indice]

            #self.rot += (np.pi/2)

            if self.sc == scl:
                self.sc = nscl
            else:
                self.sc = scl
    





    