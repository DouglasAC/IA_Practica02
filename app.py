from flask import Flask, render_template, request, json, jsonify
from datetime import datetime
import base64
import io
from io import BytesIO
from PIL import Image
import numpy as np
import re
from io import StringIO
import pickle
from Logistic_Regression.Model import Model
from Logistic_Regression.Data import Data
from Logistic_Regression import Plotter

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def cargar(filename):
    with open(filename, 'rb') as input: 
        obj = pickle.load(input)
    return obj

modeloUsac = cargar("Guardar/ModeoloUsac08.pkl")
modeloLandivar = cargar("Guardar/ModeoloLandivar01.pkl")
modeloMariano = cargar("Guardar/ModeoloUsac03.pkl")
modeloMarroquin = cargar("Guardar/ModeoloUsac04.pkl")

@app.route('/')
def inicio():

    return render_template('index.html')


@app.route('/imagenes', methods=['GET', 'POST', 'DELETE', 'PUT'])
def modelo():
    data = request.get_json()

    
    # print(data['imagenes'][0][1])
    # print(data['modo'])
    image_data = re.sub('^data:image/.+;base64,', '', data['imagenes'][0][1])
    im = Image.open(BytesIO(base64.b64decode(image_data)))
    ar = np.asarray(im)
    print(ar)
    im.show()
    return jsonify(
        solucion = 10,
        fitness  = 10
    )

@app.route('/cincoomenos', methods=['GET', 'POST', 'DELETE', 'PUT'])
def cincoomenos():
    data = request.get_json()
    imagenes  = data['imagenes']
    datos = []
    for imagen in imagenes:
        nombre = str(imagen[0]).split("_")[0]
        image_data = re.sub('^data:image/.+;base64,', '', imagen[1])
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        ar = np.asarray(im)
        datos.append([nombre, ar])

    respuestas = []

    for dato in datos:
        val = verificarUsac(dato[0], dato[1])
        if val == 1:
            respuestas.append("Usac")
            continue
        val = verificarLandivar(dato[0], dato[1])
        if val == 1:
            respuestas.append("Landivar")
            continue
        val = verificarMariano(dato[0], dato[1])
        if val == 1:
            respuestas.append("Mariano")
            continue
        val = verificarMarroquin(dato[0], dato[1])
        if val == 1:
            respuestas.append("Marroquin")
            continue
        respuestas.append("No se identifico")
    print(respuestas)
    return jsonify(
        respuesta = respuestas
    )
        
@app.route('/masdecinco', methods=['GET', 'POST', 'DELETE', 'PUT'])
def masdecinco():
    data = request.get_json()
    imagenes  = data['imagenes']
    datos = []
    for imagen in imagenes:
        nombre = str(imagen[0]).split("_")[0]
        image_data = re.sub('^data:image/.+;base64,', '', imagen[1])
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        ar = np.asarray(im)
        datos.append([nombre, ar])
    # [ usac, landivar, mariano, marroquin]
    # [ acerto, no acerto]
    respuestas = [[0,0],[0,0],[0,0],[0,0]]

    for dato in datos:
        
        if str(dato[0]).lower() == 'usac':
            val = verificarUsac(dato[0], dato[1])
            if val == 1:
                respuestas[0][0] += 1
                continue
            else:
                respuestas[0][1] += 1
                continue
        if str(dato[0]).lower() == 'landivar':
            val = verificarLandivar(dato[0], dato[1])
            if val == 1:
                respuestas[1][0] += 1
                continue
            else:
                respuestas[1][1] += 1
        if str(dato[0]).lower() == 'mariano':
            val = verificarMariano(dato[0], dato[1])
            if val == 1:
                respuestas[2][0] += 1
            else:
                respuestas[2][1] += 1
        if str(dato[0]).lower() == 'marroquin':
            val = verificarMarroquin(dato[0], dato[1])
            if val == 1:
                respuestas[3][0] += 1
                continue
            else:
                respuestas[3][1] += 1
    print(respuestas)
    return jsonify(
        respuesta = respuestas
    )

def verificarUsac(nombre, imagen):
    prueba = None
    if str(nombre).lower() == 'usac':
        prueba = datosPrueba(imagen, 1)
    else:
        prueba = datosPrueba(imagen, 0)
    res = modeloUsac.predict(prueba.x)
    return res

def verificarLandivar(nombre, imagen):
    prueba = None
    if str(nombre).lower() == 'landivar':
        prueba = datosPrueba(imagen, 1)
    else:
        prueba = datosPrueba(imagen, 0)
    res = modeloLandivar.predict(prueba.x)
    return res

def verificarMariano(nombre, imagen):
    prueba = None
    if str(nombre).lower() == 'mariano':
        prueba = datosPrueba(imagen, 1)
    else:
        prueba = datosPrueba(imagen, 0)
    res = modeloMariano.predict(prueba.x)
    return res

def verificarMarroquin(nombre, imagen):
    prueba = None
    if str(nombre).lower() == 'marroquin':
        prueba = datosPrueba(imagen, 1)
    else:
        prueba = datosPrueba(imagen, 0)
    res = modeloMarroquin.predict(prueba.x)
    return res

def predecir(dataset, modelo):
    res = modelo.predict(dataset.x)
    print("respuesta", res)
    train_accuracy = 100 - np.mean(np.abs(res - dataset.y)) * 100
    print('Prueba: ', train_accuracy)

def datosPrueba(imagen, valor):
    arregloImagenes = np.array([imagen])
    arregloRespuestas = np.array([valor])

    arregloRespuestas = arregloRespuestas.reshape(
        (1, arregloRespuestas.shape[0]))

    train_images_prueba = arregloImagenes.reshape(
        arregloImagenes.shape[0], -1).T
    train_set_prueba = Data(train_images_prueba, arregloRespuestas, 255)
    return train_set_prueba