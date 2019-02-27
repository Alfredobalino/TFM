import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K

K.clear_session()


data_entrenamiento = './data/entrenamiento'
data_validacion = './data/validacion'

"""
Parameters
"""
epocas=20 ## número de iteraciones
longitud, altura = 150, 150 ## tamaño al que reducimos las imágenes (pixel)
batch_size = 32 ## número de imágenes por reconocimiento
pasos = 1000 ## número de veces de procesamiento, por cada epoca
validation_steps = 300 ## al final de cada epoca, otros procesamiento
filtrosConv1 = 32 ## número de filtros por convolución (profundidad 32)
filtrosConv2 = 64 ## número de filtros por convolución (profundidad 64)
tamano_filtro1 = (3, 3)## altura, longitud
tamano_filtro2 = (2, 2)
tamano_pool = (2, 2) ## tamaño de filtro para el pooling
clases = 11 ## número de diferentes DLO
lr = 0.0004 ## ajuste de la red


##Preparamos nuestras imagenes

entrenamiento_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,    ## inclinación
    zoom_range=0.2,     ## zoom (parciales)
    horizontal_flip=True)   ## inversión

test_datagen = ImageDataGenerator(rescale=1. / 255)

entrenamiento_generador = entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')

validacion_generador = test_datagen.flow_from_directory(
    data_validacion,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical')

cnn = Sequential()
cnn.add(Convolution2D(filtrosConv1, tamano_filtro1, padding ="same", input_shape=(longitud, altura, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Convolution2D(filtrosConv2, tamano_filtro2, padding ="same"))
cnn.add(MaxPooling2D(pool_size=tamano_pool))

cnn.add(Flatten())
cnn.add(Dense(256, activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(clases, activation='softmax'))

cnn.compile(loss='categorical_crossentropy',
            optimizer=optimizers.Adam(lr=lr),
            metrics=['accuracy'])




cnn.fit_generator(
    entrenamiento_generador,
    steps_per_epoch=pasos,
    epochs=epocas,
    validation_data=validacion_generador,
    validation_steps=validation_steps)

## Guardamos un archivo con cada clasicficación 
target_dir = './modelo/'
if not os.path.exists(target_dir):
  os.mkdir(target_dir)
cnn.save('./modelo/modelo.h5')
cnn.save_weights('./modelo/pesos.h5')
