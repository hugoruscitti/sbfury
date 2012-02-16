# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import shaolin
import enemigos
import escenario

lista_enemigos = []

pilas.iniciar(ancho=853, alto=480, usar_motor='qtgl', titulo="Shaolin's Blind Fury")


s = shaolin.Shaolin(lista_enemigos)
lista_enemigos.append(enemigos.Red(s))
escenario.Escenario(s)

energia_shaolin = pilas.actores.Energia(x=-315, y=213, alto=20)
energia_enemigo = pilas.actores.Energia(x=310, y=213, alto=20)

#pilas.mundo.camara.x = [5300 - 640], 3
#pilas.mundo.camara.x = [100], 40
pilas.ejecutar()
