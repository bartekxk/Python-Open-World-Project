import pygame, sys,os
from pygame.locals import *
class Logs:
    def __init__(self,s):
        self.logi=""
        self.swiat=s
        file=open("logi.txt","w")
        file.close()
        self.font = pygame.font.SysFont("arial", 15)
        self.dologow = self.font.render(self.logi, 1, (0, 0, 0))
    def clear(self):
        self.logi=""
    def add(self,x):
        self.logi+=x
        self.logi+="\n"
    def log(self):
        file=open("logi.txt","a")
        file.write(self.logi)
        file.close()
        naekran=self.logi
        if len(naekran)>100:
            naekran=naekran[0:99]
            naekran+="... Wiecej w pliku logi.txt"
        self.dologow = self.font.render(naekran, 1, (0, 0, 0))
        self.swiat.ekran.blit(self.dologow,(8,580) )
        pygame.display.update()
        self.clear()