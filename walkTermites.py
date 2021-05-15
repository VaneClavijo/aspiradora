import numpy as np
import random as r
#import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
import turtle as t
limits=[5,-5,5,-5]

class Chip:

    def __init__(self, index, posicion=(0, 0), color="blue"):
        self.posicion = posicion
        self.color = color
        self.index = index

    def getPos(self):
        return self.posicion

    def getColor(self):
        return self.color

def crearListaChips(numeroChips):    
    chipList = np.array([])
    clist = np.array([]) 
    for pi in range (numeroChips):
        chipList=np.append(chipList,Chip(pi,(r.randint(-5, 5), r.randint(-5, 5))))
        clist.append(t.Turtle(shape="square"))#agrega a la lista de turtles de chip
        clist[pi].color(chipList[pi].getColor())
        clist[pi].speed(0)  # Asigna la velocidad mas alta posible
        clist[pi].shapesize(0.2, 0.5)  # Asigna el tamano de forma
        clist[pi].penup()  # Pen up para no dejar rastro del camino
        clist[pi].goto(chipList[pi].getPos())# Va a la posicion inicial de cada chip
    return chipList,clist

chipList,clist=crearListaChips(10)
t.getscreen()