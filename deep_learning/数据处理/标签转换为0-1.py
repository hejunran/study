import torch
import os
import numpy as np
from PIL import Image

name_classes = ["bc", "blj", "dlj", "fzcz", "hkmj", "hqc","pbc","qt", "qxyj", "qzj",
                    "xlj", "yc", "yt"]

def png_transform(source_png_path,save_png_path):
    orignal_png =Image.open(source_png_path)
    orignal_png = orignal_png

    orignal_png = np.array(orignal_png)
    if source_png_path.split('\\')[-3] in name_classes:
        cls_id = name_classes.index(source_png_path.split('\\')[-3])
        orignal_png[orignal_png > 0] = cls_id + 1
    orignal_png = Image.fromarray(orignal_png)
    orignal_png.save(save_png_path)

def read_png_path(root):
    png_files = os.listdir(root)
    for i in png_files:
        for j in os.listdir(os.path.join(root,i,'png')):
            source_png_path = os.path.join(root,i,'png',j)
            save_png_path = os.path.join(root,i,'label0-1',j)
            png_transform(source_png_path=source_png_path,save_png_path=save_png_path)

if __name__ == '__main__':
    root ='D:/python_study/new_data'
    read_png_path(root=root)




