import cv2

# read image
img = cv2.imread("data\\lena.jpg", 0)
print(img)

# show image
cv2.imshow("Window name",img)

# keep window running
cv2.waitKey(5000)

# to destroy all running windows
cv2.destroyAllWindows()

