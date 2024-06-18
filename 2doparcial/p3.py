import cv2
import numpy as np


ruta_imagen1 = 'E:/dat241/2doparcial/img1.jpg'
ruta_imagen2 = 'E:/dat241/2doparcial/img1.jpg'


imagen1 = cv2.imread(ruta_imagen1)
imagen2 = cv2.imread(ruta_imagen2)


if imagen1 is None or imagen2 is None:
    print("Error al cargar las imágenes")
    exit()



if imagen1.shape != imagen2.shape:
    print("Las imágenes no tienen el mismo tamaño")
    exit()



suma = cv2.add(imagen1, imagen2)
resta = cv2.subtract(imagen1, imagen2)

cv2.imshow('Imagen 1', imagen1)
cv2.imshow('Imagen 2', imagen2)
cv2.imshow('Suma de las Imágenes', suma)
cv2.imshow('Resta de las Imágenes', resta)

cv2.waitKey(0)
cv2.destroyAllWindows()
