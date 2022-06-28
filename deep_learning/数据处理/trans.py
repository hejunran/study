import torch
import cv2
import numpy as np
from PIL import  Image
import os

color={(0, 0, 0): 0, (128, 0, 0): 1, (0, 128, 0): 2, (128, 128, 0): 3,
 (0, 0, 128): 4, (128, 0, 128): 5, (0, 128, 128): 6, (128, 128, 128): 7,
 (64, 0, 0): 8, (192, 0, 0): 9, (64, 128, 0): 10, (192, 128, 0): 11, (64, 0, 128): 12,
 (192, 0, 128): 13, (64, 128, 128): 14, (192, 128, 128): 15, (0, 64, 0): 16, (128, 64, 0): 17,
 (0, 192, 0): 18, (128, 192, 0): 19, (0, 64, 128): 20, (128, 64, 128): 21, (0, 192, 128): 22,
 (128, 192, 128): 23, (64, 64, 0): 24, (192, 64, 0): 25, (64, 192, 0): 26, (192, 192, 0): 27,
 (64, 64, 128): 28, (192, 64, 128): 29, (64, 192, 128): 30, (192, 192, 128): 31, (0, 0, 64): 32, (128, 0, 64): 33, (0, 128, 64): 34, (128, 128, 64): 35, (0, 0, 192): 36, (128, 0, 192): 37, (0, 128, 192): 38, (128, 128, 192): 39, (64, 0, 64): 40, (192, 0, 64): 41, (64, 128, 64): 42, (192, 128, 64): 43, (64, 0, 192): 44, (192, 0, 192): 45, (64, 128, 192): 46, (192, 128, 192): 47, (0, 64, 64): 48, (128, 64, 64): 49, (0, 192, 64): 50, (128, 192, 64): 51, (0, 64, 192): 52, (128, 64, 192): 53, (0, 192, 192): 54, (128, 192, 192): 55, (64, 64, 64): 56, (192, 64, 64): 57, (64, 192, 64): 58, (192, 192, 64): 59, (64, 64, 192): 60, (192, 64, 192): 61, (64, 192, 192): 62, (192, 192, 192): 63, (32, 0, 0): 64, (160, 0, 0): 65, (32, 128, 0): 66, (160, 128, 0): 67, (32, 0, 128): 68, (160, 0, 128): 69, (32, 128, 128): 70, (160, 128, 128): 71, (96, 0, 0): 72, (224, 0, 0): 73, (96, 128, 0): 74, (224, 128, 0): 75, (96, 0, 128): 76, (224, 0, 128): 77, (96, 128, 128): 78, (224, 128, 128): 79, (32, 64, 0): 80, (160, 64, 0): 81, (32, 192, 0): 82, (160, 192, 0): 83, (32, 64, 128): 84, (160, 64, 128): 85, (32, 192, 128): 86, (160, 192, 128): 87, (96, 64, 0): 88, (224, 64, 0): 89, (96, 192, 0): 90, (224, 192, 0): 91, (96, 64, 128): 92, (224, 64, 128): 93, (96, 192, 128): 94, (224, 192, 128): 95, (32, 0, 64): 96,
 (160, 0, 64): 97, (32, 128, 64): 98}

# png =Image.open('G:/DATA/process_ship/bc/label/000001.png').convert('P')
# png.show()
# print(png.palette)
#
# pngs =Image.open('G:/DATA/公共数据集/VOCdevkit/VOC2012/SegmentationClass/2007_000032.png')
# pngs.show()
# print(png)


def colorful(img, save_path):
    '''
    img:需要上色的图片
    save_path:存储路径
    '''


    # img = Image.fromarray(img)  # 将图像从numpy的数据格式转为PIL中的图像格式
    palette = []
    for i in range(256):
        palette.extend((i, i, i))
    palette[:3 * 21] = np.array([[0, 0, 0],
                             [128, 0, 0],
                             [0, 128, 0],
                             [128, 128, 0],
                             [0, 0, 128],
                             [128, 0, 128],
                             [0, 128, 128],
                             [128, 128, 128],
                             [64, 0, 0],
                             [192, 0, 0],
                             [64, 128, 0],
                             [192, 128, 0],
                             [64, 0, 128],
                             [192, 0, 128],
                             [64, 128, 128],
                             [192, 128, 128],
                             [0, 64, 0],
                             [128, 64, 0],
                             [0, 192, 0],
                             [128, 192, 0],
                             [0, 64, 128]
                             ], dtype='uint8').flatten()

    img.putpalette(palette)
    img.save(save_path)


