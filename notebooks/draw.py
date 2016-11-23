# Esta implementación hace uso del módulo turtle que también está
# disponible en Brython y Skulpt.  Pero no incluyas este código en
# tu respuesta al examen.

import turtle
from math import pi

t = turtle.Turtle()

def avanzar(puntos):
    t.pendown()
    t.forward(puntos)

def girar(radianes):
    grados = radianes*180/pi
    if grados < 0: t.left(-grados)
    else: t.right(grados)
    
def comenzar():
    t.penup()
    t.home()
    
def saltar(puntos):
    t.penup()
    t.forward(puntos)
