import pygame, sys,os
from tkinter import *
from tkinter import filedialog
from random import randint
import random
from pygame.locals import *
from Organizm import Organizm
from Zwierze import Zwierze
from Roslina import Roslina
from Swiat import Swiat
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
random.seed(random.SystemRandom().random())
n=20
m=20
org=3
pygame.init()
window = pygame.display.set_mode((500, 300))
window=pygame.display.set_caption("Bartłomiej Kocot indeks 171557")
czyoknojestotwarte=True
czygratrwa=False
plikdowczytania="load.txt"
tlomenu=pygame.image.load("menu.png")
screen=pygame.display.get_surface()
screen.blit(tlomenu,(0,0))
font = pygame.font.SysFont("arial", 15)
ntext=font.render(str(n),1,(0,0,0))
mtext=font.render(str(m),1,(0,0,0))
orgtext=font.render(str(org),1,(0,0,0))
screen.blit(ntext,(66,66))
screen.blit(mtext,(128,66))
screen.blit(orgtext,(42,156))
pygame.display.flip()
zmienionowartosc=False
while czyoknojestotwarte==True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            czyoknojestotwarte=False
            break
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(event)
            if pos[0]>324 and pos[0]<473 and pos[1]>136 and pos[1]<183:
                Tk().withdraw()
                sciezkadozapisu = filedialog.askopenfile()
                plikdowczytania = sciezkadozapisu
            if pos[0] > 323 and pos[0] < 468 and pos[1] > 64 and pos[1] < 107:
                czygratrwa=True
                pygame.display.quit
                pygame.init()
                window = pygame.display.set_mode((800, 600))
                window = pygame.display.set_caption("Bartłomiej Kocot indeks 171557")
                screen = pygame.display.get_surface()
                pygame.display.flip()
                s=Swiat(20,20,screen)
                s.plikdozapisu=plikdowczytania
                s.load()
                s.plikdozapisu="save.txt"
                s.rysujSwiat()
                pygame.display.update()
                while czygratrwa:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            czygratrwa = False
                            break
                        if event.type == pygame.MOUSEBUTTONUP:
                            pos = pygame.mouse.get_pos()
                            if pos[0] < 544 and pos[0] > 447 and pos[1] > 305 and pos[1] < 360:
                                s.save()
                            if pos[0] < 559 and pos[0] > 440 and pos[1] > 222 and pos[1] < 276:
                                Tk().withdraw()
                                sciezkadozapisu = filedialog.asksaveasfilename()
                                s.plikdozapisu = sciezkadozapisu
                            if pos[0] < 561 and pos[0] > 443 and pos[1] > 431 and pos[1] < 476:
                                s.wykonajTure()
                                s.rysujSwiat()
                                pygame.display.update()
                                s.l.log()
                            if pos[0] > 656 and pos[0] < 770:
                                if pos[1] > 68 and pos[1] < 84:
                                    s.zmienaktualnygatunek("Antylopa")
                                if pos[1] > 87 and pos[1] < 104:
                                    s.zmienaktualnygatunek("Lis")
                                if pos[1] > 110 and pos[1] < 125:
                                    s.zmienaktualnygatunek("Owca")
                                if pos[1] > 128 and pos[1] < 143:
                                    s.zmienaktualnygatunek("Wilk")
                                if pos[1] > 151 and pos[1] < 164:
                                    s.zmienaktualnygatunek("Zolw")
                                if pos[1] > 170 and pos[1] < 185:
                                    s.zmienaktualnygatunek("BSosnowskiego")
                                if pos[1] > 186 and pos[1] < 203:
                                    s.zmienaktualnygatunek("Guarana")
                                if pos[1] > 205 and pos[1] < 221:
                                    s.zmienaktualnygatunek("Mlecz")
                                if pos[1] > 226 and pos[1] < 241:
                                    s.zmienaktualnygatunek("Trawa")
                                if pos[1] > 247 and pos[1] < 263:
                                    s.zmienaktualnygatunek("WilczeJagody")
                                if pos[1] > 264 and pos[1] < 279:
                                    s.zmienaktualnygatunek("Cyber-owca")
                            if pos[0] > 5 and pos[1] > 5 and pos[0] < 400 and pos[1] < 400:
                                if s.GetField(int((pos[0] - 5) / s.skalowanie),
                                              int((pos[1] - 5) / s.skalowanie)) == None:
                                    if s.aktualnygatunek == "Antylopa":
                                        dododania = Antylopa(s, int(pos[1] / s.skalowanie), int(pos[0] / s.skalowanie))
                                    if s.aktualnygatunek == "Lis":
                                        dododania = Lis(s, int(pos[1] / s.skalowanie), int(pos[0] / s.skalowanie))
                                    if s.aktualnygatunek == "Owca":
                                        dododania = Owca(s, int(pos[1] / s.skalowanie), int(pos[0] / s.skalowanie))
                                    if s.aktualnygatunek == "Wilk":
                                        dododania = Wilk(s, int(pos[1] / s.skalowanie), int(pos[0] / s.skalowanie))
                                    if s.aktualnygatunek == "Zolw":
                                        dododania = Zolw(s, int(pos[1] / s.skalowanie), int(pos[0] / s.skalowanie))
                                    if s.aktualnygatunek == "BSosnowskiego":
                                        dododania = BSosnowskiego(s, int(pos[1] / s.skalowanie),
                                                                  int(pos[0] / s.skalowanie))
                                    if s.aktualnygatunek == "Guarana":
                                        dododania = Guarana(s, int(pos[1] / s.skalowanie), int(pos[0] / s.skalowanie))
                                    if s.aktualnygatunek == "Mlecz":
                                        dododania = Mlecz(s, int(pos[1] / s.skalowanie), int(pos[0] / s.skalowanie))
                                    if s.aktualnygatunek == "Trawa":
                                        dododania = Trawa(s, int(pos[1] / s.skalowanie), int(pos[0] / s.skalowanie))
                                    if s.aktualnygatunek == "WilczeJagody":
                                        dododania = WilczeJagody(s, int(pos[1] / s.skalowanie),
                                                                 int(pos[0] / s.skalowanie))
                                    # if s.aktualnygatunek=="Cyber-owca":
                                    #    dododania=Cyber-owca(s,int(pos[1]/s.skalowanie),int(pos[0]/s.skalowanie))
                                    s.queue.add(dododania)
                                    s.rysujSwiat()
                                    pygame.display.update()
                pygame.display.quit
                pygame.init()
                window = pygame.display.set_mode((500, 300))
                window = pygame.display.set_caption("Bartłomiej Kocot indeks 171557")
                screen = pygame.display.get_surface()
                pygame.display.flip()
                zmienionowartosc = True
            if pos[0] > 33 and pos[0] < 140 and pos[1] > 204 and pos[1] < 250:
                czygratrwa=True
                pygame.display.quit
                pygame.init()
                window = pygame.display.set_mode((800, 600))
                window = pygame.display.set_caption("Bartłomiej Kocot indeks 171557")
                screen = pygame.display.get_surface()
                pygame.display.flip()
                s = Swiat(n, m,screen)
                for i in range(0,org):
                    x = randint(0,n-1)
                    y = randint(0,m-1)
                    if s.GetField(x, y) == None:
                        o =  BSosnowskiego(s, x, y)
                        s.queue.add(o)
                    x = randint(0,n-1)
                    y = randint(0,m-1)
                    if s.GetField(x, y) == None:
                        o =  Guarana(s, x, y)
                        s.queue.add(o)
                    x = randint(0,n-1)
                    y = randint(0,m-1)
                    if s.GetField(x, y) == None:
                        o =  Mlecz(s, x, y)
                        s.queue.add(o)
                    x = randint(0,n-1)
                    y = randint(0,m-1)
                    if s.GetField(x, y) == None:
                        o =  Trawa(s, x, y)
                        s.queue.add(o)
                    x = randint(0,n-1)
                    y = randint(0,m-1)
                    if s.GetField(x, y) == None:
                        o =  WilczeJagody(s, x, y)
                        s.queue.add(o)
                    x = randint(0,n-1)
                    y = randint(0,m-1)
                    if s.GetField(x, y) == None:
                        o =  Antylopa(s, x, y)
                        s.queue.add(o)
                    x = randint(0,n-1)
                    y = randint(0,m-1)
                    if s.GetField(x, y) == None:
                        o =  Lis(s, x, y)
                        s.queue.add(o)
                    x = randint(0,n-1)
                    y = randint(0,m-1)
                    if s.GetField(x, y) == None:
                        o =  Owca(s, x, y)
                        s.queue.add(o)
                    x = randint(0,n-1)
                    y = randint(0,m-1)
                    if s.GetField(x, y) == None:
                        o =  Wilk(s, x, y)
                        s.queue.add(o)
                    x = randint(0,n-1)
                    y = randint(0,m-1)
                    if s.GetField(x, y) == None:
                        o =  Zolw(s, x, y)
                        s.queue.add(o)
                    x = randint(0, n - 1)
                    y = randint(0, m - 1)
                    if s.GetField(x, y) == None:
                        o =  Cyberowca(s, x, y)
                        s.queue.add(o)
                while s.GetField(x,y)==None:
                    x = randint(0, n - 1)
                    y = randint(0, m - 1)
                o=Czlowiek(s,x,y)
                s.queue.add(o)
                s.rysujSwiat()
                pygame.display.update()
                while czygratrwa:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            czygratrwa=False
                            break
                        if event.type == pygame.MOUSEBUTTONUP:
                            pos = pygame.mouse.get_pos()
                            if pos[0]<544 and pos[0]>447 and pos[1]>305 and pos[1]<360:
                                s.save()
                            if pos[0] < 559 and pos[0] > 440 and pos[1] > 222 and pos[1] < 276:
                                Tk().withdraw()
                                sciezkadozapisu = filedialog.asksaveasfilename()
                                s.plikdozapisu=sciezkadozapisu
                            if pos[0]<561 and pos[0]>443 and pos[1]>431 and pos[1]<476:
                                s.wykonajTure()
                                s.rysujSwiat()
                                pygame.display.update()
                                s.l.log()
                            if pos[0]>656 and pos[0]<770:
                                if pos[1]>68 and pos[1]<84:
                                    s.zmienaktualnygatunek("Antylopa")
                                if pos[1]>87 and pos[1]<104:
                                    s.zmienaktualnygatunek("Lis")
                                if pos[1]>110 and pos[1]<125:
                                    s.zmienaktualnygatunek("Owca")
                                if pos[1]>128 and pos[1]<143:
                                    s.zmienaktualnygatunek("Wilk")
                                if pos[1]>151 and pos[1]<164:
                                    s.zmienaktualnygatunek("Zolw")
                                if pos[1]>170 and pos[1]<185:
                                    s.zmienaktualnygatunek("BSosnowskiego")
                                if pos[1]>186 and pos[1]<203:
                                    s.zmienaktualnygatunek("Guarana")
                                if pos[1]>205 and pos[1]<221:
                                    s.zmienaktualnygatunek("Mlecz")
                                if pos[1]>226 and pos[1]<241:
                                    s.zmienaktualnygatunek("Trawa")
                                if pos[1]>247 and pos[1]<263:
                                    s.zmienaktualnygatunek("WilczeJagody")
                                if pos[1]>264 and pos[1]<279:
                                    s.zmienaktualnygatunek("Cyberowca")
                            if pos[0]>5 and pos[1]>5 and pos[0]<400 and pos[1]<400:
                                if s.GetField(int((pos[0]-5)/s.skalowanie),int((pos[1]-5)/s.skalowanie))==None:
                                    if s.aktualnygatunek=="Antylopa":
                                        dododania=Antylopa(s,int(pos[1]/s.skalowanie),int(pos[0]/s.skalowanie))
                                    if s.aktualnygatunek=="Lis":
                                        dododania=Lis(s,int(pos[1]/s.skalowanie),int(pos[0]/s.skalowanie))
                                    if s.aktualnygatunek=="Owca":
                                        dododania=Owca(s,int(pos[1]/s.skalowanie),int(pos[0]/s.skalowanie))
                                    if s.aktualnygatunek=="Wilk":
                                        dododania=Wilk(s,int(pos[1]/s.skalowanie),int(pos[0]/s.skalowanie))
                                    if s.aktualnygatunek=="Zolw":
                                        dododania=Zolw(s,int(pos[1]/s.skalowanie),int(pos[0]/s.skalowanie))
                                    if s.aktualnygatunek=="BSosnowskiego":
                                        dododania=BSosnowskiego(s,int(pos[1]/s.skalowanie),int(pos[0]/s.skalowanie))
                                    if s.aktualnygatunek=="Guarana":
                                        dododania=Guarana(s,int(pos[1]/s.skalowanie),int(pos[0]/s.skalowanie))
                                    if s.aktualnygatunek=="Mlecz":
                                        dododania=Mlecz(s,int(pos[1]/s.skalowanie),int(pos[0]/s.skalowanie))
                                    if s.aktualnygatunek=="Trawa":
                                        dododania=Trawa(s,int(pos[1]/s.skalowanie),int(pos[0]/s.skalowanie))
                                    if s.aktualnygatunek=="WilczeJagody":
                                        dododania=WilczeJagody(s,int(pos[1]/s.skalowanie),int(pos[0]/s.skalowanie))
                                   # if s.aktualnygatunek=="Cyberowca":
                                    #    dododania=Cyberowca(s,int(pos[1]/s.skalowanie),int(pos[0]/s.skalowanie))
                                    s.queue.add(dododania)
                                    s.rysujSwiat()
                                    pygame.display.update()
                pygame.display.quit
                pygame.init()
                window = pygame.display.set_mode((500, 300))
                window = pygame.display.set_caption("Bartłomiej Kocot indeks 171557")
                screen = pygame.display.get_surface()
                pygame.display.flip()
                zmienionowartosc=True
            if pos[0]>62 and pos[0]<82 and pos[1]>44 and pos[1]<60:
                n+=1
                ntext = font.render(str(n), 1, (0, 0, 0))
                zmienionowartosc=True
            if pos[0] > 65 and pos[0] < 85 and pos[1] > 92 and pos[1] < 106 and n>1:
                n -= 1
                ntext = font.render(str(n), 1, (0, 0, 0))
                zmienionowartosc = True
            if pos[0]>124 and pos[0]<146 and pos[1]>44 and pos[1]<60:
                m+=1
                mtext = font.render(str(m), 1, (0, 0, 0))
                zmienionowartosc=True
            if pos[0] > 127 and pos[0] < 145 and pos[1] > 92 and pos[1] < 106 and m>1:
                m -= 1
                mtext = font.render(str(m), 1, (0, 0, 0))
                zmienionowartosc = True
            if pos[0]>35 and pos[0]<52 and pos[1]>135 and pos[1]<150:
                org+=1
                orgtext = font.render(str(org), 1, (0, 0, 0))
                zmienionowartosc=True
            if pos[0] > 34 and pos[0] < 53 and pos[1] > 180 and pos[1] < 193 and org>1:
                org-=1
                orgtext = font.render(str(org), 1, (0, 0, 0))
                zmienionowartosc = True
            if zmienionowartosc==True:
                screen.blit(tlomenu, (0, 0))
                screen.blit(ntext, (66, 66))
                screen.blit(mtext, (128, 66))
                screen.blit(orgtext, (42, 156))
                screen.blit(ntext, (66, 66))
                pygame.display.update()
                zmienionowartosc=False
