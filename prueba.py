# from Lista import Lista
from Cola import Cola

# ls = Lista()
cl = Cola()

# ls.agregar("1")
# ls.agregar("2")
# ls.agregar("3")
# ls.agregar("4")
cl.push("a")
cl.push("b")
cl.push("c")
cl.push("d")

p = str(cl.pop())
print "dato eliminado: " + p
q = str(cl.pop())
print "dato eliminado: " + q
s = str(cl.pop())
print "dato eliminado: " + s
t = str(cl.pop())
print "dato eliminado: " + t
x = str(cl.pop())
print "dato eliminado: " + x
# parametro = str(2)

# print ls.buscar(parametro)
