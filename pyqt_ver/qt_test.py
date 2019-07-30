from util import *
from data_aug_for_yolo import *
import cv2
import os

def main(dir_path, hflip, vflip, angle, scale, x, y, resize_scale, prefix, suffix):
    save_path_list = make_directory(dir_path)

    image_name_list = make_image_list(dir_path)

    if image_name_list is None:
        return

    print("image list : ", len(image_name_list))
    print(image_name_list)


    for img_name in image_name_list:


        print("read yolo start")
        img, bboxes, save_path = read_yolo_data(save_path_list,dir_path,img_name)

        name = os.path.splitext(img_name)
        img_name = prefix + name[0] + suffix + name[1]

        print("data augment start")
        DataAugmentator(img,bboxes,save_path,img_name,hflip,vflip,angle,scale, x, y, resize_scale)



def DataAugmentator(img, bboxes, save_path, img_name, hflip, vflip, angle, scale, x = 0, y = 0, resize_scale = 1.0):

    if hflip == 2:
        img, bboxes = RandomFlip(img, bboxes)

    if vflip == 2:
        img,bboxes = RandomFlip(img, bboxes, mode=0)

    if scale != 1.0:
        img,bboxes = RandomScale(img, bboxes, scale=scale)

    if angle != 0:
        img = RandomRotate(img, angle=angle)

    print(x, y, resize_scale)
    if x != 0 and y != 0 and resize_scale != 1.0:
        img = RandomResize(img, x, y , resize_scale)

    if bboxes == []:
        SaveImage(img,save_path,img_name)
    else:
        SaveImage(img, save_path, img_name, bboxes)

if __name__ == '__main__':
    main("./test_img", 2, 2, 45, 0.7)
