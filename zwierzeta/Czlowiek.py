import pygame, sys,os
from pygame.locals import *
from Zwierze import Zwierze
from random import randint
class Czlowiek(Zwierze):
    def __init__(self,s,x,y):
        self.czasumiejetnosci = 0
        self.s = s
        self.sila = 5
        self.inicjatywa = 4
        self.x = x
        self.y = y
        self.dlugosczycia = 0
        self.s.setField(self.x, self.y, self)
        self.obrazek = pygame.image.load(self.getGatunek() + ".bmp")
        self.obrazek=pygame.transform.scale(self.obrazek, (self.s.skalowanie,self.s.skalowanie))
    def akcja(self):
        ruchx = 0
        ruchy = 0
        #ruch
        czyklawisznacisniety=False
        while czyklawisznacisniety==False:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    ruch=event.key
                    czyklawisznacisniety=True
                    break
        if ruch ==120:
            self.ablity()
            self.akcja()
            return
        if ruch == 276:
            ruchy = -1
        if ruch == 275:
            ruchy = 1
        if ruch == 273:
            ruchx = -1
        if ruch == 274:
            ruchx = 1
        if ruchy==0 and ruchx==0:
            self.akcja()
            return
        if self.s.CheckField(self.x + ruchx, self.y + ruchy) == False:
            self.akcja()
            return
        if self.czasumiejetnosci > 2:
            ruchx *= 2
            ruchy *= 2
        if self.czasumiejetnosci == 1 or self.czasumiejetnosci == 2:
            losuj = randint(0,1)
            if losuj == 1:
                ruchx *= 2
                ruchy *= 2
        if self.s.GetField(self.x + ruchx, self.y + ruchy) == None:
            self.s.setField(self.x + ruchx, self.y + ruchy, self)
            self.s.setField(self.x, self.y, None)
            self.x +=ruchx
            self.y +=ruchy
            self.s.l.add("Organizm " + self.getGatunek() + " porusza sie na pole (" + str(self.getX()) + "," + str(self.getY()) + ")")
        else:
             pom = self.s.GetField(self.x + ruchx, self.y + ruchy)
             self.s.l.add("Organizm " + self.getGatunek() + "kolizja z " + self.s.GetField(self.x + ruchx,self.y + ruchy).getGatunek() + "(" + str(self.getX()) + "," + str(self.getY()) + ")")
             self.kolizja(self.s.GetField(self.x + ruchx, self.y + ruchy))
             pom.reakcja(self)
        if self.czasumiejetnosci == 1:
            self.czasumiejetnosci = -5
            return
        if self.czasumiejetnosci < 0:
            self.czasumiejetnosci+=1
            return
        if self.czasumiejetnosci > 0:
            self.czasumiejetnosci-=1
            return
    def ablity(self):
        if self.czasumiejetnosci != 0:
            self.s.l.add( "Umiejętność zostala juz aktywowana")
            self.s.rysujSwiat()
            self.s.l.log()
            pygame.display.update()
            return
        self.czasumiejetnosci = 5
        self.s.l.add("Umiejetnosc zostala aktywowana")
        self.s.rysujSwiat()
        self.s.l.log()
        pygame.display.update()
    def rozmnoz(self,x,y):
        return None
    def getGatunek(self):
        return "Czlowiek"