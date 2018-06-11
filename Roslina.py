from Organizm import Organizm
from random import randint
class Roslina(Organizm):
    def akcja(self):
        czyrozprzestrzenic = randint(0, 4)
        if czyrozprzestrzenic == 0:
            rx = randint(-1, 1)
            ry = randint(-1, 1)
            if self.getworld().CheckField(self.getX() + rx, self.getY() + ry) == True and self.s.GetField(self.getX() + rx, self.getY() + ry) == None:
                c = self.rozmnoz(self.getX() + rx, self.getY() + ry)
                self.s.setField(self.getX() + rx, self.getY() + ry, c)
                self.s.queue.add(self.s.GetField(self.getX() + rx, self.getY() + ry))
                self.s.l.add("Organizm " + self.getGatunek() + " rozprzestrzenia sie (" + str(self.getX()) + "," + str(self.getY()) + ")")
    def kolizja(self):
        pass
    def reakcja(self,a):
        pass

