# Código obtenido del ejemplo Círculo del Aux3
import numpy as np
import glfw
from OpenGL.GL import *
from gpu_shape import GPUShape
from shaders import SimpleTransformShader
from shapes import createCircle
from shapes import createRect
from shapes import createTriangle
from shapes import createCuadro
from shapes import createPlumbob
from shapes import createEllipse
import transformations as tr
from classes import Controller
import sys

# Defrinicón sys
nombre = "Valeria"
iniciales = "VG"
rut = "19684903"

if len(sys.argv) == 4:
    nombre = sys.argv[1]
    iniciales = sys.argv[2]
    rut = sys.argv[3]

else:
    nombre = ""
    iniciales = ""
    rut = ""



# Creación del objeto Controller
controller = Controller()


def main():

    if not glfw.init():
        glfw.set_window_should_close(window, True)
        return -1

    width = 800
    height = 600

    window = glfw.create_window(width, height, "Tarea 1 Parte 1", None, None) #creacion de la ventana segun los parámetros de ancho y largo

    if not window: #condición para cuando no se crea la ventana
        glfw.terminate()
        glfw.set_window_should_close(window, True)
        return -1

    glfw.make_context_current(window)
 
    pipeline = SimpleTransformShader() #definición del Shader en la variable pipeline
    glUseProgram(pipeline.shaderProgram) #llamado para usar el Shader definido

    

    
# HitBox

    c0 = createCuadro(controller.c0.color[0], controller.c0.color[1], controller.c0.color[2]) #creación del Hit Box
    gpuC0 = GPUShape().initBuffers() #creación de buffers para la figura
    pipeline.setupVAO(gpuC0) #definicion de posición y color de vértices
    gpuC0.fillBuffers(c0.vertexData, c0.indexData) #define los arrays vertex e index en el buffer


# Comentarios análogos para la definición de las figuras siguientes

# Letra D
    c1 = createCircle(500, controller.c1.color[0], controller.c1.color[1], controller.c1.color[2]) # Medio círculo
    gpuC1 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuC1)
    gpuC1.fillBuffers(c1.vertexData, c1.indexData)

    c2 = createCircle(500, controller.c2.color[0], controller.c2.color[1], controller.c2.color[2]) # Medio círculo más pequeño
    gpuC2 = GPUShape().initBuffers()                                                         # y del mismo color que la HitBox
    pipeline.setupVAO(gpuC2)
    gpuC2.fillBuffers(c2.vertexData, c2.indexData)
    
    c3 = createRect(controller.c3.color[0], controller.c3.color[1], controller.c3.color[2]) # Rectángulo inclinado
    gpuC3 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuC3)
    gpuC3.fillBuffers(c3.vertexData, c3.indexData)


# Letra V

    v1 = createTriangle(controller.v1.color[0], controller.v1.color[1], controller.v1.color[2]) 
    gpuV1 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuV1)
    gpuV1.fillBuffers(v1.vertexData, v1.indexData)

    v2 = createTriangle(controller.v2.color[0], controller.v2.color[1], controller.v2.color[2])
    gpuV2 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuV2)
    gpuV2.fillBuffers(v2.vertexData, v2.indexData)

# Elipse 1

    e1 = createEllipse(500, controller.e1.color[0], controller.e1.color[1], controller.e1.color[2])
    gpuE1 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuE1)
    gpuE1.fillBuffers(e1.vertexData, e1.indexData)

# Elipse 2

    e2 = createEllipse(500, controller.e2.color[0], controller.e2.color[1], controller.e2.color[2])
    gpuE2 = GPUShape().initBuffers()
    pipeline.setupVAO(gpuE2)
    gpuE2.fillBuffers(e2.vertexData, e2.indexData)


    glClearColor(0.0, 0.0, 0.0, 1.0) # set de color de la ventana


    t0 = glfw.get_time() #contador de tiempo transcurrido
    
    

    while not glfw.window_should_close(window):

        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        
    
        t1 = glfw.get_time()
        dt = t1 - t0
        t0 = t1
     
        
        controller.changeDir() #llamado a la función que cambia la dirección del movimiento

        #Plumbob
        p0 = createPlumbob(controller.p0.color[0], controller.p0.color[1], controller.p0.color[2]) #diamante sobre el logo
        gpuP0 = GPUShape().initBuffers()
        pipeline.setupVAO(gpuP0)
        gpuP0.fillBuffers(p0.vertexData, p0.indexData)




# Hit Box
        # Aplicación de matrices de transformación a cada una de las figuras definidas.
        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.matmul([
            tr.translate(controller.c0.x - (0.002 * controller.c0.sc), controller.c0.y, 0.0), #traslación
            tr.scale(1.0 * controller.c0.sc, 1.0 * controller.c0.sc, 0.0), #escalamiento
            tr.rotationZ(controller.c0.rot) #rotación
        
        ]))
        pipeline.drawCall(gpuC0) #dibuja la figura en la ventana

    # Idem para las siguientes figuras

