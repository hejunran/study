import torch
import os
from PIL import Image
import xml.etree.ElementTree as ET
import scipy.io as scio
import cv2
import numpy as np
import h5py

datalist=[]

with open('G:/DATA/VOCdevkitSDS-Yangjie/val.txt','r') as f:
    data = f.readlines()
    for i in range(len(data)):
        datalist.append(data[i].split()[0])

datatrainlist=[]
with open('G:/DATA/VOCdevkitSDS-Yangjie/train.txt') as ft:
    data = ft.readlines()
    for i in range(len(data)):
        datatrainlist.append(data[i].split()[0])
print(datalist)
# 数据矩阵转图片的函数


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

name_classes = ["bc", "blj", "dlj", "fzcz", "hkmj",'hqc','pbc', "qt", "qxyj", "qzj",
                    "xlj", "yc", "yt"]

img_path ='G:/DATA/VOCdevkitSDS-Yangjie/img'
image_id = os.listdir(img_path)

xml_path ='G:/DATA/VOCdevkitSDS-Yangjie/Annotations'
xml_id = os.listdir(xml_path)

png_path ='G:/DATA/VOCdevkitSDS-Yangjie/png'

new_root = 'D:/python_study/process_data_yangjie'

for i in image_id:
    img_path_name = os.path.join(img_path,i)
    xml_path_name = os.path.join(xml_path,i.split('.')[0]+'.xml')
    img = Image.open(img_path_name).convert('RGB')


    xml_file = open(xml_path_name,encoding='utf-8')
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for  obj in  root.iter('object'):
        difficult =0
        if obj.find('difficult')!=None:
            difficult = obj.find('difficult').text
        cls = obj.find('name').text

        new_img_path = os.path.join(new_root,cls,'image',i)
        new_xml_path = os.path.join(new_root,cls,'annotation',i.split('.')[0]+'.xml')

        img.save(new_img_path)
        tree.write(new_xml_path)

        png_path_name = os.path.join(png_path, i.split('.')[0] + '.png')
        orignal_png = Image.open(png_path_name).convert('P')

        orignal_png = np.array(orignal_png)
        # if cls in name_classes:
        #     cls_id = name_classes.index(cls)
        #     orignal_png[orignal_png > 0] = cls_id + 1

        orignal_png = Image.fromarray(orignal_png).convert('L')
        new_png_path = os.path.join(new_root,cls,'png',i.split('.')[0]+'.png')
        colorful(orignal_png, new_png_path)




