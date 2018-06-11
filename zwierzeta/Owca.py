import pygame, sys,os
from pygame.locals import *
from Zwierze import Zwierze
class Owca(Zwierze):
    def __init__(self,s,x,y):
        self.s = s
        self.sila = 4
        self.inicjatywa = 4
        self.x = x
        self.y = y
        self.dlugosczycia = 0
        self.s.setField(self.x, self.y, self)
        self.obrazek = pygame.image.load(self.getGatunek() + ".bmp")
        self.obrazek=pygame.transform.scale(self.obrazek, (self.s.skalowanie,self.s.skalowanie))
    def rozmnoz(self,x,y):
        return Owca(self.s,x,y)
    def getGatunek(self):
        return "Owca"