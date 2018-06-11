class Kolejka:
    def __init__(self):
        self.lista=list()
    def add(self,c):
        self.lista.append(c)
        if len(self.lista)==1:
            return
        for i in range(self.length()-2,-1,-1):
            if self.lista[i].getIni()<c.getIni():
                pomocnicza=self.lista[i+1]
                self.lista[i+1]=self.lista[i]
                self.lista[i]=pomocnicza
            else:
                break
    def at(self,index):
        return self.lista[index]
    def erase(self,index):
        del self.lista[index]
    def length(self):
        return len(self.lista)
    def rem(self,x,y):
        for i in self.lista:
            if i.getX()==x and i.getY()==y:
                org=i
                self.lista.remove(org)
                return
