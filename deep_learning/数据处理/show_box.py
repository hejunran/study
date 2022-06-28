import cv2
import numpy as np
from PIL import Image
import xml.etree.ElementTree as ET

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

sourceDir_xml_path ='D:/python_study/new_data/fzcz/annotation/010051.xml'
image_path = 'D:/python_study/new_data/fzcz/image/010051.jpg'
image = cv2.imread(image_path)
box =read_xml(sourceDir_xml_path)
for bbox in box:
    # bbox = bbox.split(",")
    image = cv2.rectangle(image,(int(float(bbox[0])),
                                 int(float(bbox[1]))),
                                (int(float(bbox[2])),
                                 int(float(bbox[3]))), (255,0,0), 2)

image = Image.fromarray(np.uint8(image))
image.show()