"""Pilas."""


class NodoP():
    """Clase nodo de la pila."""

    def __init__(self):
        """Constructor de la clase Pila."""
        self.dato = None
        self.sig = None

    def getDato(self):
        """Retorna el valor."""
        return self.dato

    def setDato(self, dat):
        """Setea el dato."""
        self.dato = dat

    def getSig(self):
        """Retorna el siguiente."""
        return self.sig

    def setSig(self, siguiente):
        """Setea el siguiente."""
        self.sig = siguiente


class Pila():
        """Clase Pila."""

        def __init__(self):
            """Constructor."""
            self.cabeza = None
            self.cola = None
            self.size = 0

        def estaVacia(self):
            """Valida si esta vacia la pila."""
            if self.cabeza is None:
                return True
            else:
                return False

        def push(self, dato):
            """Agregar a la pila."""
            nuevo = NodoP()
            nuevo.setDato(dato)
            if self.estaVacia() is True:
                self.cabeza = nuevo
                self.cola = self.cabeza
            else:
                temp = NodoP()
                temp = self.cabeza
                while temp.getSig() is not None:
                    temp = temp.getSig()
                temp.setSig(nuevo)
                self.cola = nuevo

        def pop(self):
            """Elimina al ultimo de la pila."""
            if self.cola is not None:
                temp1 = NodoP()
                temp2 = NodoP()
                temp1 = self.cola
                temp2 = self.cabeza
                while temp2.getSig() is not temp1:
                    temp2 = temp2.getSig()
                temp2.setSig(None)
                self.cola = temp2
                return temp1.getDato()
            else:
                return "Lista Vacia"

        def verPila(self):
            """Imprime la pila."""
            if self.estaVacia() is False:
                actual = NodoP()
                actual = self.cabeza
                while actual is not None:
                    print actual.getDato()
                    actual = actual.getSig()
            else:
                print "No te salio"
