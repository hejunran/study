import numpy as np
import torch
from nets.frcnn import FasterRCNN
import cv2
import os
from torchvision.transforms import transforms
from matplotlib import pyplot as plt

"结构性相似矩阵的计算"
def cal_ssim(im1, im2):

    assert len(im1.shape) == 2 and len(im2.shape) == 2
    assert im1.shape == im2.shape
    mu1 = im1.mean()
    mu2 = im2.mean()
    sigma1 = np.sqrt(((im1 - mu1) ** 2).mean())
    sigma2 = np.sqrt(((im2 - mu2) ** 2).mean())
    sigma12 = ((im1 - mu1) * (im2 - mu2)).mean()
    k1, k2, L = 0.01, 0.03, 255
    C1 = (k1 * L) ** 2
    C2 = (k2 * L) ** 2
    C3 = C2 / 2
    l12 = (2 * mu1 * mu2 + C1) / (mu1 ** 2 + mu2 ** 2 + C1)
    c12 = (2 * sigma1 * sigma2 + C2) / (sigma1 ** 2 + sigma2 ** 2 + C2)
    s12 = (sigma12 + C3) / (sigma1 * sigma2 + C3)
    ssim = l12 * c12 * s12

    return ssim


def channel_ssim_matrix(imgs):
    "对于某一层的输出结构的相似性进行计算"
    length = imgs.shape[-1]
    ssim_matrax = torch.zeros((length, length))
    for i in range(imgs.shape[-1]):
        x = f[0, :, :, i]
        for j in range(imgs.shape[-1]):
            y = f[0, :, :, j]
            ssim_matrax[i][j] = cal_ssim(x, y)
    print(ssim_matrax)
    return ssim_matrax

def channel_gray_Hist(imgs):

    # assert imgs.shape==4 or imgs.shape==3    # 输入的是经过卷积处理过的图片 格式为： batch * h *w * channel
    # path = os.path.join(save_path,name)
    img_per_row = 16  # 每行多少张照片 ， 16即为每行16列
    n_cols = imgs.shape[-1] // img_per_row  # 行数 取整数

    for col in range(n_cols):
        for row in range(img_per_row):
            channel_image = imgs[0, :, :, col * img_per_row + row]
            channel_image -= channel_image.mean()
            channel_image /= channel_image.std()
            channel_image *= 64
            channel_image += 128
            channel_image = np.clip(channel_image, 0, 255).astype('uint8')
            "计算每张图的梯度"
            hist1 = cv2.calcHist([channel_image], [0], None, [256], [0, 256])
            # plt.figure(figsize=(100, 100))
            plt.subplot(n_cols, img_per_row, col * img_per_row + row + 1)
            plt.hist(channel_image.ravel(), 256, [0, 256])
            # plt.title('f_%s',str(col * img_per_row + row))

    # plt.savefig('C:/pytorch_study_project/faster_rcnn_bilibili/img/pre_max1_Hist.png')
    plt.show()



if __name__ == '__main__':
    NUM_CLASSES = 13
    IMAGE_SHAPE = [256,256,3]
    BACKBONE = "vgg16"
    model = FasterRCNN(NUM_CLASSES,backbone=BACKBONE)
    # print(model)

    image_path='C:/pytorch_study_project/faster_rcnn_bilibili/img/14.jpg'
    img=cv2.imread(image_path)
    tranf =transforms.ToTensor()
    img_tensor =tranf(img)
    img_batch=img_tensor.unsqueeze(0)

    conv_img =model.extractor.features[:6](img_batch)
    s = conv_img.detach().numpy()
    f=s.transpose((0,2,3,1))        # batch * h * w * channel
    # print(f)

    temp_matrix=channel_ssim_matrix(f)
    file = open("newfile.txt", "w")
    # for i in range(len(temp_matrix)):
    #     matrix = np.zeros((len(temp_matrix), len(temp_matrix)))
    np.savetxt(file, temp_matrix)
    np.savetxt('new.csv', temp_matrix, delimiter = ',')
    file.close()

    "对于某一层的输出结构的相似性进行计算"
    length=f.shape[-1]
    ssim_matrax = torch.zeros((length,length))
    for i in range(f.shape[-1]):
        x = f[0,:,:,i]
        for j in range(f.shape[-1]):
            y=f[0,:,:,j]
            ssim_matrax[i][j]=cal_ssim(x,y)
    print(ssim_matrax)         # 想办法把其输入到文档里面

    channel_gray_Hist(f)


