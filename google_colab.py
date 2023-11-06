import cv2
from google.colab.patches import cv2_imshow

img = cv2.imread('T29_FCLin.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉成灰階
img = cv2.medianBlur(img, 7)                 # 模糊化，去除雜訊
output = cv2.Laplacian(img, -1, 1, 5)        # 偵測邊緣
cv2_imshow(output)

cv2.imwrite('me.jpg', output)
