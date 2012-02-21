# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import enemigo
import random
import golpe

class Estrella(enemigo.Enemigo):
    """Una estrella ninja que vuela intentando golpear al shaolin."""

    def __init__(self, x, y, direccion, shaolin):
        enemigo.Enemigo.__init__(self)
        self._cargar_imagen()
        self.shaolin = shaolin
        self.centro = ("centro", "centro")
        self.x = x
        self.y = y
        self.altura_del_salto = 100
        self.golpe = golpe.Golpe(self, [shaolin], -65, 0)
        self.direccion = direccion
        self.actualizar()
        self.aprender(pilas.habilidades.Arrastrable)

    def _cargar_imagen(self):
        """Carga una imagen de estrella ninja o de una taza de cafe (!!!)."""
        if random.randint(0, 10) < 8:
            self.imagen = "estrella.png"
        else:
            self.imagen = "cafe.png"

    def actualizar(self):
        enemigo.Enemigo.actualizar(self)
        self.x += self.direccion * 6
        self.rotacion += 10
        self.z = self.y
        self.sombra.escala = 0.5

        if self.esta_fuera_de_la_pantalla():
            self.eliminar_todo()

        if self.golpe and self.golpe.verificar_colisiones():
            self.eliminar_todo()


    def eliminar_todo(self):
        self.eliminar()
        self.sombra.eliminar()
        self.eliminar_golpe()

    def eliminar_golpe(self):
        if self.golpe:
            self.golpe.eliminar()
            self.golpe = None
