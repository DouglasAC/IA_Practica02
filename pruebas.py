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
    modelo = cargar("Guardar/ModeoloUsac03.pkl") ## 4
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloUsac12.pkl") ## 5
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloUsac08.pkl") ## 1 ----- este mejor en pruebas 
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloUsac09.pkl") ## 3
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloUsac10.pkl") ## 2
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])



def modelosLandivar():
    modelo = cargar("Guardar/ModeoloLandivar01.pkl")
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloLandivar02.pkl")
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloLandivar03.pkl")
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloLandivar06.pkl")
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloLandivar05.pkl")
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    
def modelosMariano():
    modelo = cargar("Guardar/ModeoloMariano01.pkl")
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloMariano02.pkl")
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloMariano06.pkl")
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloMariano04.pkl")
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloMariano05.pkl")
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])

def modelosMarroquin():
    modelo = cargar("Guardar/ModeoloMarroquin01.pkl")
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloMarroquin02.pkl")
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    Plotter.show_Model([modelo])
    modelo = cargar("Guardar/ModeoloMarroquin03.pkl")
    Plotter.show_Model([modelo])
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    modelo = cargar("Guardar/ModeoloMarroquin05.pkl")
    Plotter.show_Model([modelo])
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    modelo = cargar("Guardar/ModeoloMarroquin06.pkl")
    Plotter.show_Model([modelo])
    print("Entrenamiento:", modelo.train_accuracy, "Prueba:", modelo.test_accuracy, "Iteraciones:", modelo.MAX_ITERATIONS, "reg:", modelo.reg, "Alpha:", modelo.alpha, "Lam:", modelo.lam)
    
def pruebaGraficasLandivar():
    modelo1 = cargar("Guardar/ModeoloLandivar01.pkl")
    modelo2 = cargar("Guardar/ModeoloLandivar02.pkl")
    modelo3 = cargar("Guardar/ModeoloLandivar03.pkl") ## 4
    modelo4 = cargar("Guardar/ModeoloLandivar04.pkl") ## 5
    modelo5 = cargar("Guardar/ModeoloLandivar05.pkl")

    Plotter.show_Model([modelo1, modelo2, modelo3, modelo4, modelo5])

def pruebaGraficasMariano():
    modelo1 = cargar("Guardar/ModeoloMariano01.pkl")
    modelo2 = cargar("Guardar/ModeoloMariano02.pkl")
    modelo3 = cargar("Guardar/ModeoloMariano03.pkl") ## 4
    modelo4 = cargar("Guardar/ModeoloMariano04.pkl") ## 5
    modelo5 = cargar("Guardar/ModeoloMariano05.pkl")

    Plotter.show_Model([modelo1, modelo2, modelo3, modelo4, modelo5])

def pruebaGraficasMarroquin():
    modelo1 = cargar("Guardar/ModeoloMarroquin01.pkl")
    modelo2 = cargar("Guardar/ModeoloMarroquin02.pkl")
    modelo3 = cargar("Guardar/ModeoloMarroquin03.pkl") ## 4
    modelo4 = cargar("Guardar/ModeoloMarroquin04.pkl") ## 5
    modelo5 = cargar("Guardar/ModeoloMarroquin05.pkl")

    Plotter.show_Model([modelo1, modelo2, modelo3, modelo4, modelo5])

pruebaGraficas()
print("-------------------")
modelosLandivar()
print("-------------------")
modelosMariano()
print("-------------------")
modelosMarroquin()