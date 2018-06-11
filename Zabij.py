from Kolejka import Kolejka
import gc
class Zabij:
    def __init__(self):
        self.q=Kolejka()
    def kill(self):
        while self.q.length()>0:
            self.q.erase(0)
        gc.collect()