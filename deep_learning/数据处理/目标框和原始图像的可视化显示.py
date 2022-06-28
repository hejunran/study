import numpy as np
import torch
import torch.nn as nn
import math
import cv2
import os
import torch.nn.functional as F
from PIL import Image, ImageDraw, ImageFont
from PIL import Image
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torch.utils.data.dataset import Dataset
from matplotlib import pyplot as plt
# import d2lzh as d2l
# from mxnet import image

name_classes = ["bc", "blj", "dlj", "fzcz", "hkmj", "qt", "qxyj", "qzj",
                    "xlj", "yc", "yt"]

COLORS={"bc":(0,0,128), "blj":(0,0,255), "dlj":(0,128,255), "fzcz":(0,255,255), "hkmj":(255,0,0),"qt":(255,0,128),
        "qxyj":(255,0,255), "qzj":(255,128,255),"xlj":(255,64,255), "yc":(64,0,255), "yt":(64,64,255)}

if __name__ == '__main__':

  
   annotation_path = 'D:/python_study/data/seg_dect_train.txt'
   val_split = 0.1
   with open(annotation_path) as f:
       lines = f.readlines()
   np.random.seed(10101)
   np.random.shuffle(lines)
   np.random.seed(None)
   num_val = int(len(lines) * val_split)
   num_train = len(lines) - num_val
   NUM_CLASSES = 12
   IMAGE_SHAPE = [256, 256, 3]


   FONT = cv2.FONT_HERSHEY_SIMPLEX
   for i in range(len(lines)):

       path =lines[i].split()[0]
       img = Image.open(lines[i].split()[0]).convert('RGB')
       img = np.array(img)

       "获取png的值"
       png_file = os.path.join('D:\python_study\process_data_yangjie', lines[i].split()[0].split('\\')[-3], 'png',
                               lines[i].split()[0].split('\\')[-1].split('.')[0] + '.png')
       png = Image.open(png_file)
       png = np.array(png)
       if png_file.split('\\')[-3] in name_classes:
           cls_id = name_classes.index(png_file.split('\\')[-3])
           png[png > 0] = 255
       "png 变成三通道，每个通道值一样 256 *256 *3 "
       png= np.stack((png,)*3, axis=-1)

       "此处是获取gt_box的值"
       boxes = np.array([np.array(list(map(int, box.split(',')))) for box in lines[i].split()[1:]])
       box_data = np.zeros((len(boxes), 5))
       box_data[:len(boxes)] = boxes
       y = box_data
       box = np.array(y[:, :4], dtype=np.float32)
       box[:, 0] = y[:, 0]
       box[:, 1] = y[:, 1]
       box[:, 2] = y[:, 2]
       box[:, 3] = y[:, 3]
       label = y[:, -1]

       left,top,right,bottom =int(box[0][0]),int(box[0][1]),int(box[0][2]),int(box[0][3])

       # img 256 * 256 * 3 ,numpy的格式 int
       cv2.rectangle(img,
                     (left, top),
                     (left + right-left, top + bottom-top),
                     COLORS[path.split('\\')[-3]],1)

       cv2.putText(img, name_classes[name_classes.index(path.split('\\')[-3])]+'_'+str(0.77), (int(left), int(top)),
                   FONT, 0.41, COLORS[path.split('\\')[-3]], 1, cv2.LINE_AA)

       window_name = 'Object detector'
       cv2.namedWindow(window_name, 0)
       cv2.resizeWindow(window_name, 800, 800)
       imgs = np.hstack([img, png])
       cv2.imshow(window_name,imgs)
       cv2.waitKey()



