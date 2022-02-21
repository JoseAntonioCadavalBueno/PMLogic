# coding=utf-8
'''
Created on 16 feb 2022

@author: root
'''
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #Capa de entrada
    celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
    fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)
    #Capa oculta
    oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
    oculta2 = tf.keras.layers.Dense(units=3)
    #Capa de salida
    salida = tf.keras.layers.Dense(units=1)
    modelo = tf.keras.Sequential([oculta1, oculta2, salida])
    
    modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error')
    #Entrenamiento
    print("Comenzando entrenamiento...")
    historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
    print("Modelo entrenado!")
    
    plt.xlabel("# Epoca")
    plt.ylabel("Magnitud de pérdida")
    plt.plot(historial.history["loss"])
    #Predicción
    print("Hagamos una predicción!")
    resultado = modelo.predict([100.0])
    print("El resultado es " + str(resultado) + " fahrenheit!")

    print(oculta1.get_weights())
    print(oculta2.get_weights())
    print(salida.get_weights())
    pass