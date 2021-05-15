import turtle as t
import random as rd
import math
max=5
posInicio=[max,-max,0]
posY=[max,-max]

class Termite:
    def __init__(self, posicionX=rd.choice(posInicio), color="red"):
        #para definir la posicion de partida
        if(posicionX==0):#para que empice en el centro cuando x=0
            posicionY=0
        else:
            posicionY=rd.choice(posY)
        self.last_postion = (posicionX,posicionY)#(0,0) para probar la espiral
        self.posicion = (posicionX,posicionY)#(0,0) para probar la espiral
        self.color = color
        self.load = None

    def getPos(self):
        return self.posicion

    def getColor(self):
        return self.color

class Chip:

    def __init__(self, index, posicion=(0, 0), color="blue"):
        self.posicion = posicion
        self.color = color
        self.index = index

    def getPos(self):
        return self.posicion

    def getColor(self):
        return self.color
    #clase para probar validez del codigo   
    def imprimit(self):
        print(self.posicion)


def crearChips(numChips):
    t.setup(900, 900, 200, 100)#tamano de la pantalla y ubicacion
    t.screensize(90, 900)#tamano pantalla de dibujo
    t.setworldcoordinates(-max-2,-max-2,max+2,max+2)#coordenadas del mundo
    chipList = []#arreglo de chips 
    clist= []#arreglo de tortugas para chips
    for i in range (numChips):
        chipList.append(Chip(i, (rd.randint(-max, max), rd.randint(-max, max))))#agrego chips random a
        #chipList[i].imprimit()
        clist.append(t.Turtle(shape="square"))#agrego tortuga para representar chip
        clist[i].color(chipList[i].getColor())#establezco el color de la lista chips
        clist[i].speed(0)  # Asigna la velocidad mas alta posible
        clist[i].shapesize(0.2, 0.5)  # Asigna el tamano de forma
        clist[i].penup()  # Pen up para no dejar rastro del camino
        clist[i].goto(chipList[i].getPos())#envia a cada chip a cada posicion
    aspiradora=Termite()#creo aspiradora
    #print(aspiradora.getPos())
    asp=t.Turtle(shape="turtle")#da la forma de tortuga
    asp.speed(10)  # Asigna la velocidad mas alta posible
    asp.shapesize(0.6, 0.9)  # Asigna el tamano de forma
    asp.penup()  # Pen up para no dejar rastro del camino
    asp.goto(aspiradora.getPos()) # Va a la posicion inicial de cada termite
    posChips = {c.getPos(): c.index for c in chipList}#arreglo con posiciones de los chips
    return aspiradora, asp, posChips, chipList, clist#retorna los elementos del mundo

def pickChip(aspiradora, Chips, posChips):#funcion para recoger chips
    if aspiradora.posicion in posChips:
        if Chips[posChips[aspiradora.posicion]].color != "white":
            aspiradora.load = posChips[aspiradora.posicion]
            Chips[aspiradora.load].color = "white"
            return aspiradora.posicion

def borrar(aspiradora, chipList, posChips,clist):#funcion para borrar chip del mundo
    posT=pickChip(aspiradora, chipList, posChips)
    if posT is not None:
        ind = posChips[posT]
        clist[ind].color(chipList[ind].getColor())
        clist[ind].goto(chipList[ind].getPos())
'''las funciones redactadas a continuacion son cada uno de los movimientos que debe hacer tanto la aspiradora como su tortuga en estas funciones se implementa la funcion de recoger y borrar'''
def arriba (aspiradora, asp, posChips, chipList, clist):
    asp.goto(asp.position()+(0,1))
    aspiradora.posicion=asp.position()
    borrar(aspiradora, chipList, posChips,clist)
def abajo (aspiradora, asp, posChips, chipList, clist):
    asp.goto(asp.position()+(0,-1))
    aspiradora.posicion=asp.position()
    borrar(aspiradora, chipList, posChips,clist)

def izquierda (aspiradora, asp, posChips, chipList, clist):
    asp.goto(asp.position()+(-1,0))
    aspiradora.posicion=asp.position()
    borrar(aspiradora, chipList, posChips,clist)

def derecha (aspiradora, asp, posChips, chipList, clist):
    asp.goto(asp.position()+(1,0))
    aspiradora.posicion=asp.position()
    borrar(aspiradora, chipList, posChips,clist)
