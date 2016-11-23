# -*- coding: utf-8 -*-
# Copia todo esto en una celda de Jupyter y ejecútala (Shift+Intro).
#
# En otra celda programa lo que se pide en el ejercicio y para ver el
# resultado en Jupyter llama a la función dibujo() como última función
# de la celda.
#
# Por ejemplo:
#
# avanzar(100)
# girar(-pi/2)
# avanzar(50)
# dibujo()
#
# O para probar tus funciones:
#
# poligono(7,100)
# dibujo()
#
# No utilices la función dibujo() en el código que envíes en el
# examen.

from IPython.display import HTML, SVG, display
from math import pi, sin, cos

def avanzar(puntos):
    global current_pos, current_drawing
    pos1 = current_pos
    saltar(puntos)
    current_drawing += line(pos1, current_pos)
        
def saltar(puntos):
    global current_pos, current_angle
    x, y = current_pos
    current_pos = x + puntos*cos(current_angle), y + puntos*sin(current_angle)

def girar(radianes):
    global current_angle
    current_angle += radianes

def comenzar():
    global current_pos, current_angle
    current_pos = (200,200)
    current_angle = 0.

def limpiar():
    global current_drawing
    current_drawing = ''
    comenzar()

def dibujo():
    global current_drawing
    ret = SVG('''<svg width="400" height="400" viewBox="0 0 400 400"
                      xmlns="http://www.w3.org/2000/svg">{}</svg>'''\
               .format(current_drawing))
    limpiar()
    return ret

def line(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return '''<line x1="{}" y1="{}" 
                    x2="{}" y2="{}" 
                    stroke-width="1" stroke="black"/>'''.format(x1,y1,x2,y2)

limpiar()
