import torch
import  os
from PIL import Image
import numpy as np
import xml.etree.ElementTree as ET
import cv2

# 此处的颜色是根据P模式下调色板的颜色进行的转换。
name_classes = ["bc", "blj", "dlj", "fzcz", "hkmj","hqc","pbc", "qt", "qxyj", "qzj",
                    "xlj", "yc", "yt"]

# 因为保存的图片是cv2模式下保存的，所以次颜色是对应BGR通道的颜色。
COLORS={"bc":(0, 0, 128), "blj":(0, 128, 0), "dlj":(0, 128, 128), "fzcz":(128, 0, 0), "hkmj":(128, 0, 128),
        "hqc":(128, 128, 0),"pbc":(128, 128, 128),"qt":(0, 0, 64), "qxyj":(0, 0, 192), "qzj":(0, 128, 64),
        "xlj":(0, 128, 192),"yc":(128, 0, 64), "yt":(128, 0, 192)}


def read_xml(xml_path):
    etree = ET.parse(xml_path)
    root = etree.getroot()
    box = []
    names=[]
    for obj in root.iter('object'):
        xmin,ymin,xmax,ymax = (x.text for x in obj.find('bndbox'))
        box.append([xmin,ymin,xmax,ymax])
        names.append(obj.find('name').text)
    print (len(box))

    return box,names

def show_label(image_path,png_path):
    image = Image.open(image_path).convert('RGB')
    png = Image.open(png_path).convert('RGB')
    image = Image.blend(png,image,0.5)
    # image.show()

    return image

def show_xml(image,xml_path,save_path):

    img=cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
    box,label_names = read_xml(xml_path)

    for i in range(len(box)):
        left, top, right, bottom = int(box[i][0]), int(box[i][1]), int(box[i][2]), int(box[i][3])
        cv2.rectangle(img,
                    (left, top),
                    (left + right - left, top + bottom - top),
                    COLORS[label_names[i]], thickness=2)       # thickness表示的是框颜色的粗细。

        FONT = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, label_names[i] + '_' + str(0.77), (int(left), int(top)),
                    FONT, 0.41, COLORS[label_names[i]], 1, cv2.LINE_AA)    # 此处0.77表示的是概率。


    filename = xml_path.split('\\')[-1].split('.')[0]+'.jpg'
    cv2.imwrite(save_path + '/' + filename, img)  # save picture
    # cv2.imshow("OpenCV",img)
    # cv2.waitKey()


def show_png_xml(soource_dir):

    for i in os.listdir(soource_dir):
        image_files = os.path.join(soource_dir,i,'image')
        for j in os.listdir(image_files):
            image_path = os.path.join(image_files,j)
            png_path = os.path.join(soource_dir, i, 'png',j.split('.')[0]+'.png')
            xml_path = os.path.join(soource_dir, i, 'annotation',j.split('.')[0]+'.xml')
            image = show_label(image_path=image_path,png_path=png_path)
            save_path = os.path.join(soource_dir,i,'new')
            show_xml(image=image,xml_path=xml_path,save_path=save_path)


if __name__ == '__main__':
    source_path ='D:/python_study/new_data'
    # save_path='D:/python_study/new_data//new'
    show_png_xml(source_path)