from Organizm import Organizm
from random import randint
class Zwierze(Organizm):
    def akcja(self):
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
            if self.getSila() < a.getSila():
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
    def reakcja(self,a):
        pass