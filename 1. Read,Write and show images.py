import cv2

# read image
img = cv2.imread("data\\lena.jpg", 1)
print(img)

# show image
cv2.imshow("Window name", img)

# keep window running + can be used to get which key is typed
key = cv2.waitKey(5000)   # 0 -> do not close
print(key)     # Ascii value will be returned


# to destroy all running windows
cv2.destroyAllWindows()

# to write a file
cv2.imwrite("data\\newFileName.png", img)


