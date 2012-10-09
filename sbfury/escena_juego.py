# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar

import pilas
import shaolin
import escenario



class EscenaJuego(pilas.escena.escena_base.EscenaBase):
    """Representa la escena de juego en donde el shaolin va luchando."""

    def __init__(self):
        pilas.escena.escena_base.EscenaBase.__init__(self)


    def iniciar(self):
        self.lista_enemigos = []
        self.cantidad_de_enemigos = 0

        self._crear_barras_de_energia()
        self.shaolin = shaolin.Shaolin(self.lista_enemigos, self)

        self._crear_eventos_personalizados()
        self._crear_escenario()

    def _crear_eventos_personalizados(self):
        pilas.eventos.se_golpea_a_enemigo = pilas.eventos.Evento("se_golpea_enemigo")
        pilas.eventos.se_golpea_a_enemigo.conectar(self.actualizar_energia_enemigo)

        pilas.eventos.se_golpea_a_shaolin = pilas.eventos.Evento("se_golpea_shaolin")
        pilas.eventos.se_golpea_a_shaolin.conectar(self.actualizar_energia_shaolin)

        pilas.eventos.se_muere_un_enemigo = pilas.eventos.Evento("se_muere_un_enemigo")
        pilas.eventos.se_muere_un_enemigo.conectar(self._cuando_muere_un_enemigo)

        pilas.eventos.se_muere_el_shaolin = pilas.eventos.Evento("se_muere_el_shaolin")
        pilas.eventos.se_muere_el_shaolin.conectar(self._cuando_muere_el_shaolin)

    def _crear_escenario(self):
        escenario.Escenario(self)

    def crear_enemigo(self, clase, x, y):
        self.lista_enemigos.append(clase(self.shaolin, x=x, y=y))
        self.cantidad_de_enemigos += 1

    def _cuando_muere_un_enemigo(self, evento):
        #actor_que_muere = evento.actor
        self.cantidad_de_enemigos -= 1

    def _cuando_muere_el_shaolin(self, evento):
        #referencia_al_shaolin_que_muere = evento.actor
        self._crear_texto_game_over()
        pilas.eventos.pulsa_tecla_escape.conectar(self._reiniciar_el_nivel)

    def _reiniciar_el_nivel(self, evento):
        EscenaJuego()

    def _crear_texto_game_over(self):
        titulo = "Game Over"
        subtitulo = "Pulse escape para reiniciar"
        self._crear_mensaje_de_texto(subtitulo, titulo)

    def _crear_mensaje_de_texto(self, subtitulo, titulo):
        texto_titulo = pilas.actores.Texto(titulo, magnitud=40)
        texto_titulo.z = -1000
        texto_titulo.escala = 0.1
        texto_titulo.escala = [1], 0.5

        texto_subtitulo = pilas.actores.Texto(subtitulo)
        texto_subtitulo.y = -60
        texto_subtitulo.transparencia = 100
        texto_subtitulo.transparencia = [0]
        texto_subtitulo.z = -1000

    def _crear_barras_de_energia(self):
        self.energia_shaolin = pilas.actores.Energia(x=-280, y=213, alto=20)
        self.energia_shaolin.cargar_miniatura("shaolin/mini.png")
        self.energia_enemigo = pilas.actores.Energia(x=+315, y=213, alto=20)

    def actualizar_energia_enemigo(self, evento):
        self.energia_enemigo.progreso = evento.quien.energia
        self.energia_enemigo.cargar_miniatura(evento.quien.miniatura)

    def actualizar_energia_shaolin(self, evento):
        self.energia_shaolin.progreso = evento.quien.energia

    def nivel_terminado(self):
        titulo = "Nivel Completado"
        subtitulo = "---"
        self._crear_mensaje_de_texto(subtitulo, titulo)
        pilas.mundo.agregar_tarea(3, self._pasar_al_siguiente_nivel)

    def _pasar_al_siguiente_nivel(self):
        import sys
        sys.exit(1)