'''en esta funcion se implementa los movimientos adecuados con intervalos para que describa el movimiento de un cuadrado tomando en cuenta su posicion inicial'''
def cuadrado(aspiradora, asp, posChips, chipList, clist):
    if(asp.position()==(max, max)):
        for j in range(max):    
            for i in range(2*(max-i)):
                abajo(aspiradora, asp, posChips, chipList, clist)
            for i in range(2*(max-i)):
                izquierda(aspiradora, asp, posChips, chipList, clist)
            for i in range(2*(max-i)):
                arriba (aspiradora, asp, posChips, chipList, clist)
            for i in range(2*(max-i)):
                derecha(aspiradora, asp, posChips, chipList, clist)
    elif(asp.position()==(-max, max)):
        for j in range(max): 
            for i in range(2*(max-i)):
                derecha(aspiradora, asp, posChips, chipList, clist)
            for i in range(2*(max-i)):
                abajo(aspiradora, asp, posChips, chipList, clist)
            for i in range(2*(max-i)):
                izquierda(aspiradora, asp, posChips, chipList, clist)
            for i in range(2*(max-i)):
                arriba (aspiradora, asp, posChips, chipList, clist) 
    elif(asp.position()==(-max, -max)):
        for j in range(max): 
            for i in range(2*(max-i)):
                arriba (aspiradora, asp, posChips, chipList, clist)
            for i in range(2*(max-i)):
                derecha(aspiradora, asp, posChips, chipList, clist)
            for i in range(2*(max-i)):
                abajo(aspiradora, asp, posChips, chipList, clist)
            for i in range(2*(max-i)):
                izquierda(aspiradora, asp, posChips, chipList, clist)
    elif(asp.position()==(max, -max)):
        for i in range(2*(max-i)):
            izquierda(aspiradora, asp, posChips, chipList, clist)
        for i in range(2*(max-i)):
            arriba (aspiradora, asp, posChips, chipList, clist)
        for i in range(2*(max-i)):
            derecha(aspiradora, asp, posChips, chipList, clist)
        for i in range(2*(max-i)):
            abajo(aspiradora, asp, posChips, chipList, clist)
    '''en esta funcion se implementa los movimientos adecuados con intervalos para que describa el movimiento de una serpiente tomando en cuenta su posicion inicial'''
def serpiente(aspiradora, asp, posChips, chipList, clist):
    if(asp.position()==(max, max)):
        for j in range(max+1):
            for i in range(2*max):
                izquierda(aspiradora, asp, posChips, chipList, clist)
            abajo(aspiradora, asp, posChips, chipList, clist)
            for i in range(2*max):
                derecha(aspiradora, asp, posChips, chipList, clist)
            abajo(aspiradora, asp, posChips, chipList, clist)    
    elif(asp.position()==(-max, max)):
        for j in range(max+1):
            for i in range(2*max):
                derecha(aspiradora, asp, posChips, chipList, clist)
            abajo(aspiradora, asp, posChips, chipList, clist)
            for i in range(2*max):
                izquierda(aspiradora, asp, posChips, chipList, clist)
            abajo(aspiradora, asp, posChips, chipList, clist)
    elif(asp.position()==(-max, -max)):
        for j in range(max+1):
            for i in range(2*max):
                derecha(aspiradora, asp, posChips, chipList, clist)
            arriba(aspiradora, asp, posChips, chipList, clist)
            for i in range(2*max):
                izquierda(aspiradora, asp, posChips, chipList, clist)
            arriba(aspiradora, asp, posChips, chipList, clist)
    elif(asp.position()==(max, -max)):
        for j in range(max+1):
            for i in range(2*max):
                izquierda(aspiradora, asp, posChips, chipList, clist)
            arriba(aspiradora, asp, posChips, chipList, clist)
            for i in range(2*max):
                derecha(aspiradora, asp, posChips, chipList, clist)
            arriba(aspiradora, asp, posChips, chipList, clist)
'''en esta funcion se implementa los movimientos adecuados con intervalos para que describa el movimiento de una espiral tomando en cuenta su posicion inicial'''
def espiral2(aspiradora, asp, posChips, chipList, clist):
    r=1
    x=1
    for x in range (500):
        asp.forward(x/100)
        asp.left(30)
        aspiradora.posicion=(round(asp.position()[0]),round(asp.position()[1]))
        borrar(aspiradora, chipList, posChips,clist)

numChips=20
aspiradora, asp, posChips, chipList, clist= crearChips(numChips)#creacion de los elementos del mundo
t.getscreen()#aparece la pantalla
mov=1#rd.randint(1,2)#random entre 1 y dos para que escoja entre movimiento de serpiente o cuadrado
if(aspiradora.posicion==(0,0)and mov==0):#si la posicion de inicio es 0,0 entonces describe una elipse
    espiral2(aspiradora, asp, posChips, chipList, clist)
elif mov==1:#si el numero aleatorio es 1 entonces describe un cuadrado
    cuadrado(aspiradora, asp, posChips, chipList, clist)
else:#caso contrario describe una serpiente
     serpiente(aspiradora, asp, posChips, chipList, clist)   
