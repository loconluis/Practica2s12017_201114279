"""Prueba de Estructuras."""
# from Lista import Lista
from Cola import Cola
from Pila import Pila
# list = Lista()
cola = Cola()
pila = Pila()
# list.agregar("a")
# list.agregar("c")
# list.agregar("d")
# list.agregar("b")
# list.agregar("e")
# list.agregar("f")
# list.agregar("g")
# list.agregar("h")
# list.agregar("i")
# list.agregar("j")
# list.agregar("k")
# list.agregar("l")
cola.push(10)
cola.push(20)
cola.push(30)
cola.push(40)
# cola.push(50)
pila.push(10)
pila.push(20)
pila.push(30)
# list.verLista()
# list.graficar()
pila.verPila()
pila.graficar()
cola.verCola()
cola.graficar()
# print "*****************************"

# print "Se elimino: "+str(cola.pop())
# print "Se elimino: "+str(pila.pop())
# cola.verCola()
# pila.verPila()
# print "*****************************"

# print "Se elimino: "+str(cola.pop())
# print "Se elimino: "+str(pila.pop())
# cola.verCola()
# list.buscar("f")
# pila.verPila()
# print "*****************************"
# print "La lista tiene longitud de : "+str(list.longitud())
