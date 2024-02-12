class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}.")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños! Ahora tengo {self.edad} años.")

    def cambiar_ciudad(self, nueva_ciudad):
        self.ciudad = nueva_ciudad
        print(f"Me he mudado a {self.ciudad}.")

# uso
persona1 = Persona("Josue", 20, "bogota")
persona1.presentarse() 
persona1.cumplir_anios()  
persona1.cambiar_ciudad("medellin")  
persona1.presentarse() 

