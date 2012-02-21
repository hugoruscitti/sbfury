# -*- encoding: utf-8 -*-
# Shaolin's Blind Fury
#
# Copyright: Hugo Ruscitti
# Web: www.losersjuegos.com.ar
import pilas
import random
import estrella


class Comportamiento(pilas.comportamientos.Comportamiento):

    def __init__(self, segundos=2):
        self.ticks_totales_para_avanzar_de_estado = segundos * 60
        self.contador_de_tiempo = 0

    def iniciar(self, enemigo):
        self.enemigo = enemigo
        self.control = pilas.mundo.control
        self.golpe = None

    def actualizar(self):
        self.contador_de_tiempo += 1

        if self.contador_de_tiempo > self.ticks_totales_para_avanzar_de_estado:
            self.contador_de_tiempo = 0
            self.enemigo.pasar_al_siguiente_estado_ai()
    
    #def golpear(self, dx=0, dy=40):
    #    self.golpe = golpe.Golpe(self.shaolin, self, self.shaolin.enemigos, dx, dy)

    #def eliminar_golpe(self):
    #    if self.golpe:
    #        self.golpe.eliminar()
    #        self.golpe = None

    def ha_golpeado(self, otro_actor):
        pass

    def ha_sido_golpeado(self, otro_actor, fuerte=False):
        # Mira hacia el lado en donde recibe el golpe.
        self.enemigo.espejado = otro_actor.x < self.enemigo.x

        if fuerte or self.enemigo.energia <= 0:
            self.enemigo.hacer(LoGolpeanFuerte())
        else:
            self.enemigo.hacer(LoGolpean())


