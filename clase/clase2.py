class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.paginas}")

    def leer_pagina(self, num_pagina):
        if num_pagina <= self.paginas:
            print(f"Estás leyendo la página {num_pagina} de {self.titulo}.")
        else:
            print("Esa página no existe en el libro.")

    def cambiar_autor(self, nuevo_autor):
        self.autor = nuevo_autor
        print(f"El autor de {self.titulo} ha sido cambiado a {nuevo_autor}.")

# uso
libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 96)
libro1.mostrar_informacion()
libro1.leer_pagina(10)
libro1.cambiar_autor("Julio Cortázar")
libro1.mostrar_informacion()
