import pickle
from Logistic_Regression import Plotter
class prueba:
    def __init__(self, val, val2):
        self.val = val
        self.val2 = val2

    def getValue(self):
        return self.val


def pruebaGuardar():
    pr = prueba(12,15)
    save_object(pr, "Guardar/prueba.pkl")

def pruebaCarga():
    pr = cargar("Guardar/prueba.pkl")
    print(pr.val2)
    print(pr.getValue())

def save_object(obj, filename):
    with open(filename, 'wb') as output: 
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def cargar(filename):
    with open(filename, 'rb') as input: 
        obj = pickle.load(input)
    return obj

def pruebaGraficas():
    modelo1 = cargar("Guardar/ModeoloUsac01.pkl")
    modelo2 = cargar("Guardar/ModeoloUsac07.pkl")
    modelo3 = cargar("Guardar/ModeoloUsac08.pkl")
    modelo4 = cargar("Guardar/ModeoloUsac09.pkl")
    modelo5 = cargar("Guardar/ModeoloUsac10.pkl")

    Plotter.show_Model([modelo1, modelo2, modelo3, modelo4, modelo5])


pruebaGraficas()