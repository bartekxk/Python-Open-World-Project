import pygame, sys,os
from pygame.locals import *
from Roslina import Roslina
from random import randint
class BSosnowskiego(Roslina):
    def __init__(self,s,x,y):
        self.s = s
        self.sila = 10
        self.inicjatywa = 0
        self.x = x
        self.y = y
        self.dlugosczycia = 0
        self.s.setField(self.x, self.y, self)
        self.obrazek=pygame.image.load(self.getGatunek()+".bmp")
        self.obrazek=pygame.transform.scale(self.obrazek, ( self.s.skalowanie,self.s.skalowanie))
    def reakcja(self,a):
        self.s.l.add("Organizm " + self.getGatunek() + " zabija " + a.getGatunek() + "(" + str(self.getX()) + ", " + str(self.getY()) + ")")
        self.s.setField(self.getX(), self.getY(), None)
        self.s.dozabicia.q.add(self)
    def akcja(self):
        czyrozprzestrzenic =randint(0,5)
        if czyrozprzestrzenic == 0:
            rx = randint(-1,1)
            ry = randint(-1,1)
            if self.s.CheckField(self.getX() + rx, self.getY() + ry) == True and self.s.GetField(self.getX() + rx,self.getY() + ry) == None:
                self.s.l.add("Organizm " + self.getGatunek() + " rozmnaza sie (" + str(self.getX()) + "," + str(self.getY()) + ")")
                c = self.rozmnoz(self.getX() + rx, self.getY() + ry)
                self.s.setField(self.getX() + rx, self.getY() + ry, c)
                self.s.queue.add(self.s.GetField(self.getX() + rx, self.getY() + ry))
        for i in range(-1,2):
            for j in range(-1, 2):
                if self.s.CheckField(self.getX() + i, self.getY() + j) == True and self.s.GetField(self.getX() + i,self.getY() + j) != None and self.s.GetField(self.getX() + i,self.getY() + j).getGatunek() != "Cyberowca" and self.s.GetField(self.getX() + i, self.getY() + j).getGatunek() != self.getGatunek():
                    self.s.l.add("Organizm " + self.getGatunek() + " zabija " + self.s.GetField(self.getX() + i, self.getY() + j).getGatunek() + "(" + str(self.getX()) + ", " + str(self.getY()) + ")")
                    self.s.dozabicia.q.add(self.s.GetField(self.getX() + i, self.getY() + j))
                    self.s.setField(self.getX() + i, self.getY() + j, None)
                    self.s.queue.rem(self.getX() + i, self.getY() + j)
    def rozmnoz(self,x,y):
        return BSosnowskiego(self.s,x,y)
    def getGatunek(self):
        return "BSosnowskiego"
