import os
import sys
import errno
import cv2
import numpy as np
import re

def check_directory(path):
    if not (os.path.isdir(path)):
        print("no directory")
        return -1
    else:
        os.chdir(path)
        return 1

def make_directory(success_dir="Yolo_data/", fail_dir="No_Yolo_data/"):
    success_dir.replace('\\', '/')
    fail_dir.replace('\\', '/')

    path_list = [success_dir, fail_dir]

    for path in path_list:
        if path[-1] != "/":
            path = path + "/"
        try:
            if not (os.path.isdir(path)):
                os.makedirs(os.path.join(path))
        except OSError as e:
            if e.errno != errno.EEXIST:
                print("Failed to create %s directory!!!!!" % path)
                raise
    return path_list


def make_image_list(ext="jpg"):
    ext_list = ["png", "jpg", "jpeg", "bmp"]

    # ext(확장자명) 추가 코드
    if ext not in ext_list:
        ext_list.append(ext)
        ext = ", ." + ext

    ext_list = tuple(ext_list)
    img_dir = os.listdir('.')

    # ext 확인하여 ext_list에 있을 경우 img_list에 추가
    image_list= [file for file in img_dir if file.endswith(ext_list)]

    # img_list가 없을 경우(확장자명이 일치하는 경우가 없을 경우)
    if len(image_list) == 0:
        if len(ext_list) == 4:
            print("There's no image file (.jpg, .png, .bmp)")
        else:
            print("There's no image file (.jpg, .png, .bmp%s)" % ext)
        return None
    return image_list

def hangeul_image_name_imread(file_path):
    stream = open(file_path.encode("utf-8"), "rb")
    bytes = bytearray(stream.read())
    numpyArray = np.asarray(bytes, dtype=np.uint8)

    return cv2.imdecode(numpyArray, cv2.IMREAD_UNCHANGED)


def read_yolo_data(save_dir_list, image_name):
    bbox_list = []
    img_dir = os.listdir('.')
    # image 정보 읽기 및 정보 유무 확인
    img = cv2.imread(image_name)
    if img is None:
        print("%s 이미지를 읽을 수 없습니다." % image_name)
        save_path = None

    # bbox 정보, save path 저장
    for file in img_dir:
        if image_name[:-4]+".txt" == file:
            try:
                f = open(file, "r")
            except FileNotFoundError:
                print('%s 파일이 없습니다.' % file)
                break
            else:
                while True:
                    line = f.readline()

                    # line에 읽어온 정보가 없을 때 break
                    if not line: break

                    # line 끝의 '\n' 와 ' '을 제외
                    while True:
                        if line[-1] == '\n' or line[-1] == ' ':
                            line = line[:-1]
                        else:
                            break
                    # bbox가 5개로 구성되면 bbox_list에 추가
                    if len(line.split(" ")) == 5:
                        line1 = line.split(" ")
                        for idx, value in enumerate(line1):
                            line1[idx] = float(value)
                        bbox_list.append(line1)
                        save_path = save_dir_list[0]
                    # 요소가 부족한 경우 bbox None으로 반환
                    else:
                        save_path = save_dir_list[1]
        # bbox가 2개 이상인 경우, 1~(n-1)개는 5개요소이고, n번째는 5개 미만인 경우 잘못된 경우이므로, None으로 return 해줌.
                        return img, [], save_path
                break
    # txt 파일은 있으나 비어 있는 경우 or 파일이 열리지 않은 경우 or 파일이 없는 경우
    if not len(bbox_list):
        save_path = save_dir_list[1]
        return img, [], save_path
    # bbox가 제대로 읽어진 경우
    else:
        return img, bbox_list, save_path

def SaveImage(img, save_path, name, bbox = []):
    name = name[:-4]
    path = save_path + name
    img_path = path + ".jpg"
    bbox_path = path + ".txt"

    cv2.imwrite(img_path, img)

    if bbox != []:
        with open(bbox_path,'w') as f:
            for i in range(len(bbox)):
                bbox[i][0] = int(bbox[i][0])
                for j in range(5):
                    f.write(str(bbox[i][j]) + " ")

                f.write("\n")