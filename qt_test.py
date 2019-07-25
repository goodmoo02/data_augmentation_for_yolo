from util import *
from data_aug_for_yolo import *
import cv2

def main(dir_path, hflip, vflip, angle, scale):
    save_path_list = make_directory(dir_path)

    image_name_list = make_image_list(dir_path)

    print("image list : ", len(image_name_list))
    print(image_name_list)

    for img_name in image_name_list:
        img, bboxes, save_path = read_yolo_data(save_path_list,dir_path,img_name)
        DataAugmentator(img,bboxes,save_path,img_name,hflip,vflip,angle,scale)


def DataAugmentator(img, bboxes, save_path, img_name, hflip, vflip, angle, scale):

    if hflip == 2:
        img, bboxes = RandomFlip(img, bboxes)

    if vflip == 2:
        img,bboxes = RandomFlip(img, bboxes, mode=0)

    if angle != 0:
        img = RandomRotate(img, angle=angle)

    if scale != 1.0:
        img,bboxes = RandomResize(img, bboxes, scale=scale)

    SaveImage(img, bboxes, save_path, img_name)

if __name__ == '__main__':
    main("./test_img", 2, 2, 45, 0.7)