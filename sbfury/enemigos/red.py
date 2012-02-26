# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import enemigo
import estados

class Red(enemigo.Enemigo):
    """El Ninja de color rojo"""

    def __init__(self, shaolin, x, y):
        enemigo.Enemigo.__init__(self)
        self.shaolin = shaolin
        self._cargar_animaciones()
        self.z = 0
        self.centro = ("centro", "abajo")
        self.x = x
        self.y = y
        self.altura_del_salto = 0
        self.actualizar()

        # inicia la lista de comportamientos para inteligencia artificia (AI)
        self._iniciar()
        #self.pasar_al_siguiente_estado_ai()
        self.mover(0, 0)
        self.energia = 100

    def _iniciar(self):
        # inicia la lista de comportamientos para inteligencia artificia (AI)
        self.comportamientos_ai = [
                    estados.Parado(segundos=1),
                    estados.LanzarEstrella(),
                    estados.CaminarAleatoriamente(segundos=0.5),
                    estados.Golpear(),
                    estados.Parado(segundos=1),
                    estados.CaminaHaciaLineaVerticalDelShaolin(segundos=1),
                    ]
        self.comportamiento_ai_indice = 0

        self.hacer(estados.IngresarCayendo())
        self.miniatura = pilas.imagenes.cargar("red/mini.png")

    def actualizar(self):
        enemigo.Enemigo.actualizar(self)
        if self.avanzar_animacion(0.15):
            self.comportamiento_actual.ha_terminado_animacion()

    def pasar_al_siguiente_estado_ai(self):
        # Avanza en la lista de comportamientos como si fuera una lista
        # infinita.
        self.comportamiento_ai_indice += 1
        self.comportamiento_ai_indice %= len(self.comportamientos_ai)

        # Toma la instancia del comportamiento y comienza a realizarlo.
        estado_nuevo = self.comportamientos_ai[self.comportamiento_ai_indice]
        self.hacer(estado_nuevo)

    def _cargar_animaciones(self):
        cargar = pilas.imagenes.cargar_grilla
        self.animaciones = {
                'parado': cargar("red/parado.png", 1),
                'golpear': cargar("red/golpear.png", 3),
                'lo_golpean': cargar("red/lo_golpean.png", 1),
                'lo_golpean_fuerte': cargar("red/lo_golpean_fuerte.png", 2),
                'caminar': cargar("red/caminar.png", 4),
                'lanzar': cargar("red/lanzar.png", 4),
                'saltando': cargar("red/saltando.png", 1),
            }

    def mirar_al_shaolin(self):
        self.espejado = self.shaolin.x < self.x
