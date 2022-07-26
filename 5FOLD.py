import os
import random
import shutil

from glob import glob
# you only need to edit it here 
img_path = './images/'
label_path = './labels/'
FOLD_path = './FOLD/'


# you can revise folder name ex) FOLD1 FOLD2 FOLD3 FOLD4 FOLD5
each_fold_outpath = FOLD_path+'FOLD'

# you can accese only 5FOLD
FOLD_num = 5

# images and labels name must have to have same names
nameList = os.listdir(img_path)
random.shuffle(nameList)

img_path_List = []
label_path_List = []

all_list = []

# make same labels
for n in nameList:
    imgList = img_path+n
    labelList = label_path+n[:-3]+'txt'
    img_path_List.append(imgList)
    label_path_List.append(labelList)

os.makedirs(FOLD_path, exist_ok=True)
eachFOLD = len(img_path_List)//FOLD_num

for idx, f in enumerate(range(0, len(img_path_List), eachFOLD)):
    all_list.append(img_path_List[f:f+eachFOLD])
    all_list.append(label_path_List[f:f+eachFOLD])
    os.makedirs(each_fold_outpath+str(idx+1), exist_ok=True)

for idx, fold in enumerate(range(0, FOLD_num*2, 2)):
    for path in all_list[fold]:
        os.makedirs(each_fold_outpath+str(idx+1)+'/val', exist_ok=True)
        shutil.copy2(path, each_fold_outpath+str(idx+1)+'/val')
    
for idx, fold in enumerate(range(1, FOLD_num*2, 2)):
    for path in all_list[fold]:
        os.makedirs(each_fold_outpath+str(idx+1)+'/val', exist_ok=True)
        shutil.copy2(path, each_fold_outpath+str(idx+1)+'/val')
    
for idx in range(FOLD_num):
    train_fold_list = all_list.copy()
    
    os.makedirs(each_fold_outpath+str(idx+1)+'/train', exist_ok=True)
    
    # delete same label (train/val)
    for d in range(2):
        del train_fold_list[idx*2]
    
    for fold_list in train_fold_list:
        for list in fold_list:
            shutil.copy2(list, each_fold_outpath+str(idx+1)+'/train')


# make images / labels
# if you don't use, files will don't devide images/labels partially
for fold in glob(FOLD_path+'*'):
    for endpath in glob(fold+'/*'):
        os.makedirs(endpath+'/images', exist_ok=True)
        os.makedirs(endpath+'/labels', exist_ok=True)
        
        for imgpath in glob(endpath+'/*.jpg'):
            shutil.move(imgpath, endpath+"/images/"+imgpath.split('\\')[-1])
        for labelpath in glob(endpath+'/*.txt'):
            shutil.move(labelpath, endpath+"/labels/"+labelpath.split('\\')[-1])