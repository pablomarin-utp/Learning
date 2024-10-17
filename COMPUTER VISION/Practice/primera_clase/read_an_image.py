import cv2

img = cv2.imread("matrix.jpeg", 3)
cv2.imshow("Matrix", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
img = cv2.imread("matrix.jpeg", 0)
cv2.imwrite("gray.jpeg", img)