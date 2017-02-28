"""Prueba de Estructuras."""
from Lista import Lista

list = Lista()
list.agregar("a")
list.agregar("b")
list.agregar("c")
list.agregar("d")
list.agregar("e")
list.agregar("f")
list.agregar("g")
list.agregar("h")
list.agregar("i")
list.agregar("j")
list.agregar("k")
list.agregar("l")


list.verLista()


list.buscar("f")

print "La lista tiene longitud de : "+str(list.longitud())
