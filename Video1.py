# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 20:30:31 2021
@ 基本秀圖像
@author: fclin 老師
"""

import cv2

# 選擇第一隻攝影機
cap = cv2.VideoCapture(1)

while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read()

  # 顯示圖片
  cv2.imshow('frame', frame)

  # 若按下 q 鍵則離開迴圈
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
