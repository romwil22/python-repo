import cv2
import glob

imgs = glob.glob("*.jpg")

for img in imgs:
    img1 = cv2.imread(img, 0)
    reimg = cv2.resize(img1, (100, 100))
    cv2.imshow("image new size", reimg)
    cv2,cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resize_"+img, reimg)

