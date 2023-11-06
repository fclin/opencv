# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 20:30:31 2021
@ 將圖片轉為灰階
@author: fclin 老師
"""
# 使用副程式 去背

import cv2
import remove_background as rbg

# 選擇第一隻攝影機
cap = cv2.VideoCapture(1)

while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read()

 # 將圖片轉為灰階
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 # 顯示圖片
  cv2.imshow('frame', frame)
  # Filename 
  filename = '.\images\savedImage.jpg'
  rbg.imageProcess(filename)
  cv2.imwrite(filename, frame) 

  # 若按下 q 鍵則離開迴圈
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