# Primera Letra D
        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.matmul([
            tr.translate(controller.c1.x - (0.1925 * controller.c1.sc) , controller.c1.y + (0.025 * controller.c1.sc), 0.0),
            tr.scale(0.25 * controller.c1.sc, 0.2 * controller.c1.sc, 0.0),
            tr.rotationZ(controller.c1.rot)
        ]))
        pipeline.drawCall(gpuC1)
        
        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.matmul([
            tr.translate(controller.c2.x - (0.1925 * controller.c2.sc) , controller.c2.y + (0.025 * controller.c2.sc), 0.0),
            tr.scale(0.1875 * controller.c2.sc, 0.1375 * controller.c2.sc, 0.0),
            tr.rotationZ(controller.c2.rot)
        ]))
        pipeline.drawCall(gpuC2)

        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.matmul([
            tr.translate(controller.c3.x - (0.1925 * controller.c3.sc) , controller.c3.y + (0.025 * controller.c3.sc), 0.0),
            tr.scale(controller.c3.sc * 0.25, controller.c3.sc * 0.25, 0.0),
            tr.rotationZ(controller.c3.rot)
        
        ]))
        pipeline.drawCall(gpuC3)



# Segunda Letra D
        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.matmul([
            tr.translate(controller.c1.x + (0.07 * controller.c1.sc) , controller.c1.y + (0.025 * controller.c1.sc), 0.0),
            tr.scale(0.25 * controller.c1.sc, 0.2 * controller.c1.sc, 0.0),
            tr.rotationZ(controller.c1.rot)
        ]))
        pipeline.drawCall(gpuC1)
        
        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.matmul([
            tr.translate(controller.c2.x + (0.07 * controller.c2.sc) , controller.c2.y + (0.025 * controller.c2.sc), 0.0),
            tr.scale(0.1875 * controller.c2.sc, 0.1375 * controller.c2.sc, 0.0),
            tr.rotationZ(controller.c2.rot)
        ]))
        pipeline.drawCall(gpuC2)

        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.matmul([
            tr.translate(controller.c3.x + (0.07 * controller.c3.sc) , controller.c3.y + (0.025 * controller.c3.sc), 0.0),
            tr.scale(controller.c3.sc * 0.25, controller.c3.sc * 0.25, 0.0),
            tr.rotationZ(controller.c3.rot)
        
        ]))
        pipeline.drawCall(gpuC3)
    
    # Letra V
        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.matmul([
            tr.translate(controller.v1.x - (0.1925 * controller.v1.sc), controller.v1.y + (0.025 * controller.v1.sc), 0.0),
            tr.scale(0.25 * controller.v1.sc, 0.25 * controller.v1.sc, 0.0),
            tr.rotationZ(controller.v1.rot)
        
        
        ]))
        pipeline.drawCall(gpuV1)

        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.matmul([
            tr.translate(controller.v2.x - (0.1225 * controller.v2.sc), controller.v2.y + (0.07 * controller.v2.sc), 0.0),
            tr.scale(0.15 * controller.v2.sc , 0.15 * controller.v2.sc, 0.0),
            tr.rotationZ(controller.v2.rot)
        
        
        ]))
        pipeline.drawCall(gpuV2)

    # Elipse 1

        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.matmul([
            tr.translate(controller.e1.x - (0.0125 * controller.e1.sc), controller.e1.y - (0.15 * controller.e1.sc), 0.0),
            tr.scale(0.325 * controller.e1.sc , 0.075 * controller.e1.sc, 0.0),
            tr.rotationZ(controller.e1.rot)
        
        
        ]))
        pipeline.drawCall(gpuE1)

    # Elipse 2

        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.matmul([
            tr.translate(controller.e2.x - (0.0125 * controller.e2.sc), controller.e2.y - (0.15 * controller.e2.sc), 0.0),
            tr.scale(0.1 * controller.e2.sc , 0.0375 * controller.e2.sc, 0.0),
            tr.rotationZ(controller.e2.rot)
        
        ]))
        pipeline.drawCall(gpuE2)

    # Plumbob
        glUniformMatrix4fv(glGetUniformLocation(pipeline.shaderProgram, "transform"), 1, GL_TRUE, tr.matmul([
            tr.translate(controller.p0.x - (0.055 * controller.p0.sc), controller.p0.y + (0.1125 * controller.p0.sc), 0.0),
            tr.scale(0.15 * controller.p0.sc, 0.15 * controller.p0.sc, 0.0),
            tr.rotationZ(controller.p0.rot)
        
        
        ]))
        pipeline.drawCall(gpuP0)


        glfw.swap_buffers(window) #intercambio de buffers con la ventana 
        controller.update(dt) #actualiza la posción de las figuras según la función changeDir()
    

    # Limpia cada una de las figuras para liberar memoria
    gpuC0.clear()
    gpuC1.clear()
    gpuC2.clear()
    gpuC3.clear()
    gpuV1.clear()
    gpuV2.clear()
    gpuE1.clear()
    gpuE2.clear()
    gpuP0.clear()
 

    glfw.terminate()

    return 0

if __name__ == "__main__": #llama a la función main para que se ejecute repetidamente, mientras la ventana esté abierta
    main()
