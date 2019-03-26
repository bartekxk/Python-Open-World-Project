import pygame, sys,os
from pygame.locals import *
from Roslina import Roslina
class WilczeJagody(Roslina):
    def __init__(self,s,x,y):
        self.s = s
        self.sila = 99
        self.inicjatywa = 0
        self.x = x
        self.y = y
        self.dlugosczycia = 0
        self.s.setField(self.x, self.y, self)
        self.obrazek = pygame.image.load(self.getGatunek() + ".bmp")
        self.obrazek=pygame.transform.scale(self.obrazek, (self.s.skalowanie,self.s.skalowanie))
    def reakcja(self,a):
        self.s.l.add("Organizm " + self.getGatunek() + " zabija " + a.getGatunek() + "(" + str(self.getX()) + ", " + str(self.getY()) + ")")
        self.s.setField(self.getX(), self.getY(), None)
        self.s.dozabicia.q.add(self)
        self.s.queue.rem(self.getX(), self.getY())
        return;
    def rozmnoz(self,x,y):
        return WilczeJagody(self.s,x,y)
    def getGatunek(self):
        return "WilczeJagody"