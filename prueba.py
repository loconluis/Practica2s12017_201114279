"""Prueba de Estructuras."""
# from Lista import Lista
from Cola import Cola

# list = Lista()
cola = Cola()
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
cola.push(50)
# list.verLista()
cola.verCola()
print "*****************************"

print "Se elimino: "+str(cola.pop())

cola.verCola()
print "*****************************"

print "Se elimino: "+str(cola.pop())

cola.verCola()
# list.buscar("f")

# print "La lista tiene longitud de : "+str(list.longitud())
