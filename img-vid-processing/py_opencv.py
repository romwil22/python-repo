# Loading, Displaying, Resizing, and Creating Images

import cv2

img = cv2.imread("galaxy.jpg", 0)

print(type(img))
print(img)
print(img.shape)  # rows, columns
print(img.ndim) # dimension

img2 = cv2.imread("galaxy.jpg", 1)
print(type(img2))
print(img2)
print(img2.shape)
print(img2.ndim)

reimg = cv2.resize(img, (int(img.shape[0]/2), int(img.shape[1]/2)))
cv2.imshow("galaxy image", reimg)
cv2.imwrite("galaxy-resize.jpg", reimg)
cv2.waitKey(0)
cv2.destroyAllWindows()