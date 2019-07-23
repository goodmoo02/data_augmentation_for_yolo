import cv2
import numpy as np

img_path = "C:/Users/bit/Desktop/yolo/img2/"

for j in range(4):
    if j == 0:
        ani = "cat"
    elif j == 1:
        ani = "fox"
    elif j == 2:
        ani = "lion"
    elif j == 3:
        ani = "tiger"
    for i in range(251,301):
        src = cv2.imread(img_path+ani+str(i)+".jpg", cv2.IMREAD_UNCHANGED)
        dst = cv2.flip(dst, 0)  # 상하 반전
        # dst = cv2.flip(src, 1) # 좌우 반전
        # cv2.imwrite(img_path+ani+"_lr_flip"+str(i)+".jpg", dst)
        cv2.imwrite(img_path+ani+"_ud_flip"+str(i)+".jpg", dst)