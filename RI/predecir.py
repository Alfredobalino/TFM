import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

longitud, altura = 150, 150
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("pred: 1. Cuarzoarenitas y arcillas rojas con algún lentejón calizo")
  elif answer == 1:
    print("pred: 2. Cuarzoarenitas alternantes con limolitas verdes u oscuras.")
  elif answer == 2:
    print("pred: 3. Calizas con Ostrócodos y Choráceas.")
  elif answer == 1:
    print("pred: 4. Alternancia de calcarenitas y limolitas verdes o rojas.")
  elif answer == 2:
    print("pred: 5. Conglomerado silíceo con matriz limolítica arcillosa.")
  elif answer == 1:
    print("pred: 6. Alternancias en ciclos de cuarzoarenitas y arcillolitas predominantemente rojos(verdes hacia techo).")
  elif answer == 2:
    print("pred: 7. Depósitos morrénicos.")
  elif answer == 1:
    print("pred: 8. Derrubios de ladera.")
  elif answer == 2:
    print("pred: 9. Terrazas.")
  elif answer == 1:
    print("pred: 10. Aluvial. Incluso conos")
  elif answer == 2:
    print("pred: 11. Llanura de inundación")


  return answer
