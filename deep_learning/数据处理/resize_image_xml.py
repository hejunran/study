import math
import os
from PIL import Image, ImageDraw
import numpy as np
import xml.etree.ElementTree as ET

name_classes = ["bc", "blj", "dlj", "fzcz", "hkmj","hqc","pbc","qt", "qxyj", "qzj",
                    "xlj", "yc", "yt"]

color={(0, 0, 0): 0, (128, 0, 0): 1, (0, 128, 0): 2, (128, 128, 0): 3,
 (0, 0, 128): 4, (128, 0, 128): 5, (0, 128, 128): 6, (128, 128, 128): 7,
 (64, 0, 0): 8, (192, 0, 0): 9, (64, 128, 0): 10, (192, 128, 0): 11, (64, 0, 128): 12,
 (192, 0, 128): 13, (64, 128, 128): 14, (192, 128, 128): 15, (0, 64, 0): 16, (128, 64, 0): 17,
 (0, 192, 0): 18, (128, 192, 0): 19, (0, 64, 128): 20, (128, 64, 128): 21, (0, 192, 128): 22,
 (128, 192, 128): 23, (64, 64, 0): 24, (192, 64, 0): 25, (64, 192, 0): 26, (192, 192, 0): 27,
 (64, 64, 128): 28, (192, 64, 128): 29, (64, 192, 128): 30, (192, 192, 128): 31, (0, 0, 64): 32, (128, 0, 64): 33, (0, 128, 64): 34, (128, 128, 64): 35, (0, 0, 192): 36, (128, 0, 192): 37, (0, 128, 192): 38, (128, 128, 192): 39, (64, 0, 64): 40, (192, 0, 64): 41, (64, 128, 64): 42, (192, 128, 64): 43, (64, 0, 192): 44, (192, 0, 192): 45, (64, 128, 192): 46, (192, 128, 192): 47, (0, 64, 64): 48, (128, 64, 64): 49, (0, 192, 64): 50, (128, 192, 64): 51, (0, 64, 192): 52, (128, 64, 192): 53, (0, 192, 192): 54, (128, 192, 192): 55, (64, 64, 64): 56, (192, 64, 64): 57, (64, 192, 64): 58, (192, 192, 64): 59, (64, 64, 192): 60, (192, 64, 192): 61, (64, 192, 192): 62, (192, 192, 192): 63, (32, 0, 0): 64, (160, 0, 0): 65, (32, 128, 0): 66, (160, 128, 0): 67, (32, 0, 128): 68, (160, 0, 128): 69, (32, 128, 128): 70, (160, 128, 128): 71, (96, 0, 0): 72, (224, 0, 0): 73, (96, 128, 0): 74, (224, 128, 0): 75, (96, 0, 128): 76, (224, 0, 128): 77, (96, 128, 128): 78, (224, 128, 128): 79, (32, 64, 0): 80, (160, 64, 0): 81, (32, 192, 0): 82, (160, 192, 0): 83, (32, 64, 128): 84, (160, 64, 128): 85, (32, 192, 128): 86, (160, 192, 128): 87, (96, 64, 0): 88, (224, 64, 0): 89, (96, 192, 0): 90, (224, 192, 0): 91, (96, 64, 128): 92, (224, 64, 128): 93, (96, 192, 128): 94, (224, 192, 128): 95, (32, 0, 64): 96,
 (160, 0, 64): 97, (32, 128, 64): 98}
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

def get_random_data(filename_jpg, box,png, nw, nh):
    """
    修改 box
    :param filename_jpg: 图片名
    :param box: 原box
    :param nw: 改变后的宽度
    :param nh: 改变后的高度
    :return:
    """
    image = Image.open(filename_jpg)
    iw, ih = image.size
    print('tupianchicun:', iw, ih)
    # 对图像进行缩放并且进行长和宽的扭曲
    image = image.resize((nw, nh), Image.BICUBIC)
    png = png.resize((nw, nh), Image.NEAREST)
    # 将box进行调整
    box_resize = []
    for boxx in box:

        boxx[0] = str(int(int(boxx[0]) * (nw / iw)))
        boxx[1] = str(int(int(boxx[1]) * (nh / ih)))
        boxx[2] = str(int(int(boxx[2]) * (nw / iw)))
        boxx[3] = str(int(int(boxx[3]) * (nh / ih)))
        box_resize.append(boxx)
    return image, box_resize,png


def read_xml(xml_name):
    """
    看原xml中的box
    :param xml_name: xml文件名
    :return:
    """
    etree = ET.parse(xml_name)
    root = etree.getroot()
    box = []
    for obj in root.iter('object'):
        xmin,ymin,xmax,ymax = (x.text for x in obj.find('bndbox'))
        box.append([xmin,ymin,xmax,ymax])
    print (len(box))
    print ('enen')
    return box

def write_xml(xml_name,save_name, box, resize_w, resize_h):
    """
    将修改后的box 写入到 xml文件中
    :param xml_name: 原xml
    :param save_name: 保存的xml
    :param box: 修改后需要写入的box
    :return:
    """
    etree = ET.parse(xml_name)
    root = etree.getroot()
    print(len(box))

    # 修改图片的宽度、高度
    for obj in root.iter('size'):
        obj.find('width').text = str(resize_w)
        obj.find('height').text = str(resize_h)

    # 修改box的值
    for obj, bo in zip(root.iter('object'), box):
        for index, x in enumerate(obj.find('bndbox')):
            x.text = bo[index]
            print(bo[index])

    etree.write(save_name)

def start(sourceDir, targetDir, resize_w, resize_h):
    """
    程序开始的主函数
    :param sourceDir: 源文件夹
    :param targetDir: 保存文件夹
    :param resize_w: 改变后的宽度
    :param resize_h: 改变后的高度
    :return:
    """
    sourceDir_images_path = os.path.join(sourceDir, 'image')

    for id in os.listdir(sourceDir_images_path):
        sourceDir_image_path = os.path.join(sourceDir_images_path,id)
        sourceDir_xml_path = os.path.join(sourceDir,'annotation',id.split('.')[0]+'.xml')
        sourceDir_png_path =os.path.join(sourceDir,"png",id.split('.')[0]+'.png')

        targetDir_image_path =os.path.join(targetDir,'image',id)
        targetDir_xml_path =os.path.join(targetDir,'annotation',id.split('.')[0]+'.xml')
        targetDir_png_path =os.path.join(targetDir,'png',id.split('.')[0]+'.png')

        box =read_xml(sourceDir_xml_path)
        png =Image.open(sourceDir_png_path).convert('P')
        image_data, box_data,png_data = get_random_data(sourceDir_image_path,box,png, resize_w, resize_h)

        image_data.save(targetDir_image_path)

        png_data = np.array(png_data)
        if sourceDir.split('\\')[-1] in name_classes:
            cls_id = name_classes.index(sourceDir.split('\\')[-1])
            png_data[png_data > 0] = cls_id + 1
        png_data = Image.fromarray(png_data).convert('P')

        colorful(png_data, targetDir_png_path)

        write_xml(sourceDir_xml_path, targetDir_xml_path, box_data, resize_w, resize_h)


if __name__ == "__main__":

    # 源文件夹
    sourceDir = r"D:\python_study\process_data_yangjie\yt"
    # 目标文件夹
    targetDir = r"D:\python_study\new_data\yt"
    start(sourceDir, targetDir, 256, 256)