# img=Image.open('G:/DATA/process_ship/bc/label/000001.png').convert('P')
# colorful(img, 'G:/DATA/process_ship/bc/000001.png')

if __name__ == '__main__':
    import random

    random.seed(101)
    f_train = open(
        '/datasets/voc/VOC2012/ImageSets/Segmentation/train.txt',
            'w')
    f_val = open(
        '/datasets/voc/VOC2012/ImageSets/Segmentation/val.txt',
            'w')

    f_test = open('/datasets/voc/VOC2012/ImageSets/Segmentation/test.txt',
              'w')

    # 一 1100
    resultList1 = [i for i in range(100000,101100)]
    resultList_train = random.sample(resultList1, 770)
    resultList_test_val=[]
    for i in resultList1:
        if i not in resultList_train:
            resultList_test_val.append(i)
        else:
            f_train.write(str(i)+'\n')

    resultList_test = random.sample(resultList_test_val,220)
    resultList_val = []
    for j in resultList_test_val:
        if j not in resultList_test:
            resultList_val.append(j)
            f_val.write(str(j)+'\n')
        else:
            f_test.write(str(j)+'\n')

    # 二 1175
    resultList1 = [i for i in range(101100, 102275)]
    resultList_train = random.sample(resultList1, 823)
    resultList_test_val = []
    for i in resultList1:

        if i not in resultList_train:
            resultList_test_val.append(i)
        else:
            f_train.write(str(i) + '\n')

    resultList_test = random.sample(resultList_test_val, 235)
    resultList_val = []
    for j in resultList_test_val:
        if j not in resultList_test:
            resultList_val.append(j)
            f_val.write(str(j) + '\n')
        else:
            f_test.write(str(j) + '\n')

    # 三： 1180
    resultList1 = [i for i in range(102275, 103455)]
    resultList_train = random.sample(resultList1, 826)
    resultList_test_val = []
    for i in resultList1:
        if i not in resultList_train:
            resultList_test_val.append(i)
        else:
            f_train.write(str(i) + '\n')

    resultList_test = random.sample(resultList_test_val, 236)
    resultList_val = []
    for j in resultList_test_val:
        if j not in resultList_test:
            resultList_val.append(j)
            f_val.write(str(j) + '\n')
        else:
            f_test.write(str(j) + '\n')

    # 四：1191
    resultList1 = [i for i in range(103455, 104646)]
    resultList_train = random.sample(resultList1, 834)
    resultList_test_val = []
    for i in resultList1:
        if i not in resultList_train:
            resultList_test_val.append(i)
        else:
            f_train.write(str(i) + '\n')

    resultList_test = random.sample(resultList_test_val, 238)
    resultList_val = []
    for j in resultList_test_val:
        if j not in resultList_test:
            resultList_val.append(j)
            f_val.write(str(j) + '\n')
        else:
            f_test.write(str(j) + '\n')

    # 五 1127
    resultList1 = [i for i in range(104646, 105773)]
    resultList_train = random.sample(resultList1, 789)
    resultList_test_val = []
    for i in resultList1:
        if i not in resultList_train:
            resultList_test_val.append(i)
        else:
            f_train.write(str(i) + '\n')

    resultList_test = random.sample(resultList_test_val, 225)
    resultList_val = []
    for j in resultList_test_val:
        if j not in resultList_test:
            resultList_val.append(j)
            f_val.write(str(j) + '\n')
        else:
            f_test.write(str(j) + '\n')

    # 六 1055
    resultList1 = [i for i in range(105773, 106828)]
    resultList_train = random.sample(resultList1, 739)
    resultList_test_val = []
    for i in resultList1:
        if i not in resultList_train:
            resultList_test_val.append(i)
        else:
            f_train.write(str(i) + '\n')

    resultList_test = random.sample(resultList_test_val, 211)
    resultList_val = []
    for j in resultList_test_val:
        if j not in resultList_test:
            resultList_val.append(j)
            f_val.write(str(j) + '\n')
        else:
            f_test.write(str(j) + '\n')

    # 七 1184
    resultList1 = [i for i in range(106828, 108012)]
    resultList_train = random.sample(resultList1, 829)
    resultList_test_val = []
    for i in resultList1:
        if i not in resultList_train:
            resultList_test_val.append(i)
        else:
            f_train.write(str(i) + '\n')

    resultList_test = random.sample(resultList_test_val, 237)
    resultList_val = []
    for j in resultList_test_val:
        if j not in resultList_test:
            resultList_val.append(j)
            f_val.write(str(j) + '\n')
        else:
            f_test.write(str(j) + '\n')

    # 八 1274
    resultList1 = [i for i in range(108012, 109286)]
    resultList_train = random.sample(resultList1, 892)
    resultList_test_val = []
    for i in resultList1:
        if i not in resultList_train:
            resultList_test_val.append(i)
        else:
            f_train.write(str(i) + '\n')

    resultList_test = random.sample(resultList_test_val, 255)
    resultList_val = []
    for j in resultList_test_val:
        if j not in resultList_test:
            resultList_val.append(j)
            f_val.write(str(j) + '\n')
        else:
            f_test.write(str(j) + '\n')
    # 九 1191
    resultList1 = [i for i in range(109286, 110477)]
    resultList_train = random.sample(resultList1, 834)
    resultList_test_val = []
    for i in resultList1:
        if i not in resultList_train:
            resultList_test_val.append(i)
        else:
            f_train.write(str(i) + '\n')

    resultList_test = random.sample(resultList_test_val, 238)
    resultList_val = []
    for j in resultList_test_val:
        if j not in resultList_test:
            resultList_val.append(j)
            f_val.write(str(j) + '\n')
        else:
            f_test.write(str(j) + '\n')
    # 十 1197
    resultList1 = [i for i in range(110477, 111674)]
    resultList_train = random.sample(resultList1, 838)
    resultList_test_val = []
    for i in resultList1:
        if i not in resultList_train:
            resultList_test_val.append(i)
        else:
            f_train.write(str(i) + '\n')

    resultList_test = random.sample(resultList_test_val, 239)
    resultList_val = []
    for j in resultList_test_val:
        if j not in resultList_test:
            resultList_val.append(j)
            f_val.write(str(j) + '\n')
        else:
            f_test.write(str(j) + '\n')

    # 十一 1375
    resultList1 = [i for i in range(111674, 113049)]
    resultList_train = random.sample(resultList1, 963)
    resultList_test_val = []
    for i in resultList1:
        if i not in resultList_train:
            resultList_test_val.append(i)
        else:
            f_train.write(str(i) + '\n')

    resultList_test = random.sample(resultList_test_val, 275)
    resultList_val = []
    for j in resultList_test_val:
        if j not in resultList_test:
            resultList_val.append(j)
            f_val.write(str(j) + '\n')
        else:
            f_test.write(str(j) + '\n')

    f_val.close()
    f_train.close()
    f_test.close()




    dir ='G:/DATA/process_ship'
    folder =os.listdir(dir)
    name_classes = ["bc", "blj", "dlj", "fzcz", "hkmj", "qt", "qxyj", "qzj",
                    "xlj", "yc", "yt"]

    num = 100000
    for i in folder:
        orignal_png_folder =os.path.join(dir,i,'label')
        orignal_png_names = os.listdir(orignal_png_folder)

        orignal_img_folder = os.path.join(dir,i,'image')
        new_img_folder ='C:/Users/Administrator/Desktop/awesome-semantic-segmentation-pytorch-master/datasets/voc/VOC2012/JPEGImages'

        new_png_folder ='C:/Users/Administrator/Desktop/awesome-semantic-segmentation-pytorch-master/datasets/voc/VOC2012/SegmentationClass'
        # for j in orignal_png_names:
        #     orignal_png_path = os.path.join(orignal_png_folder,j)
        #
        #     orignal_png = Image.open(orignal_png_path).convert('P')
        #
        #     orignal_png = np.array(orignal_png)
        #     if i in name_classes:
        #         cls_id = name_classes.index(i)
        #         orignal_png[orignal_png > 0] = cls_id + 1
        #
        #     orignal_png = Image.fromarray(orignal_png).convert('P')
        #     new_png_path = os.path.join(dir,i,'png',j)
        #     colorful(orignal_png, new_png_path)

        for k in os.listdir(orignal_img_folder):
            print(k)
            new_img_name = os.path.join(new_img_folder,str(num)+'.jpg')
            new_png_name = os.path.join(new_png_folder,str(num)+'.png')

            orignal_img_path =os.path.join(dir,i,'image',k)
            orignal_img = Image.open(orignal_img_path)
            orignal_img.save(new_img_name)

            orignal_png_path = os.path.join(dir,i,'png',k.split('.')[0]+'.png')
            orignal_png = Image.open(orignal_png_path)
            orignal_png.save(new_png_name)

            num +=1