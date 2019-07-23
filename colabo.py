import os
import sys
import errno
import cv2
import numpy as np

def make_directory(base_path, success_dir="success_img", fail_dir="fail_img"):
    # '\'를 문자열로 받을 시 문제 방지 위해 '/'로 변환
    base_path.replace('\\', '/')

    # '/'가 마지막에 포함되지 않을 시 절대경로 위해 '/'를 넣어줌.
    if base_path[-1] != "/":
        base_path = base_path + "/"
    success_dir = base_path + success_dir
    fail_dir = base_path + fail_dir
    path_list = [success_dir, fail_dir]
    for i in range(2):
        try:
            if not (os.path.isdir(path_list[i])):
                os.makedirs(os.path.join(path_list[i]))
        except OSError as e:
            if e.errno != errno.EEXIST:
                print("Failed to create %s directory!!!!!" % path_list[i])
                raise
    return path_list


def make_image_list(img_path, ext="jpg"):
    img_path.replace('\\', '/')
    ext_list = ["png", "jpg", "jpeg", "bmp"]

    # ext(확장자명) 추가 코드
    if ext not in ext_list:
        ext_list.append(ext)
        ext = ", ." + ext
    image_list = []
    img_dir = os.listdir(img_path)

    # ext 확인하여 ext_list에 있을 경우 img_list에 추가
    for file in img_dir:
        ext_check = file.split(".")[-1].lower()
        if ext_check in ext_list:
            image_list.append(file)

    # img_list가 없을 경우(확장자명이 일치하는 경우가 없을 경우)
    if len(image_list) == 0:
        if len(ext_list) == 4:
            print("There's no image file (.jpg, .png, .bmp)")
        else:
            print("There's no image file (.jpg, .png, .bmp%s)" % ext)
        return None
    return image_list




def read_yolo_data(save_dir_list, img_path, image_name):
    bbox_list = []
    img_path.replace('\\', '/')
    if img_path[-1] != "/":
        img_path = img_path + "/"
    img_dir = os.listdir(img_path)
    # image 정보 읽기 및 정보 유무 확인
    img = cv2.imread(img_path + image_name)
    if not img:
        print("%s 이미지를 읽을 수 없습니다." % image_name)
        save_path = None
    # bbox 정보, save path 저장
    for file in img_dir:
        if image_name[:-4]+".txt" == file:
            print("filename: " + file)
            try:
                f = open(img_path+file, "r")
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
                        bbox_list.append(line.split(" "))
                        save_path = save_dir_list[0]
                        # print(bbox_list)
                    # 요소가 부족한 경우 bbox None으로 반환
                    else:
                        save_path = save_dir_list[1]
        # bbox가 2개 이상인 경우, 1~(n-1)개는 5개요소이고, n번째는 5개 미만인 경우 잘못된 경우이므로, None으로 return 해줌.
                        return img, None, save_path
                break
    # txt 파일은 있으나 비어 있는 경우 or 파일이 열리지 않은 경우 or 파일이 없는 경우
    if not len(bbox_list):
        save_path = dir_list[1]
        return img, None, save_path
    # bbox가 제대로 읽어진 경우
    else:
        return img, bbox_list, save_path

def bbox_augmentation(bbox): # bbox 는 리스트 형태
    pass

# img_path = "C:/Users/bit/Desktop/yolo/img3"
img_path = "D:/파이썬/opencv/img3/img3"
# make_directory 테스트
dir_list = make_directory(img_path)


# make_image_list 테스트
image_list = make_image_list(img_path, "gif")
# print(image_list)

#for image_name in image_list:
print(image_list[1])
img1, bbox_list, save_path = read_yolo_data(dir_list, img_path, image_list[0])
# if bbox_list != None:
# print(bbox_list)
# print(save_path)







######################## 참고 ##############################

#cv2.imread loads an image from the specified file and returns it.
# If the image cannot be read (because of missing file, improper permissions, unsupported or invalid format),
# the function returns an empty matrix ( Mat::data==NULL ).
#
# Currently, the following file formats are supported:
#   Windows bitmaps - *.bmp, *.dib (always supported)
#   JPEG files - *.jpeg, *.jpg, *.jpe (see the Notes section)
#   JPEG 2000 files - *.jp2 (see the Notes section)
#   Portable Network Graphics - *.png (see the Notes section)
#   WebP - *.webp (see the Notes section)
#   Portable image format - *.pbm, *.pgm, *.ppm (always supported)
#   Sun rasters - *.sr, *.ras (always supported)
#   TIFF files - *.tiff, *.tif (see the Notes section)



