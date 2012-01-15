import pilas
import random

class EfectoGolpe(pilas.actores.Animacion):

    def __init__(self, x, y):
        grillas = [
                pilas.imagenes.cargar_grilla("golpe_1.png", 2),
                pilas.imagenes.cargar_grilla("golpe_2.png", 2),
            ]

        grilla = random.choice(grillas)
        pilas.actores.Animacion.__init__(self, grilla, ciclica=False, 
            velocidad=10, x=x, y=y)
        self.escala = 0.5
        self.escala = [1.5], 0.1

