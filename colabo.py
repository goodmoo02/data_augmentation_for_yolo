from util import *
from data_aug_for_yolo import *

img_path = "C:/Users/bit/Desktop/yolo/img5"

# check_directory 테스트
if check_directory(img_path) == -1:
    exit(-1)

# make_directory 테스트
dir_list = make_directory(img_path)

# make_image_list 테스트
image_list = make_image_list(img_path, "gif")
if image_list == None:
    exit(-1)

for image_name in image_list:
    img1, bbox_list, save_path = read_yolo_data(dir_list, img_path, image_name)
    img2, bbox = RandomFlip(img1, bbox_list)
    img3, bbox = RandomResize(img2, bbox)
    SaveImage(img3, bbox, save_path, image_name)

cv2.destroyAllWindows()






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
