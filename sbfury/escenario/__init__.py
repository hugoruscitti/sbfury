import pilas

class Escenario:

    def __init__(self):
        fondos = [
                    ("nivel1/layer_3.png", -320, 240, 500),
                    ("nivel1/layer_2.png", -320, 240, 450),
                    ("nivel1/layer_1.png", -320, 240, 440),
                    ("nivel1/layer_0.png", -320,  19, 430),
                 ]
        self.capas = []

        for imagen, x, y, z in fondos:
            capa = pilas.actores.Actor(imagen)
            capa.centro = ("izquierda", "arriba")
            capa.x = x
            capa.y = y
            capa.z = z

            self.capas.append(capa)

        pilas.mundo.camara.x = [1000], 20
