"""Lista simple."""


class Nodo():
    """Clase Nodo."""

    def __init__(self):
        """Constructor."""
        self.dato = None
        self.sig = None

    def getDato(self):
        """Retorna el val."""
        return self.dato

    def setDato(self, dat):
        """Setea el valor."""
        self.dato = dat

    def getSig(self):
        """Retorna el siguiente."""
        return self.sig

    def setSig(self, siguiente):
        """Setea el siguiente."""
        self.sig = siguiente


class Lista():
    """Clase Lista."""

    def __init__(self):
        """Constructor Lista."""
        self.indice = None
        self.size = 0

    def estaVacia(self):
        """Verifica si esta vacia."""
        if self.indice is None:
            return True
        else:
            return False

    def agregar(self, dato):
        """Agrega un nuevo dato a la lista."""
        nuevo = Nodo()
        nuevo.setDato(dato)
        if self.estaVacia() is True:
            self.indice = nuevo
            self.indice.setSig(None)
        else:
            temp = Nodo()
            temp = self.indice
            while temp.getSig() is not None:
                temp = temp.getSig()
            temp.setSig(nuevo)

    def verLista(self):
        """Imprime la lista."""
        aux = Nodo()
        aux = self.indice
        while aux.getSig() is not None:
            print aux.getDato()
            aux = aux.getSig()
