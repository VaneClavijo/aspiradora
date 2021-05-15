import numpy as np
import random
class termite:
    maxLimit=5
    posiciones = np.array([maxLimit,maxLimit],
                          [-maxLimit,maxLimit],
                          [-maxLimit,-maxLimit],
                          [maxLimit,-maxLimit],
                          [0,0])
    def __init__(self,posicion=np.random.choice(posiciones), move=random.randint(1,2), color="red"):
        self.last_postion = posicion
        self.posicion = posicion
        self.color = color
        self.move = move
        self.load = None
        self.carga=0
    
    def moveUp(self, interval=1):
        self.posicion = (self.posicion[0], self.posicion[1] + interval)

    def moveDown(self, interval=1):
        self.posicion = (self.posicion[0], self.posicion[1] - interval)

    def moveRight(self, interval=1):
        self.posicion = (self.posicion[0] + interval, self.posicion[1])

    def moveLeft(self, interval=1):
        self.posicion = (self.posicion[0] - interval, self.posicion[1])


    def pickChip(self, Chips, posChips):
        if self.posicion in posChips:
            if Chips[posChips[self.posicion]].color != "white":
                self.load = posChips[self.posicion]
                self.carga=self.carga+1
                Chips[self.load].color = "white"
                return self.carga
    #def mov1 ():
    #def mov2 ():
    #def mov3 ():

class Chip:

    def __init__(self, index, posicion=(0, 0), color="blue"):
        self.posicion = posicion
        self.color = color
        self.index = index

    def getPos(self):
        return self.posicion

    def getColor(self):
        return self.color
