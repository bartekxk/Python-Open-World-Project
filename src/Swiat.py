from Kolejka import Kolejka
from Zabij import Zabij
from Logs import Logs
from Organizm import Organizm
import pygame, sys,os
from pygame.locals import *
from src.rosliny.BSosnowskiego import BSosnowskiego
from src.rosliny.Guarana import Guarana
from src.rosliny.Mlecz import Mlecz
from src.rosliny.Trawa import Trawa
from src.rosliny.WilczeJagody import WilczeJagody
from src.zwierzeta.Antylopa import Antylopa
from src.zwierzeta.Lis import Lis
from src.zwierzeta.Owca import Owca
from src.zwierzeta.Wilk import Wilk
from src.zwierzeta.Zolw import Zolw
from src.zwierzeta.Czlowiek import Czlowiek
from src.zwierzeta.Cyberowca import Cyberowca
class Swiat:
    def __init__(self,n,m,sc):
        self.N=n
        self.tura=0
        self.M=m
        self.l=Logs(self)
        self.queue=Kolejka()
        self.aktualnygatunek="Antylopa"
        self.aktualnyobrazek=pygame.image.load(self.aktualnygatunek+".bmp")
        self.plikdozapisu="save.txt"
        self.dozabicia=Zabij()
        self.plansza=[[None for i in range(self.M)] for j in range(self.N)]
        self.ekran=sc
        self.tlo = pygame.image.load("panelgry.png")
        self.pustepole=pygame.image.load("pusty.bmp")
        if n>=m:
            self.skalowanie=int(400/n)
        else:
            self.skalowanie=int(400/m)
    def zmienaktualnygatunek(self,str):
        self.aktualnygatunek=str
        self.aktualnyobrazek=pygame.image.load(self.aktualnygatunek+".bmp")
        self.rysujSwiat()
        pygame.display.update()
    def setField(self,x,y,c):
        self.plansza[x][y]=c
    def GetField(self,x,y):
        return self.plansza[x][y]
    def getN(self):
        return self.N
    def getM(self):
        return self.M
    def CheckField(self,x,y):
        if x<self.N and x>=0 and y<self.M and y>=0:
            return True
        return False
    def wykonajTure(self):
        i=0
        while i<self.queue.length():
            if self.queue.at(i).getGatunek()=="Czlowiek":
                self.dozabicia.kill()
                self.rysujSwiat()
                pygame.display.update()
                self.l.clear()
                self.l.add("Ruch czlowieka!")
                self.l.log()
            self.queue.at(i).akcja()
            i+=1
        self.dozabicia.kill()
    def rysujSwiat(self):
        self.ekran.blit(self.tlo, (0, 0))
        self.ekran.blit(self.aktualnyobrazek,(770,42) )
        x=5
        y=5
        for i in range(0,self.N):
            for j in range(0,self.M):
                if self.GetField(i,j)!=None:
                    self.ekran.blit(self.GetField(i,j).rysujorganizm(), (x, y))
                else:
                    self.ekran.blit(self.pustepole, (x, y))
                x+=self.skalowanie
            x=5
            y+=self.skalowanie
    def save(self):
        file = open(self.plikdozapisu, "w")
        file.write(str(self.N))
        file.write("\n")
        file.write(str(self.M))
        file.write("\n")
        file.write(str(self.queue.length()))
        file.write("\n")
        for i in range (0,self.queue.length()):
            file.write(self.queue.at(i).getGatunek())
            file.write("\n")
            if self.queue.at(i).getGatunek()=="Czlowiek":
                file.write(str(self.queue.at(i).czasumiejetnosci))
                file.write("\n")
            file.write(str(self.queue.at(i).getX()))
            file.write("\n")
            file.write(str(self.queue.at(i).getY()))
            file.write("\n")
            file.write(str(self.queue.at(i).getSila()))
            file.write("\n")
            file.write(str(self.queue.at(i).getIni()))
            file.write("\n")
            file.write(str(self.queue.at(i).getDZ()))
            file.write("\n")
        file.close()
        self.l.clear()
        self.l.add("Pomyślnie zapisano w "+self.plikdozapisu)
        self.rysujSwiat()
        self.l.log()

    def load(self):
        self.plikdozapisu = str(self.plikdozapisu)
        self.plikdozapisu = self.plikdozapisu[25:]
        index = self.plikdozapisu.index("'")
        self.plikdozapisu = self.plikdozapisu[0:index]
        file = open(self.plikdozapisu, "r")
        self.N = int(file.readline())
        self.M = int(file.readline())
        if self.N >= self.M:
            self.skalowanie = int(400 / self.N)
        else:
            self.skalowanie = int(400 / self.M)
        i = int(file.readline())
        for k in range(0, i):
            gatunek = str(file.readline())
            gatunek = gatunek[:len(gatunek) - 1]
            if gatunek == "Czlowiek":
                ablity = int(file.readline())
            x = int(file.readline())
            y = int(file.readline())
            sila = int(file.readline())
            inicjatywa = int(file.readline())
            dlugosczycia = int(file.readline())
            if gatunek == "Czlowiek":
                pom = Czlowiek(self, x, y)
                pom.czasumiejetnosci = ablity
            if gatunek == "BSosnowskiego":
                pom = BSosnowskiego(self, x, y)
            if gatunek == "Guarana":
                pom = Guarana(self, x, y)
            if gatunek == "Mlecz":
                pom = Mlecz(self, x, y)
            if gatunek == "Trawa":
                pom = Trawa(self, x, y)
            if gatunek == "WilczeJagody":
                pom = WilczeJagody(self, x, y)
            if gatunek == "Antylopa":
                pom = Antylopa(self, x, y)
            if gatunek == "Lis":
                pom = Lis(self, x, y)
            if gatunek == "Owca":
                pom = Owca(self, x, y)
            if gatunek == "Wilk":
                pom = Wilk(self, x, y)
            if gatunek == "Zolw":
                pom = Zolw(self, x, y)
            if gatunek == "Cyberowca":
                pom = Cyberowca(self, x, y)
            pom.setSila(sila)
            pom.setIni(inicjatywa)
            pom.setDZ(dlugosczycia)
            self.queue.add(pom)
        self.l.add("Poprawnie zaladowano")
        self.l.log()