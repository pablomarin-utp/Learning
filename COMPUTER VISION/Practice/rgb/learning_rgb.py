import cv2
import os
import numpy as np
# Ruta del archivo
file_path = 'prueba.jpeg'

# Verifica si el archivo existe

bgr = cv2.imread(file_path)
if bgr is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta del archivo.")
else:
    print("Imagen cargada correctamente.")
    C1 = bgr[:,:,0]
    C2 = bgr[:,:,1]
    C3 = bgr[:,:,2]
    cv2.imshow("BGR Channels", np.hstack([C1, C2, C3]))
    rgb =cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    C1 = rgb[:,:,0]
    C2 = rgb[:,:,1]
    C3 = rgb[:,:,2]
    cv2.imshow("RGB Channels", np.hstack([C1, C2, C3]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
