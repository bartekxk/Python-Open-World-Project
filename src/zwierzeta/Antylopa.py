import pygame, sys,os
from pygame.locals import *
from Zwierze import Zwierze
from random import randint
class Antylopa(Zwierze):
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
    def akcja(self):
        ruchx = randint(-2, 2)
        ruchy = randint(-2, 2)
        while ruchx == 0 and ruchy == 0:
            ruchx = randint(-1, 1)
            ruchy = randint(-1, 1)
        if self.s.CheckField(self.x + ruchx, self.y + ruchy) == False:
            return
        if self.s.GetField(self.x + ruchx, self.y + ruchy) == None:
            self.s.setField(self.x + ruchx, self.y + ruchy, self)
            self.s.setField(self.x, self.y, None)
            self.x += ruchx
            self.y += ruchy
            self.s.l.add("Organizm " + self.getGatunek() + " porusza sie na pole (" + str(self.getX()) + "," + str(
                self.getY()) + ")")
        else:
            if self.s.GetField(self.x + ruchx, self.y + ruchy).getSila() > self.getSila():
                return
            self.s.l.add("Organizm " + self.getGatunek() + "kolizja z " + self.s.GetField(self.x + ruchx,
                                                                                          self.y + ruchy).getGatunek() + "(" + str(
                self.getX()) + "," + str(self.getY()) + ")")
            pom = self.s.GetField(self.x + ruchx, self.y + ruchy)
            self.kolizja(self.s.GetField(self.x + ruchx, self.y + ruchy))
            pom.reakcja(self)
    def kolizja(self,a):
        if a.getSila() < 5:
            return
        if a.getGatunek().equals(self.getGatunek()):

            czyznaleziono = False
            for i in range(-1,2):
                for j in range(-1, 2):
                    if a.getworld().CheckField(a.getX() + i, a.getY() + j) == True and a.getworld().GetField(a.getX() + i, a.getY() + j) == None:
                        czyznaleziono = True
                        c = a.rozmnoz(a.getX() + i, a.getY() + j)
                        self.s.setField(a.getX() + i, a.getY() + j, c)
                        self.s.queue.add(self.s.GetField(self.getX() + i, self.getY() + j))
                        self.s.l.add("Organizm " + self.getGatunek() + " rozmnaza sie (" + str(self.getX()) + "," + str(self.getY()) + ")")
                        return
            if czyznaleziono == False:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if self.getworld().CheckField(self.x + i, self.getY() + j) == True and self.getworld().GetField(self.getX() + i, self.getY() + j) == None:
                            czyznaleziono = True
                            c = a.rozmnoz(a.getX() + i, a.getY() + j)
                            self.s.setField(self.getX() + i, self.getY() + j, c)
                            self.s.queue.add(self.s.GetField(self.getX() + i, self.getY() + j))
                            self.s.l.add("Organizm " + self.getGatunek() + " rozmnaza sie (" + str(self.getX()) + "," + str(self.getY()) + ")")
                            return
        else:
            czywalczyc = randint(0,1)
            if czywalczyc == 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if a.getworld().CheckField(a.getX() + i, a.getY() + j) == True and a.getworld().GetField(a.getX() + i, a.getY() + j) == None:
                            self.s.setField(self.getX(), self.getY(), None)
                            self.s.setField(a.getX() + i, a.getY() + j, self)
                            self.x += i
                            self.y += j
                            return
            else:
                    if self.getSila() < a.getSila():
                        self.s.setField(self.getX(), self.getY(), None)
                        self.s.dozabicia.q.add(self)
                        self.s.queue.rem(self.getX(), self.getY())
                        self.s.l.add("Organizm " + self.getGatunek() + " zostaje zabity przez " + a.getGatunek() + " (" +str(self.getX()) + ", " + str(self.getY()) + ")")
                        return
                    else:
                        a.getworld().setField(a.getX(), a.getY(), self)
                        self.s.setField(self.getX(), self.getY(), None)
                        self.x = a.getX()
                        self.y = a.getY()
                        self.s.dozabicia.q.add(a)
                        self.s.queue.rem(a.getX(), a.getY())
                        self.s.l.add("Organizm " + self.getGatunek() + " zabija " + a.getGatunek() + "(" + str(self.getX()) + ", " + str(self.getY()) + ")")
    def rozmnoz(self,x,y):
        return Antylopa(self.s,x,y)
    def getGatunek(self):
        return "Antylopa"