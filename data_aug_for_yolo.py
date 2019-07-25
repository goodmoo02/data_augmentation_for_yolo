import numpy as np
import cv2
import random
import copy

def RandomFlip(img,bboxes,mode=1,p=1.0):
    # mode : 0 상하 반전 1 좌우 반전
    src = copy.deepcopy(img)
    bbox = copy.deepcopy(bboxes)

    if random.random() < p:
        print("flip 실행")
        dst = cv2.flip(src, mode)

        for i in range(len(bbox)):
            if mode == 0:
                bbox[i][2] = 1 - bbox[i][2]
            elif mode == 1:
                bbox[i][1] = 1 - bbox[i][1]

        return dst,bbox

    print("flip 미실행")
    return img, bboxes


def RandomResize(img, bbox, scale=0.7, p=1.0):
    src = copy.deepcopy(img)
    bbox = copy.deepcopy(bbox)

    if random.random() >= p:
        return src,bbox

    dsize = (int(src.shape[1] * scale),int(src.shape[0] * scale))
    dst = np.zeros(src.shape)

    src = cv2.resize(src,dsize,interpolation=cv2.INTER_AREA)
    # print(src.shape)

    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            dst[i][j] = src[i][j]

    for i in range(len(bbox)):
        for j in range(5):
            if j != 0:
                bbox[i][j] = bbox[i][j] * scale
    return dst,bbox


def RandomRotate(img,angle,scale=1.0,p=1.0):
    if random.random() > p:
        print("rotate 실행")
        return img

    H = img.shape[0]
    W = img.shape[1]
    matrix = cv2.getRotationMatrix2D((W / 2,H / 2),angle,scale)
    rotated = cv2.warpAffine(img,matrix,(W,H))

    return rotated



if __name__ == "__main__":
    img = cv2.imread("lena.jpg")

    cv2.imshow("img1", img)

    img2, _ = RandomResize(img, [])

    cv2.imshow("img2", img2)
    cv2.imwrite("lena_resize.jpg", img2)
    cv2.waitKey(0)