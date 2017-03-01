"""Cola."""
import subprocess


class NodoC():
    """Clase Nodo de la cola."""

    def __init__(self):
        """Constructor."""
        self.dato = None
        self.sig = None

    def getDato(self):
        """Retorna el dato."""
        return self.dato

    def setDato(self, dat):
        """Setea el dato."""
        self.dato = dat

    def getSig(self):
        """Retorna el siguiente."""
        return self.sig

    def setSig(self, siguiente):
        """Setea el nodo siguiente."""
        self.sig = siguiente


class Cola():
    """Clase de la Cola."""

    def __init__(self):
        """Constructor."""
        self.cabeza = None
        self.cola = None
        self.size = 0

    def estaVacia(self):
        """Verifica si esta vacia la cola."""
        if self.cabeza is None:
            return True
        else:
            return False

    def push(self, dato):
        """Agrega a la cola."""
        nuevo = NodoC()
        nuevo.setDato(dato)
        if self.estaVacia() is True:
            self.cabeza = nuevo
            self.cola = self.cabeza
        else:
            temp = NodoC()
            temp = self.cabeza
            while temp.getSig() is not None:
                temp = temp.getSig()
            temp.setSig(nuevo)
            self.cola = nuevo

    def pop(self):
        """Elimina primero de la cola."""
        if self.cabeza is not None:
            temp = NodoC()
            temp = self.cabeza
            self.cabeza = temp.getSig()
            temp.setSig(None)
            return temp.getDato()
        else:
            return "Lista vacia"

    def verCola(self):
        """Imprime la cola."""
        if self.estaVacia() is False:
            aux = NodoC()
            aux = self.cabeza
            while aux is not None:
                print aux.getDato()
                aux = aux.getSig()
        else:
            print "No te salio"

    def graficar(self):
        """Metodo para graficar la Cola."""
        path = '/home/luislocon/Documentos/Cursos/EDD/Practica2EDD/Grafos/cola.dot'
        fo = open(path, "w")
        cadenaGrafo = "digraph { label = \"Cola\" \n \n"
        actual = NodoC()
        actual = self.cabeza
        while actual.getSig() is not None:
            cadenaGrafo += "\t"+str(actual.getDato())+"->"+str(actual.getSig().getDato())+"\n"
            actual = actual.getSig()
        cadenaGrafo += "}"
        fo.write(cadenaGrafo)
        fo.close()
        subprocess.call(["dot", "-Tpng", "-O", path])
