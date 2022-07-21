import os

def Rename_list(namelist, img_path, label_path):
    for idx, n in enumerate(namelist):
        imgList = img_path+n
        labelList = label_path+n[:-3]+'txt'

        os.rename(imgList, img_path+str(idx)+'.jpg')
        os.rename(labelList, label_path+str(idx)+'.txt')