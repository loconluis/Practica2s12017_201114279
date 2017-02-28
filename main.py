"""Servicio Web."""

__author__ = "loconluis"

from flask import Flask, request, Response
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
    param = str(request.form['dato'])
    lista.agregar(param)


@app.route('/lista/buscar', methods=['GET'])
def serch():
    """Metodo de buscar por POST."""
    param = str(request.form['dato'])
    lista.buscar(param)


# Metodos para la Cola


def pushC():
    @app.route('/cola/agregar', methods=['POST'])
    """Metodo para agregar a la cola."""
    param = str(request.form['dato'])
    cola.push(param)


@app.route('/cola/eliminar', methods=['GET'])
def popC():
    """Metodo para eliminar de la cola."""
    cola.pop()

# Metodos para la Pila


@app.route('/pila/agregar', methods=['POST'])
def pushP():
    """Metodo para agregar a la cola."""
    param = str(request.form['dato'])
    cola.push(param)


@app.route('/pila/eliminar', methods=['GET'])
def popP():
    """Metodo para eliminar de la cola."""
    cola.pop()
# Metodos para la Matriz
