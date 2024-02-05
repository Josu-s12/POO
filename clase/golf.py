class Golf:
    def __init__(self,distancia,driver,pitching,putter):
        self.distancia=distancia
        self.driver=driver
        self.pitching=pitching
        self.putter=putter

    def Hdistancia(self):
        return self.distancia
    def Usedriver(self):
            print(f"{self.distancia} que es mas de 300yd es recomendado usar el {self.driver}")
    def Usepitching(self):
            print(f"{self.distancia} que es menos de 100yd es recomendado usa el {self.pitching}")
    def Useputter(self):
            print(f"{self.distancia} ya estas en green usa el {self.putter}")

club = Golf("De acuerdo a la distancia","Driver","Pitching","Putter")
club.Usedriver()
club.Usepitching()
club.Useputter()
