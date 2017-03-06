"""Lista simple."""
import subprocess


class Nodo():
    """Clase Nodo."""

    def __init__(self):
        """Constructor."""
        self.dato = None
        self.pos = None
        self.sig = None

    def getDato(self):
        """Retorna el val."""
        return self.dato

    def setDato(self, dat):
        """Setea el valor."""
        self.dato = dat

    def getPos(self):
        """Devuelve la posicion."""
        return self.pos

    def setPos(self, posicion):
        """Setea la posicion."""
        self.pos = posicion

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
            nuevo.setPos(self.size)
        else:
            temp = Nodo()
            temp = self.indice
            while temp.getSig() is not None:
                temp = temp.getSig()
            temp.setSig(nuevo)
            self.size = self.size + 1
            nuevo.setPos(self.size)

    def buscar(self, dato):
        """Metodo Buscar."""
        temp = Nodo()
        temp = self.indice
        i = 1
        while temp is not None:
            if temp.getDato() == dato:
# print "Palabra: "+temp.getDato()+" en la posicion: "+str(i)
# return "El dato: <" + str(temp.getDato()) + "> encontrado en la posicion: " + str(i)
                return str(i)
            else:
                temp = temp.getSig()
            i = i + 1
        return "Dato no encontrado"

    def eliminar(self, i):
        """Metodo para eliminar por indice."""
        temp1 = Nodo()
        temp2 = Nodo()
        temp3 = Nodo()
        temp1 = self.indice
        temp2 = temp1.getSig()
        temp3 = temp2.getSig()
        if temp1.getPos() == i:
            self.indice = temp1.getSig()
        elif i < (self.longitud()):
            while self.buscar(temp2.getDato()) == i:
                temp1 = temp1.getSig()
                temp2 = temp1.getSig()
                temp3 = temp2.getSig()
            temp1.setSig(temp3)
            temp2 = None
        elif i == self.longitud():
            while temp2.getSig() is not None:
                temp2 = temp2.getSig()
            temp2 = None

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
        if self.longitud() == 0:
            cadenaGrafo += "}"
        elif self.longitud() == 1:
            cadenaGrafo += str(actual.getDato()) + "}"
        else:
            while actual.getSig() is not None:
                cadenaGrafo += "\t"+str(actual.getDato())+"->"+str(actual.getSig().getDato()+"\n")
                actual = actual.getSig()
            cadenaGrafo += "}"
        fo.write(cadenaGrafo)
        fo.close()
        subprocess.call(["dot", "-Tpng", "-O", path])
