from abc import ABC, abstractmethod
class Organizm(ABC):
    @abstractmethod
    def kolizja(self,a):
        pass

    @abstractmethod
    def reakcja(self,a):
        pass

    @abstractmethod
    def getGatunek(self):
        pass

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def rozmnoz(self,x,y):
        pass

    def getDZ(self):
       return self.dlugosczycia

    def setSila(self,s):
        self.sila=s

    def setIni(self,ini):
        self.inicjatywa=ini

    def setDZ(self,dz):
        self.dlugosczycia=dz
    def grow(self):
        self.dlugosczycia+=1
    def getSila(self):
        return self.sila
    def getIni(self):
        return self.inicjatywa
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getworld(self):
        return self.s
    def rysujorganizm(self):
        return self.obrazek