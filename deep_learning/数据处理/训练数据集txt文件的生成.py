import os
import random
import xml.etree.ElementTree as ET
from os import getcwd

segfilepath=r'C:/Data/process_ship'
saveBasePath=r"C:/Data/Text"

sets = ['seg_dect_train', 'seg_dect_val', 'seg_dect_test']

classes = ["bc", "blj", "dlj", "fzcz", "hkmj", "qt", "qxyj", "qzj", "xlj", "yc", "yt"]

def convert_annotation(name_file,path_annotation, list_file):

    img_id=name_file.split('\\')[-1].split('.')[0]+'.xml'
    temp_ship_annotation_path=os.path.join(path_annotation,img_id)
    in_file = open( temp_ship_annotation_path,encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = 0
        if obj.find('difficult') != None:
            difficult = obj.find('difficult').text

        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(float(xmlbox.find('xmin').text)), int(float(xmlbox.find('ymin').text)),
             int(float(xmlbox.find('xmax').text)), int(float(xmlbox.find('ymax').text)))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))



ftrainval = open(os.path.join(saveBasePath,'trainval.txt'), 'w')
ftest = open(os.path.join(saveBasePath,'test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath,'train.txt'), 'w')
fval = open(os.path.join(saveBasePath,'val.txt'), 'w')


ship_folders=os.listdir(segfilepath)
for temp_ship_folder in ship_folders:
   path_img =os.path.join(segfilepath,temp_ship_folder,'image')
   path_annotation=os.path.join(segfilepath,temp_ship_folder,'annotation')
   temp_jpg = os.listdir(path_img)

   trainval_percent = 0.8
   train_percent = 0.9




    temp_total_jpg=[]
   for jpg in temp_jpg:
       temp_total_jpg.append(jpg)

   num = len(temp_total_jpg)
   list = range(num)
   # print(list)
   tv = int(num * trainval_percent)
   tr = int(tv * train_percent)
   trainval = random.sample(list, tv)
   train = random.sample(trainval, tr)

   for i in list:
       name = temp_total_jpg[i]

       name_file = os.path.join(path_img, name)

       if i in trainval:
           ftrainval.write(name_file)
           # convert_annotation(name_file,path_annotation,ftrainval)
           ftrainval.write("\n")
           if i in train:
               ftrain.write(name_file)
               # convert_annotation(name_file, path_annotation, ftrainval)
               ftrain.write("\n")
           else:
               fval.write(name_file)
               # convert_annotation(name_file, path_annotation, ftrainval)
               fval.write("\n")
       else:
           ftest.write(name_file)
           ftest.write("\n")
           # convert_annotation(name_file, path_annotation, ftrainval)


ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

list_file = open('C:/Data/Text/seg_dect_train.txt', 'w')
with open(os.path.join(saveBasePath,'train.txt')) as f:
    lines =f.readlines()
    for line in lines:
        s=line.split()[0]
        list_file.write('%s' % (s))
        path_annotation=os.path.join(segfilepath, line.split('\\')[-3],'annotation')
        convert_annotation(line,path_annotation,list_file)
        list_file.write('\n')

list_file.close()


list_file = open('C:/Data/Text/seg_dect_val.txt', 'w')
with open(os.path.join(saveBasePath,'val.txt')) as f:
    lines =f.readlines()
    for line in lines:
        s=line.split()[0]
        list_file.write('%s' % (s))
        path_annotation=os.path.join(segfilepath, line.split('\\')[-3],'annotation')
        convert_annotation(line,path_annotation,list_file)
        list_file.write('\n')

list_file.close()

list_file = open('C:/Data/Text/seg_dect_test.txt', 'w')
with open(os.path.join(saveBasePath,'test.txt')) as f:
    lines =f.readlines()
    for line in lines:
        s=line.split()[0]
        list_file.write('%s' % (s))
        path_annotation=os.path.join(segfilepath, line.split('\\')[-3],'annotation')
        convert_annotation(line,path_annotation,list_file)
        list_file.write('\n')

list_file.close()

list_file = open('C:/Data/Text/seg_dect_trainval.txt', 'w')
with open(os.path.join(saveBasePath,'trainval.txt')) as f:
    lines =f.readlines()
    for line in lines:
        s=line.split()[0]
        list_file.write('%s' % (s))
        path_annotation=os.path.join(segfilepath, line.split('\\')[-3],'annotation')
        convert_annotation(line,path_annotation,list_file)
        list_file.write('\n')

list_file.close()