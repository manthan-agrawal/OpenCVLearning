import cv2

# read image
img = cv2.imread("data\\lena.jpg", 1)
print(img)

# show image
cv2.imshow("Window name",img)

# keep window running
cv2.waitKey(5000)# 0 -> do not close

# to destroy all running windows
cv2.destroyAllWindows()

