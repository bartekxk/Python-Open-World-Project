import pygame, sys,os
from pygame.locals import *
from Zwierze import Zwierze
from random import randint
class Zolw(Zwierze):
    def __init__(self,s,x,y):
        self.s = s
        self.sila = 2
        self.inicjatywa = 1
        self.x = x
        self.y = y
        self.dlugosczycia = 0
        self.s.setField(self.x, self.y, self)
        self.obrazek = pygame.image.load(self.getGatunek() + ".bmp")
        self.obrazek=pygame.transform.scale(self.obrazek, (self.s.skalowanie,self.s.skalowanie))
    def akcja(self):
        czywykonacruch = randint(0,3)
        if czywykonacruch == 0:
            return
        ruchx = randint(-1, 1)
        ruchy = randint(-1, 1)
        while ruchx == 0 and ruchy == 0:
            ruchx = randint(-1,1)
            ruchy = randint(-1,1)
        if self.s.CheckField(self.x + ruchx, self.y + ruchy) == False:
            return
        if self.s.GetField(self.x + ruchx, self.y + ruchy) == None:
            self.s.setField(self.x + ruchx, self.y + ruchy, self)
            self.s.setField(self.x, self.y, None)
            self.x += + ruchx
            self.y += ruchy
            self.s.l.add("Organizm " + self.getGatunek() + " porusza sie na pole (" + str(self.getX()) + "," + str(self.getY()) + ")")
        else:
            self.s.l.add("Organizm " + self.getGatunek() + "kolizja z " + self.s.GetField(self.x + ruchx,self.y + ruchy).getGatunek() + "(" + str(self.getX()) + "," + str(self.getY()) + ")")
            pom = self.s.GetField(self.x + ruchx, self.y + ruchy)
            self.kolizja(self.s.GetField(self.x + ruchx, self.y + ruchy))
            pom.reakcja(self)
    def rozmnoz(self,x,y):
        return Zolw(self.s,x,y)
    def getGatunek(self):
        return "Zolw"