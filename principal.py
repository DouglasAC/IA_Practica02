from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import random
import pickle
from FileManagement import File
from Logistic_Regression.Model import Model
from Logistic_Regression.Data import Data
from Logistic_Regression import Plotter


def imagenesUsac():
    imagenes = []

    # imagenes usac
    contenidoUsac = os.listdir("Imagenes/USAC")
    # print(len(contenidoUsac))
    for imagen in contenidoUsac:
        im = Image.open("Imagenes/USAC/" + imagen)
        ar = np.asarray(im)
        # imagen y un 1 que representa que si es Usac
        imagenes.append([ar, 1])

    # imagenes no usac
    contenidoLandivar = os.listdir("Imagenes/Landivar")
    for imagen in contenidoLandivar:
        im = Image.open("Imagenes/Landivar/" + imagen)
        ar = np.asarray(im)
        # imagen y un 0 que representa que no es Usac
        imagenes.append([ar, 0])
    contenidoMariano = os.listdir("Imagenes/Mariano")
    for imagen in contenidoMariano:
        im = Image.open("Imagenes/Mariano/" + imagen)
        ar = np.asarray(im)
        # imagen y un 0 que representa que no es Usac
        imagenes.append([ar, 0])
    contenidoMarroquin = os.listdir("Imagenes/Marroquin")
    for imagen in contenidoMarroquin:
        im = Image.open("Imagenes/Marroquin/" + imagen)
        ar = np.asarray(im)
        # imagen y un 0 que representa que no es Usac
        imagenes.append([ar, 0])

    # Desordenar las imagenes

    random.shuffle(imagenes)

    # Separar las imagenes de las respuestas

    listaImagenes = []
    listaRespuestas = []
    for elemento in imagenes:
        listaImagenes.append(elemento[0])
        listaRespuestas.append(elemento[1])

    arregloImagenes = np.array(listaImagenes)
    arregloRespuestas = np.array(listaRespuestas)

    slice_point = int(arregloImagenes.shape[0] * 0.8)

    train_images = arregloImagenes[0:slice_point]
    train_result = arregloRespuestas[0:slice_point]

    test_images = arregloImagenes[slice_point:]
    test_result = arregloRespuestas[slice_point:]

    train_result = train_result.reshape((1, train_result.shape[0]))
    test_result = test_result.reshape((1, test_result.shape[0]))

    #print(len(train_images), len(train_result), len(test_images), len(test_result))
    return train_images, train_result, test_images, test_result, ["No USAC", "USAC"]


def modelosUsac():
    """
    # Cargando conjuntos de datos
    train_images_orig, train_result, test_images_orig, test_result, classes = imagenesUsac()
    # Convertir imagenes a un solo arreglo
    train_images = train_images_orig.reshape(train_images_orig.shape[0], -1).T
    test_images = test_images_orig.reshape(test_images_orig.shape[0], -1).T

    # Definir los conjuntos de datos
    train_set = Data(train_images, train_result, 255)
    test_set = Data(test_images, test_result, 255)
    
    model1 = Model(train_set, test_set, reg=True, alpha=0.0001, lam=300, MAX_ITERATIONS=10000)
    model1.training()
    save_object(model1, "Guardar/ModeoloUsac01.pkl")

    model2 = Model(train_set, test_set, reg=True, alpha=0.0001, lam=150, MAX_ITERATIONS=11000)
    model2.training()
    save_object(model2, "Guardar/ModeoloUsac02.pkl")

    model3 = Model(train_set, test_set, reg=True, alpha=0.00001, lam=300, MAX_ITERATIONS=12000)
    model3.training()
    save_object(model3, "Guardar/ModeoloUsac03.pkl")

    model4 = Model(train_set, test_set, reg=True, alpha=0.00001, lam=150, MAX_ITERATIONS=12000)
    model4.training()
    save_object(model4, "Guardar/ModeoloUsac04.pkl")
    """
    modelo = cargar("Guardar/ModeoloUsac01.pkl")

    model5 = Model(modelo.train_set, modelo.test_set, reg=True, alpha=0.0001, lam=0.01, MAX_ITERATIONS=10000)
    model5.training(print_training=True)
    save_object(model5, "Guardar/ModeoloUsac11.pkl")
    Plotter.show_Model([model5])

    """
    Plotter.show_Model([model2])

    img1 = datosPrueba("USAC_1.jpg", 1)
    predecir(img1, model2)
    img2 = datosPrueba("USAC_2.jpg", 1)
    predecir(img2, model2)
    img3 = datosPrueba("USAC_3.jpg", 1)
    predecir(img3, model2)
    img4 = datosPrueba("Landivar_1.jpg", 0)
    predecir(img4, model2)
    img5 = datosPrueba("Mariano_1.jpg", 0)
    predecir(img5, model2)
    img6 = datosPrueba("Marroquin_1.jpg", 0)
    predecir(img6, model2)
    """
    


def datosPrueba(nombre, valor = 0):
    imPrueba = Image.open("Imagenes/Pruebas/" + nombre)
    arrPrueba = np.asarray(imPrueba)

    arregloImagenes = np.array([arrPrueba])
    arregloRespuestas = np.array([valor])

    arregloRespuestas = arregloRespuestas.reshape(
        (1, arregloRespuestas.shape[0]))

    train_images_prueba = arregloImagenes.reshape(
        arregloImagenes.shape[0], -1).T
    train_set_prueba = Data(train_images_prueba, arregloRespuestas, 255)
    return train_set_prueba

def predecir(dataset, modelo):
    res = modelo.predict(dataset.x)
    print("respuesta", res)
    train_accuracy = 100 - np.mean(np.abs(res - dataset.y)) * 100
    print('Prueba: ', train_accuracy)


def save_object(obj, filename):
    with open(filename, 'wb') as output: 
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def cargar(filename):
    with open(filename, 'rb') as input: 
        obj = pickle.load(input)
    return obj

def cargarModelo():
    modelo = cargar("Guardar/ModeoloUsac01.pkl")
    img1 = datosPrueba("USAC_1.jpg", 1)
    predecir(img1, modelo)
    img2 = datosPrueba("USAC_2.jpg", 1)
    predecir(img2, modelo)
    img3 = datosPrueba("USAC_3.jpg", 1)
    predecir(img3, modelo)
    img4 = datosPrueba("Landivar_1.jpg", 0)
    predecir(img4, modelo)
    img5 = datosPrueba("Mariano_1.jpg", 0)
    predecir(img5, modelo)
    img6 = datosPrueba("Marroquin_1.jpg", 0)
    predecir(img6, modelo)

    print('Eficacia en entrenamiento: ', modelo.train_accuracy)
    print('Eficacia en prueba: ', modelo.test_accuracy, end='\r\n------------\r\n')

modelosUsac()
