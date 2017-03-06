"""Servicio Web."""

__author__ = "loconluis"

from flask import Flask, request
from Lista import Lista
from Cola import Cola
from Pila import Pila

app = Flask("Estructuras_de_Datos_Practica_2")
lista = Lista()
cola = Cola()
pila = Pila()


@app.route('/')
def hello():
    """Hello World."""
    return "Hello Word"

# Metodos para la lista


@app.route('/lista/agregar', methods=['POST'])
def add():
    """Metodo de agregar por POST."""
    parametro = str(request.form['dato'])
    lista.agregar(parametro)
    lista.graficar()
    return parametro


@app.route('/lista/buscar', methods=['POST'])
def serch():
    """Metodo de buscar por POST."""
    parametro = str(request.form['dato'])
    flag = lista.buscar(parametro)
    print flag
    return flag


# Metodos para la Cola


@app.route('/cola/agregar', methods=['POST'])
def pushC():
    """Metodo para agregar a la cola."""
    param = str(request.form['dato'])
    cola.push(param)
    cola.graficar()
    return param


@app.route('/cola/eliminar', methods=['POST'])
def popC():
    """Metodo para eliminar de la cola."""
    p = str(cola.pop())
    print "Elemento eliminado: " + p
    cola.graficar()
    return p

# Metodos para la Pila


@app.route('/pila/agregar', methods=['POST'])
def pushP():
    """Metodo para agregar a la cola."""
    param = str(request.form['dato'])
    pila.push(param)
    pila.graficar()
    return param


@app.route('/pila/eliminar', methods=['POST'])
def popP():
    """Metodo para eliminar de la cola."""
    p = str(pila.pop())
    print "Elemento eliminado: " + p
    pila.graficar()
    return p

# Metodos para la Matriz


app.run()
