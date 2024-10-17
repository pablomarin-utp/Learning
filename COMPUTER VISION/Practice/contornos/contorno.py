import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('prueba.jpeg')

# Convertir a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar un umbral para obtener una imagen binaria
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Encontrar contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos en la imagen original
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Mostrar la imagen con contornos
cv2.imshow('Contornos', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
