import cv2
import mediapipe as mp

# Inicializar los objetos de MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Captura de video desde la cámara
capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break
    
    # Convertir la imagen a RGB (MediaPipe trabaja con imágenes RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Procesar la imagen y detectar manos
    result = hands.process(frame_rgb)
    
    # Si se detecta alguna mano
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Dibujar las conexiones y puntos de referencia de la mano
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2))
    
    # Mostrar el resultado
    cv2.imshow('Hand Tracking', frame)
    
    # Romper el bucle al presionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
capture.release()
cv2.destroyAllWindows()
