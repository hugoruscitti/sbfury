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

    def pulsa_saltar(self):
        pass

    def pulsa_golpear(self):
        pass

class Parado(Comportamiento):

    def iniciar(self, shaolin):
        Comportamiento.iniciar(self, shaolin)
        self.shaolin.cambiar_animacion('parado')

    def actualizar(self):
        if self.control.izquierda or self.control.derecha:
            self.shaolin.hacer(Caminar())

        if self.control.arriba or self.control.abajo:
            self.shaolin.hacer(Caminar())

    def pulsa_golpear(self):
        self.shaolin.hacer(Golpear())

    def pulsa_saltar(self):
        self.shaolin.hacer(Saltar())

class Caminar(Comportamiento):

    def iniciar(self, shaolin):
        Comportamiento.iniciar(self, shaolin)
        self.shaolin.cambiar_animacion('camina')

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

        self.shaolin.avanzar_animacion(0.2)

    def pulsa_golpear(self):
        self.shaolin.hacer(Golpear())

    def pulsa_saltar(self):
        if self.control.izquierda:
            direccion = -1
        elif self.control.derecha:
            direccion = 1
        else:
            direccion = 0

        self.shaolin.hacer(SaltarCaminando(direccion))

class Golpear(Comportamiento):

    def iniciar(self, shaolin):
        Comportamiento.iniciar(self, shaolin)
        self.shaolin.cambiar_animacion('ataca1')
        self.shaolin.reproducir_sonido('golpe')
        self.shaolin.golpear(dy=90)

    def actualizar(self):
        if self.shaolin.avanzar_animacion(0.5):
            self.shaolin.hacer(Parado())

class Saltar(Comportamiento):

    def iniciar(self, shaolin):
        Comportamiento.iniciar(self, shaolin)
        self.shaolin.cambiar_animacion('salta')
        self.velocidad_inicial = 14

    def actualizar(self):
        self.shaolin.altura_del_salto += self.velocidad_inicial
        self.velocidad_inicial -= 0.75

        if self.shaolin.altura_del_salto < 0:
            self.shaolin.altura_del_salto = 0
            self.shaolin.hacer(Parado())

        if 1 < self.velocidad_inicial:
            self.shaolin.definir_cuadro(0)
        elif -5 < self.velocidad_inicial < 1:
            self.shaolin.definir_cuadro(1)
        elif self.velocidad_inicial < -5:
            self.shaolin.definir_cuadro(2)

    def pulsa_golpear(self):
        self.shaolin.hacer(GolpearSaltando(self.velocidad_inicial, 0))

class SaltarCaminando(Saltar):

    def __init__(self, direccion):
        self.direccion = direccion
        Saltar.__init__(self)

    def actualizar(self):
        Saltar.actualizar(self)
        self.shaolin.mover(self.direccion * 1.75, 0)

    def pulsa_golpear(self):
        self.shaolin.hacer(GolpearSaltando(self.velocidad_inicial, self.direccion))

class GolpearSaltando(Saltar):

    def __init__(self, velocidad_inicial, direccion):
        self.velocidad_inicial = velocidad_inicial
        self.direccion = direccion
        Saltar.__init__(self)
        self.contador = 0

    def iniciar(self, shaolin):
        Comportamiento.iniciar(self, shaolin)
        self.shaolin.cambiar_animacion("ataque_aereo")

    def actualizar(self):
        Saltar.actualizar(self)
        self.shaolin.mover(self.direccion * 1.75, 0)
        self.contador += 1

        if self.contador < 10:
            self.shaolin.definir_cuadro(0)
        else:
            self.shaolin.definir_cuadro(1)

        if self.contador == 5:
            self.shaolin.reproducir_sonido('golpe')
            self.shaolin.golpear(dx=40)

    def pulsa_golpear(self):
        pass
