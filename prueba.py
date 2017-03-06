# from Lista import Lista
# from Cola import Cola
from Pila import Pila

# ls = Lista()
# cl = Cola()
pl = Pila()

# ls.agregar("1")
# ls.agregar("2")
# ls.agregar("3")
# ls.agregar("4")
# cl.push("a")
# cl.push("b")
# cl.push("c")
# cl.push("d")
pl.push("A")
pl.push("B")
pl.push("C")
pl.push("D")
pl.push("E")

p = str(pl.pop())
print "dato eliminado: " + p
o = str(pl.pop())
print "dato eliminado: " + o
i = str(pl.pop())
print "dato eliminado: " + i
u = str(pl.pop())
print "dato eliminado: " + u
y = str(pl.pop())
print "dato eliminado: " + y

# p = str(cl.pop())
# print "dato eliminado: " + p
# q = str(cl.pop())
# print "dato eliminado: " + q
# s = str(cl.pop())
# print "dato eliminado: " + s
# t = str(cl.pop())
# print "dato eliminado: " + t
# x = str(cl.pop())
# print "dato eliminado: " + x
# parametro = str(2)

# print ls.buscar(parametro)
