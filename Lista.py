"""Lista simple."""
import subprocess


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

    import subprocess

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
            self.size = self.size + 1
        else:
            temp = Nodo()
            temp = self.indice
            while temp.getSig() is not None:
                temp = temp.getSig()
            temp.setSig(nuevo)
            self.size = self.size + 1

    def buscar(self, dato):
        """Metodo Buscar."""
        temp = Nodo()
        temp = self.indice
        i = 1
        while temp is not None:
            if temp.getDato() == dato:
#                 print "Palabra: "+temp.getDato()+" en la posicion: "+str(i)
                return "El dato: <" + str(temp.getDato()) + "> encontrado en la posicion: " + str(i)
            else:
                temp = temp.getSig()
            i = i + 1
        return "Dato no encontrado"

    def longitud(self):
        """Retorna size."""
        value = self.size
        return value

    def verLista(self):
        """Imprime la lista."""
        if self.estaVacia() is False:
            aux = Nodo()
            aux = self.indice
            while aux is not None:
                print aux.getDato()
                aux = aux.getSig()
        else:
            print "No te salio"

    def graficar(self):
        """Metodo para graficar la lista."""
        path = '/home/luislocon/Documentos/Cursos/EDD/Practica2EDD/Grafos/lista.dot'
        fo = open(path, "w")
        cadenaGrafo = "digraph { label = \"Lista\" \n \n"
        actual = Nodo()
        actual = self.indice
    #    i = 0
        while actual.getSig() is not None:
            cadenaGrafo += "\t"+str(actual.getDato())+"->"+str(actual.getSig().getDato()+"\n")
            actual = actual.getSig()
        cadenaGrafo += "}"
        fo.write(cadenaGrafo)
        fo.close()
        subprocess.call(["dot", "-Tpng", "-O", path])
