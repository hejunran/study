import os
import torch
# import pyyaml
import yaml


def write_yaml(source_path,save_path):

    files_names =os.listdir(source_path)
    for i in files_names:
        yaml_name =os.path.join(save_path,i.split('.')[0]+'.yaml')
        # print(yaml.dump(dict={'label_names':'-_background_'}))
        with open(yaml_name, 'w') as f:
            yaml.dump(dict(label_names=['_background_', source_path.split('/')[-2]]), f)


if __name__ == '__main__':
    source_path='D:/python_study/new_data/yt/image'
    save_path ='D:/MNC_Study/mask-rcnn-keras-master/train_dataset/ymal'
    write_yaml(source_path,save_path)
    # i ='bc'
    # print(yaml.dump(dict(label_names=['_background_',i])))
    # with open('1.ymal','w') as f:
    #     yaml.dump(dict(label_names=['_background_',i]),f)