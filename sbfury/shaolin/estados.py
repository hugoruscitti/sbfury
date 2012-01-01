# -*- encoding: utf-8 -*-
import pilas

class Comportamiento(pilas.comportamientos.Comportamiento):
    """Representa una accion que puede realizar el shaolin, cómo
    caminar, saltar, golpear etc...

    Esta clase es abstracta, así que solo estaría aquí para ser
    superclase de toda acción.

    También está basada en el sistema de comportamientos de pilas, 
    te recomiendo ver el actor ``cooperativista`` para un ejemplo
    mas sencillo de implementación de comportamientos.
    """

    def iniciar(self, shaolin):
        self.shaolin = shaolin
        self.control = pilas.mundo.control

class Parado(Comportamiento):


    def iniciar(self, shaolin):
        Comportamiento.iniciar(self, shaolin)
        self.shaolin.cambiar_animacion('stand')

    def actualizar(self):
        if self.control.izquierda or self.control.derecha:
            self.shaolin.hacer(Caminar())

        if self.control.arriba or self.control.abajo:
            self.shaolin.hacer(Caminar())

class Caminar(Comportamiento):

    def iniciar(self, shaolin):
        Comportamiento.iniciar(self, shaolin)
        self.shaolin.cambiar_animacion('attack1')

    def actualizar(self):
        x, y = 0, 0

        if self.control.izquierda:
            x = -1
            self.shaolin.espejado = True
        elif self.control.derecha:
            x = 1
            self.shaolin.espejado = False

        if self.control.arriba:
            y = 1
        elif self.control.abajo:
            y = -1

        if x == y == 0:
            self.shaolin.hacer(Parado())
        else:
            self.shaolin.mover(x, y)
