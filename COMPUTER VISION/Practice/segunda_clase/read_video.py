import cv2

# Inicializar la captura de video desde la cámara
capture = cv2.VideoCapture(0)

# Definir el códec y crear el objeto VideoWriter
recorder = cv2.VideoWriter("Output.avi", cv2.VideoWriter_fourcc(*"XVID"), 20.0, (640, 480))

# Comprobar si la captura de video está abierta
while capture.isOpened():
    ret, img = capture.read()
    if ret:
        cv2.imshow('video', img)
        recorder.write(img)
        # Romper el bucle al presionar la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: break

# Liberar los recursos
capture.release()
recorder.release()
cv2.destroyAllWindows()
