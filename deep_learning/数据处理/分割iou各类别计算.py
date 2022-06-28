"""
refer to https://github.com/jfzhang95/pytorch-deeplab-xception/blob/master/utils/metrics.py
"""
import numpy as np
from PIL import Image
import os

__all__ = ['SegmentationMetric']

"""
confusionMetric
P\L     P    N
P      TP    FP
N      FN    TN
"""
name_classes = ["bc", "blj", "dlj", "fzcz", "hkmj", "hqc", "pbc", "qt", "qxyj", "qzj",
                    "xlj", "yc", "yt"]

class SegmentationMetric(object):
    def __init__(self, numClass):
        self.numClass = numClass
        self.confusionMatrix = np.zeros((self.numClass,) * 2)

    def pixelAccuracy(self):
        # return all class overall pixel accuracy
        # acc = (TP + TN) / (TP + TN + FP + TN)
        acc = np.diag(self.confusionMatrix).sum() / self.confusionMatrix.sum()
        return acc

    def classPixelAccuracy(self):
        # return each category pixel accuracy(A more accurate way to call it precision)
        # acc = (TP) / TP + FP
        classAcc = np.diag(self.confusionMatrix) / self.confusionMatrix.sum(axis=1)
        return classAcc

    def meanPixelAccuracy(self):
        classAcc = self.classPixelAccuracy()
        meanAcc = np.nanmean(classAcc)
        return meanAcc

    def meanIntersectionOverUnion(self):
        # Intersection = TP Union = TP + FP + FN
        # IoU = TP / (TP + FP + FN)
        intersection = np.diag(self.confusionMatrix)
        union = np.sum(self.confusionMatrix, axis=1) + np.sum(self.confusionMatrix, axis=0) - np.diag(
            self.confusionMatrix)
        IoU = intersection / union
        mIoU = np.nanmean(IoU)
        return mIoU

    def genConfusionMatrix(self, imgPredict, imgLabel):
        # remove classes from unlabeled pixels in gt image and predict
        mask = (imgLabel >= 0) & (imgLabel < self.numClass)
        label = self.numClass * imgLabel[mask] + imgPredict[mask]
        count = np.bincount(label, minlength=self.numClass ** 2)
        confusionMatrix = count.reshape(self.numClass, self.numClass)
        return confusionMatrix

    def Frequency_Weighted_Intersection_over_Union(self):
        # FWIOU =     [(TP+FN)/(TP+FP+TN+FN)] *[TP / (TP + FP + FN)]
        freq = np.sum(self.confusion_matrix, axis=1) / np.sum(self.confusion_matrix)
        iu = np.diag(self.confusion_matrix) / (
                np.sum(self.confusion_matrix, axis=1) + np.sum(self.confusion_matrix, axis=0) -
                np.diag(self.confusion_matrix))
        FWIoU = (freq[freq > 0] * iu[freq > 0]).sum()
        return FWIoU

    def addBatch(self, imgPredict, imgLabel):
        assert imgPredict.shape == imgLabel.shape
        self.confusionMatrix += self.genConfusionMatrix(imgPredict, imgLabel)

    def reset(self):
        self.confusionMatrix = np.zeros((self.numClass, self.numClass))



if __name__ == '__main__':
    # imgPredict = np.array([0, 0, 1, 1, 2, 2])
    # # imgLabel = np.array([0, 0, 0, 1, 2, 2])
    # imgPredict = Image.open('predict_img/yt_041593.png')
    # imgLabel = Image.open('ground_img/041593.png')
    # pngPredict = np.array(imgPredict)
    # pngLabel = np.array(imgLabel)
    # #
    # if 'yt' in name_classes:
    #     cls_id = name_classes.index('yt')
    #     pngLabel[pngLabel > 0] = cls_id + 1
    #
    # metric = SegmentationMetric(13)
    # metric.addBatch(pngPredict, pngLabel)
    # acc = metric.pixelAccuracy()
    # mIoU = metric.meanIntersectionOverUnion()
    #
    # print(acc, mIoU)

    # pre_img_path ='predict_img'
    # pre_img_list=os.listdir(pre_img_path)
    test_txt_path='C:/Data/test.txt'
    test_image_list=open(test_txt_path, 'r').read().splitlines()

    num_classes=14
    hist = np.zeros((num_classes, num_classes))

    idx=0
    IoU =np.zeros((14))
    mIoU =np.zeros((14))
    leibie_number =np.zeros((14))
    for test_image_name in test_image_list:

        s=test_image_name.split('\\')[-1].split('.')
        pre_image_id = test_image_name.split('\\')[-3]+'_'+ test_image_name.split('\\')[-1].split('.')[0]+'.png'
        pre_img_path = os.path.join('miou_pr_dir',pre_image_id)
        # print(pre_img_path)
        pre_image =np.array(Image.open(pre_img_path))

        "把标签数据集进行处理，每一类对应相应的类别值"
        label_image_path =os.path.join('C:\Data\ship_visiable',test_image_name.split('\\')[-3],'label',test_image_name.split('\\')[-1].split('.')[0]+'.png')
        label_image =np.array(Image.open(label_image_path))
        if test_image_name.split('\\')[-3] in name_classes:
            cls_id = name_classes.index(test_image_name.split('\\')[-3])
            label_image[label_image > 0] = cls_id + 1


        metric = SegmentationMetric(num_classes)
        metric.addBatch(pre_image, label_image)   # 得到对应的预测和标签的混淆矩阵
        if test_image_name.split('\\')[-3] in name_classes:
            leibie_id = name_classes.index(test_image_name.split('\\')[-3])
            leibie_number[leibie_id] +=1
            # print(test_image_name)
            # print(label_image_path)
            # print('{:s}'.format(test_image_name.split('\\')[-3]))
            # print(metric.meanIntersectionOverUnion())
            if  metric.meanIntersectionOverUnion()<0.5:
                print(test_image_name)
            IoU[leibie_id] +=metric.meanIntersectionOverUnion()

    for i in range(num_classes-1):
        mIoU[i] =IoU[i]/leibie_number[i]
        print('{:s}: {:0.2f}'.format(name_classes[i],mIoU[i]))
    print(sum(mIoU)/13)

    print(mIoU)




