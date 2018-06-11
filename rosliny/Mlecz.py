import pygame, sys,os
from pygame.locals import *
from Roslina import Roslina
from random import randint
class Mlecz(Roslina):
    def __init__(self,s,x,y):
        self.s = s
        self.sila = 0
        self.inicjatywa = 0
        self.x = x
        self.y = y
        self.dlugosczycia = 0
        self.s.setField(self.x, self.y, self)
        self.obrazek = pygame.image.load(self.getGatunek() + ".bmp")
        self.obrazek=pygame.transform.scale(self.obrazek, (self.s.skalowanie,self.s.skalowanie))
    def akcja(self):
        for i in range(0,3):
            czyrozprzestrenic = randint(0,6)
            if czyrozprzestrenic == 3:
                rx = randint(-1,1)
                ry = randint(-1,1)
                if self.s.CheckField(self.getX() + rx, self.getY() + ry) == True and self.s.GetField(self.getX() + rx, self.getY() + ry) == None:
                    c = self.rozmnoz(self.getX() + rx, self.getY() + ry)
                    self.s.setField(self.getX() + rx, self.getY() + ry, c)
                    self.s.queue.add(self.s.GetField(self.getX() + rx, self.getY() + ry))
                    self.s.l.add("Organizm " + self.getGatunek() + " rozmnaza sie (" + str(self.getX()) + "," + str(self.getY()) + ")")
    def rozmnoz(self,x,y):
        return Mlecz(self.s,x,y)
    def getGatunek(self):
        return "Mlecz"
