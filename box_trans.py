class bbox:
    def __init__(self, path = None, ani = None):
        self.img_path = path
        self.ani = ani
        self.class_name = None
        self.x_coord = None
        self.y_coord = None
        self.width = None
        self.height = None
        self.trans_x_coord = None
        self.trans_y_coord = None
        self.trans_width = None
        self.trans_height = None

    # bbox_trans( ani - 동물종류, aug - 0: flip / 1: rotate / 2: else, opt - aug 옵션 [ flip - 0: 상하 / 1: 좌우 / 2: 상하 & 좌우 ], order - 텍스트 순서
    def bbox_trans(self, ani=None, aug=None, opt=None, order=None):
        '''
        :param ani: animal species
        :param aug: augmentation kinds (0: flip / 1: rotate / 2: else)
        :param opt: augmentaion option [ flip - 0: 상하 / 1: 좌우 / 2: 상하 & 좌우 ]
        :param order: txt order
        '''
        trans = None
        for i in range(order):
            print("현재 진행 순서: " + str(i + 1))
            self.insert(ani, (i + 1))
            if aug == 0:
                trans = self.flip(opt)
            elif aug == 1:
                self.rotate(opt)
            else:
                self.el(opt)
            self.write(trans, i + 1)

    # bbox.txt 1개 파일에서 bbox 추출
    def insert(self, ani=None, order = None):
        class_name_list = []
        x_coord_list = []
        y_coord_list = []
        width_list = []
        height_list = []
        self.ani = ani
        f = open(self.img_path + ani + str(order) + ".txt", "r")
        while True:
            line = f.readline()
            if not line: break
            class_name_list.append(line[0:2])
            x_coord_list.append(line[2:10])
            y_coord_list.append(line[11:19])
            width_list.append(line[20:28])
            height_list.append(line[29:37])
        self.class_name = class_name_list
        self.x_coord = x_coord_list
        self.y_coord = y_coord_list
        self.width = width_list
        self.height = height_list
        self.trans_x_coord = x_coord_list
        self.trans_y_coord = y_coord_list
        self.trans_width = width_list
        self.trans_height = height_list
        f.close()

    def write(self, trans, order):
        f = open(self.img_path + self.ani + "_" + trans + str(order) + ".txt", "a")
        for i in range(len(self.trans_x_coord)):
            line = self.class_name[i] + self.trans_x_coord[i] + " " + self.trans_y_coord[i] \
                    + " " + self.trans_width[i] + " " + self.trans_height[i] + "\n"
            f.write(line)
        f.close()


    # flip 시에는 x, y 좌표만 변경하면 됨.
    # opt - 0: 상하 / 1: 좌우 / 2: 상하 & 좌우
    def flip(self, opt):
        trans = None
        if opt == 0:
            trans = "ud_flip"
        elif opt == 1:
            trans = "lr_flip"
        else:
            trans = "all_flip"

        for i in range(len(self.trans_x_coord)):
            if (opt == 0 or opt == 2):
                coord = float(self.trans_x_coord[i])
                coord = 1. - coord
                coord = str(coord)
                while(len(coord) !=8):
                    coord = coord + "0"

                self.trans_x_coord[i] = coord
            if (opt == 1 or opt == 2):
                coord = float(self.trans_y_coord[i])
                coord = 1. - coord
                coord = str(coord)
                while(len(coord) != 8):
                    coord = coord + "0"
                self.trans_y_coord[i] = coord
        return trans

    def rotate(self):
        pass

    def el(self):
        pass


# img_path = "C:/Users/bit/Desktop/yolo/img2/"
#
#
# for j in range(4):
#     if j == 0:
#         ani = "cat"
#     elif j == 1:
#         ani = "fox"
#     elif j == 2:
#         ani = "lion"
#     elif j == 3:
#         ani = "tiger"
#     for i in range(251,301):
#         f = open(img_path+ani+str(i)+".txt", "r")
#         fp = open(img_path+ani+"_flip"+str(i)+".txt", "w")
#         print(f.name)
#         while True:
#             line = f.readline()
#             if not line: break
#             x_coord = float(line[2:10])
#             y_coord = float(line[11:19])
#             print(x_coord)
#             print(y_coord)
#             flip_coord = 1. - x_coord
#             flip_coord = round(x_coord, 6)
#             print(flip_coord)
#             flip_coord = str(flip_coord)
#             # flip_coord = coord_transfer()
#             print(line)
#
#             # x_coord flip 시
#             flip_line = line[0:2] + flip_coord + line[10:38]
#
#             # y_coord flip 시
#             flip_line = line[0:11] + flip_coord + line[19:38]
#             print(flip_line)
#             fp.write(flip_line)
#         f.close()
#         fp.close()


# bbox_trans( ani - 동물종류,
#             aug - 0: flip / 1: rotate / 2: else,
#             opt - aug 옵션 [ flip - 0: 상하 / 1: 좌우 / 2: 상하 & 좌우 ],
#             order - 텍스트 순서
img_path = "C:/Users/bit/Desktop/yolo/test/"
bb = bbox(img_path)
bb.bbox_trans("cat",0,2,300)