class Parado(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.cambiar_animacion('parado')
        self.enemigo.mirar_al_shaolin()

    def actualizar(self):
        Comportamiento.actualizar(self)
        self.enemigo.mirar_al_shaolin()


class CaminarAleatoriamente(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.cambiar_animacion('caminar')

        self.dx = random.choice([1, -1])
        self.dy = random.choice([1, 0, -1])

    def actualizar(self):
        Comportamiento.actualizar(self)
        self.enemigo.mover(self.dx, self.dy)
        self.enemigo.mirar_al_shaolin()
        

class Golpear(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.cambiar_animacion('golpear')

    def actualizar(self):
        pass

class LoGolpean(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.cambiar_animacion('lo_golpean')
        self.x_inicial = self.enemigo.x
        self.y_inicial = self.enemigo.y
        self.contador = 20

        # emite evento para avisar que ha sido golpeado
        enemigo.reducir_energia(10)


    def actualizar(self):

        x = self.x_inicial
        y = self.y_inicial

        self.enemigo.x = random.choice([x - 1, x, x + 1])
        self.enemigo.y = random.choice([y - 1, y, y + 1])

        # timeout para regresar al estado parado:
        if self.contador < 0:
            self.enemigo.x = self.x_inicial
            self.enemigo.y = self.y_inicial
            self.enemigo.pasar_al_siguiente_estado_ai()
        else:
            self.contador -= 1
        
    def ha_sido_golpeado(self, otro_actor, fuerte=False):
        pass


class LoGolpeanFuerte(LoGolpean):

    def iniciar(self, enemigo):
        LoGolpean.iniciar(self, enemigo)
        self.enemigo.puede_ser_golpeado = False
        self.enemigo.cambiar_animacion('lo_golpean_fuerte')
        self.velocidad_general = 14
        self.velocidad_inicial = self.velocidad_general

        if self.enemigo.espejado:
            self.velocidad_horizontal = 1.55
        else:
            self.velocidad_horizontal = -1.55

        # emite evento para avisar que ha sido golpeado
        enemigo.reducir_energia(20)

    def actualizar(self):
        self.enemigo.altura_del_salto += self.velocidad_inicial
        self.velocidad_inicial -= 0.75

        if self.enemigo.altura_del_salto < 30:
            # Si está cerca del suelo se muestra acostado.
            self.enemigo.definir_cuadro(1)
        else:
            self.enemigo.definir_cuadro(0)

        if self.enemigo.altura_del_salto < 0:
            # Si toca el suelo rebota con menos intensidad.
            self.velocidad_horizontal /= 1.5
            self.velocidad_general -= 4
            self.velocidad_inicial = self.velocidad_general
            self.altura_del_salto = 0

            if self.velocidad_general < 0:
                self.terminar_caida()

        self.enemigo.mover(self.velocidad_horizontal, 0)

    def terminar_caida(self):
        if self.enemigo.energia <= 0:
            self.enemigo.hacer(Morirse())
        else:
            self.enemigo.hacer(QuedarseEnElSuelo())

class QuedarseEnElSuelo(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.cambiar_animacion('lo_golpean_fuerte')
        self.enemigo.definir_cuadro(1)
        self.contador = 60
        self.enemigo.puede_ser_golpeado = False

    def actualizar(self):
        self.enemigo.definir_cuadro(1)
        self.contador -= 1

        if self.contador < 0:
            self.levantarse()

    def levantarse(self):
        self.enemigo.puede_ser_golpeado = True
        self.enemigo.pasar_al_siguiente_estado_ai()



class CaminaHaciaLineaVerticalDelShaolin(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.cambiar_animacion('caminar')
        self._seleccionar_dy()
        self._salir_si_esta_cerca_verticalmente()

    def actualizar(self):
        Comportamiento.actualizar(self)
        self.enemigo.mover(0, self.dy)
        self.enemigo.mirar_al_shaolin()
        self._salir_si_esta_cerca_verticalmente()

    def _distancia_vertical_al_shaolin(self):
        return abs(self.enemigo.shaolin.y - self.enemigo.y)

    def _salir_si_esta_cerca_verticalmente(self):
        if self._distancia_vertical_al_shaolin() < 10:
            self.enemigo.pasar_al_siguiente_estado_ai()

    def _seleccionar_dy(self):
        if self.enemigo.shaolin.y < self.enemigo.y:
            self.dy = -1
        else:
            self.dy = 1


class LanzarEstrella(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.cambiar_animacion('lanzar')
        self.enemigo.mirar_al_shaolin()


        self.contador = 0


    def actualizar(self):
        Comportamiento.actualizar(self)
        self.enemigo.mirar_al_shaolin()

        self.contador += 1

        if self.contador == 10:
            self._lanzar_estrella()


        if self.contador > 30:
            self.enemigo.pasar_al_siguiente_estado_ai()

    def _lanzar_estrella(self):
        if self.enemigo.espejado:
            direccion = -1
        else:
            direccion = 1

        estrella.Estrella(self.enemigo.x, self.enemigo.y, direccion, self.enemigo.shaolin)

class Morirse(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.cambiar_animacion('lo_golpean_fuerte')
        self.enemigo.definir_cuadro(1)
        self.enemigo.puede_ser_golpeado = False
        pilas.eventos.se_muere_un_enemigo.emitir(actor=self)

    def actualizar(self):
        Comportamiento.actualizar(self)
        self.enemigo.definir_cuadro(1)

        self.enemigo.transparencia += 1
        self.enemigo.sombra.transparencia += 1

        if self.enemigo.transparencia > 100:
            self.eliminar_actor_del_escenario()

    def eliminar_actor_del_escenario(self):
        self.enemigo.sombra.eliminar()
        self.enemigo.eliminar()

class IngresarCajendo(Comportamiento):

    def iniciar(self, enemigo):
        Comportamiento.iniciar(self, enemigo)
        self.enemigo.mirar_al_shaolin()
        self.enemigo.puede_ser_golpeado = True
        self.enemigo.cambiar_animacion('saltando')
        self.enemigo.altura_del_salto = 400
        self.velocidad_inicial = 0

    def actualizar(self):
        self.enemigo.altura_del_salto += self.velocidad_inicial
        self.velocidad_inicial -= 0.75

        if self.enemigo.altura_del_salto < 0:
            self.enemigo.altura_del_salto = 0
            self.enemigo.pasar_al_siguiente_estado_ai()
