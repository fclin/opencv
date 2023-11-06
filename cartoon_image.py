# 如何透過 opencv 將圖片做成卡通圖

import cv2

image = cv2.imread('T29_FCLin.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray, 7)

edges = cv2.Canny(blurred, 100, 200)
ret, threshold = cv2.threshold(edges, 150, 255, cv2.THRESH_BINARY)
color = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
cartoon = cv2.bitwise_and(color, color, mask=threshold)

cv2_imshow(cartoon)

# 若要儲存卡通圖像
cv2.imwrite('cartoon_image.jpg', cartoon)
