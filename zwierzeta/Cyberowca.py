import pygame, sys,os
from pygame.locals import *
from Zwierze import Zwierze
from random import randint
from math import sqrt
class Cyberowca(Zwierze):
    def __init__(self,s,x,y):
        self.s = s
        self.sila = 11
        self.inicjatywa = 4
        self.x = x
        self.y = y
        self.dlugosczycia = 0
        self.s.setField(self.x, self.y, self)
        self.obrazek = pygame.image.load(self.getGatunek() + ".bmp")
        self.obrazek=pygame.transform.scale(self.obrazek, (self.s.skalowanie,self.s.skalowanie))
    def akcja(self):
        ruchx=0
        ruchy=0
        listabarszu=list()
        for i in range(0,self.s.getN()):
            for j in range(0,self.s.getM()):
                if self.s.GetField(i,j)!=None and self.s.GetField(i,j).getGatunek()=="BSosnowskiego":
                    listabarszu.append(self.s.GetField(i,j))
        elementmin=None
        minodleglosc=self.s.getN()*self.s.getM()
        for org in listabarszu:
            odleglosc=sqrt(int((org.getX()-self.x)*(org.getX()-self.x))+(org.getY()-self.y)*(org.getY()-self.y))
            if odleglosc<minodleglosc:
                elementmin=org
                minodleglosc=odleglosc
        if len(listabarszu)>0:
            if elementmin.getX() > self.x:
                ruchx = 1
            if elementmin.getX() < self.x:
                ruchx= -1
            if elementmin.getY() > self.y:
                ruchy= 1
            if elementmin.getY() < self.y:
                ruchy= -1
        else:
            ruchx = randint(-1,1)
            ruchy = randint(-1,1)
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
            self.s.l.add("Organizm " + self.getGatunek() + " porusza sie na pole (" + str(self.getX()) + "," + str(self.getY()) + ")")
        else:
            pom = self.s.GetField(self.x + ruchx, self.y + ruchy)
            self.s.l.add("Organizm " + self.getGatunek() + "kolizja z " + self.s.GetField(self.x + ruchx,self.y + ruchy).getGatunek() + "(" + str(self.getX()) + "," + str(self.getY()) + ")")
            self.kolizja(self.s.GetField(self.x + ruchx, self.y + ruchy))
            pom.reakcja(self)

    def kolizja(self,a):
        if a.getGatunek() == self.getGatunek():
            czyznaleziono = False
            for i in range(-1,2):
                for j in range(-1, 2):
                        if a.getworld().CheckField(a.getX()+i, a.getY()+j) == True and a.getworld().GetField(a.getX()+i, a.getY()+j) == None:
                            czyznaleziono=True
                            c=a.rozmnoz(a.getX()+i, a.getY()+j)
                            self.getworld().setField(a.getX()+i, a.getY()+j, c)
                            self.s.queue.add(self.s.GetField(a.getX()+i, a.getY()+j))
                            self.s.l.add("Organizm " + self.getGatunek() + " rozmnaza sie (" + str(self.getX()) + "," + str(self.getY()) + ")")
                            return
            if czyznaleziono == False:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if self.getworld().CheckField(self.x + i, self.getY() + j) == True and self.getworld().GetField(self.getX() + i, self.getY() + j) == None:
                            czyznaleziono = True
                            c = a.rozmnoz(a.getX() + i, a.getY() + j)
                            self.s.setField(self.getX() + i, self.getY() + j, c)
                            self.s.queue.add(self.s.GetField(a.getX() + i, a.getY() + j))
                            self.s.l.add("Organizm " + self.getGatunek() + " rozmnaza sie (" + str(self.getX()) + "," + str(self.getY()) + ")")
                            return
        else:
            if self.getSila() < a.getSila() and a.getGatunek()!="BSosnowskiego":
                self.s.queue.rem(self.getX(), self.getY())
                self.s.setField(self.getX(), self.getY(), None)
                self.s.dozabicia.q.add(self)
                self.s.l.add("Organizm " + self.getGatunek() + " zostaje zabity przez " + a.getGatunek() + " (" + str(self.getX()) + ", " + str(self.getY()) + ")")
                return
            else:
                self.s.queue.rem(a.getX(), a.getY())
                a.s.setField(a.getX(), a.getY(), self)
                self.s.setField(self.getX(), self.getY(), None)
                self.x = a.getX()
                self.y = a.getY()
                self.s.dozabicia.q.add(a)
                self.s.l.add("Organizm " + self.getGatunek() + " zabija " + a.getGatunek() + "(" + str(self.getX()) + ", " + str(self.getY()) + ")")
    def rozmnoz(self,x,y):
        return Cyberowca(self.s,x,y)
    def getGatunek(self):
        return "Cyberowca"