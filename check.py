'''
Created on 16 feb 2022

@author: root
'''
import tensorflow as tf
#comprueba si la GPU est� disponible
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
#Comprueba la versi�n de Tensorflow
print(tf.__version__)