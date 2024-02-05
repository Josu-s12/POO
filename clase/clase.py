class Perro:#clase
    def __init__(self,raza,nombre,color):#metodo
        self.raza = raza
        self.nombre=nombre
        self.color=color
        
    def getNombre(self):#atributos
            return self.nombre
    def ladrar(self):
            print(f"{self.nombre} esta ladrando!")
    def caminar(self):
            print(f"{self.nombre} esta caminando")
    def getRaza(self):
          print(f"{self.nombre}"f" es {self.raza}")
        
#objeto  #clase  
perro1 =  Perro("border collie","emma","negro con blanco")
print(perro1.getNombre())
perro1.ladrar()
perro1.caminar()
perro1.getRaza()