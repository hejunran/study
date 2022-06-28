import  os
from PIL import Image
import numpy as np
import xml.etree.ElementTree as ET
import cv2


name_classes = ["bc", "ship", "dlj", "fzcz", "hkmj","hqc","pbc", "qt", "qxyj", "qzj",
                    "xlj", "yc", "yt"]

# 因为保存的图片是cv2模式下保存的，所以次颜色是对应BGR通道的颜色。
COLORS={"bc":(0, 0, 128), "ship":(0, 128, 0), "dlj":(0, 128, 128), "fzcz":(128, 0, 0), "hkmj":(128, 0, 128),
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

def show_xml(root_path):

    img_ids=os.listdir(os.path.join(root_path,'imgs'))

    for img_id in img_ids:
        img_path = os.path.join(root_path,'imgs',img_id)
        xml_path=os.path.join(root_path,'annotations',img_id.split(".")[0]+'.xml')

        image =Image.open(img_path)
        save_path=os.path.join(root_path,'object_view')

        img=cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
        box,label_names = read_xml(xml_path)

        for i in range(len(box)):
            left, top, right, bottom = int(box[i][0]), int(box[i][1]), int(box[i][2]), int(box[i][3])
            cv2.rectangle(img,
                          (left, top),
                          (left + right - left, top + bottom - top),
                          COLORS[label_names[i]], thickness=1)  # thickness表示的是框颜色的粗细。

            FONT = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, '', (int(left), int(top)),
                        FONT, 0.31, COLORS[label_names[i]], 1, cv2.LINE_AA)
            # cv2.putText(img, label_names[i] + '_' + str(0.77), (int(left), int(top)),
            #             FONT, 0.41, COLORS[label_names[i]], 1, cv2.LINE_AA)  # 此处0.77表示的是概率。

        filename = xml_path.split('\\')[-1].split('.')[0] + '.jpg'
        cv2.imwrite(save_path + '/' + filename, img)  # save picture



if __name__ == '__main__':
    source_path = 'E:\choose_small'
    # save_path='D:/python_study/new_data//new'
    show_xml(source_path)