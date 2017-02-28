"""Matriz."""


class NodoM():
    """Clase del nodo de la matriz dispersa."""

    def __init__(self):
        """Constructor."""
        self.dato = None
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None

    def getDato(self):
        """Retorna el dato."""
        return self.dato

    def setDato(self, dat):
        """Setea el dato."""
        self.dato = dat

    def getArriba(self):
        """Retorna el nodo superior."""
        return self.arriba

    def setArriba(self, up):
        """Setea el nodo superior."""
        self.arriba = up

    def getAbajo(self):
        """Retorna el nodo inferior."""
        return self.abajo

    def setAbajo(self, down):
        """Setea el nodo inferior."""
        self.abajo = down

    def getDerecha(self):
        """Retorna el nodo derecho."""
        return self.derecha

    def setDerecha(self, right):
        """Setea el nodo derecho."""
        self.derecha = right

    def getIzquierda(self):
        """Retorna el nodo izquierdo."""
        return self.izquierda

    def setIzquierda(self, left):
        """Setea el nodo izquierdo."""
        self.izquierda = left
