
import os
import random
import shutil

img_path = './images/'
label_path = './labels/'
FOLD_path = './FOLD/'

each_fold_outpath = './FOLD/FOLD'

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
    

for idx in range(0, FOLD_num*2, 2):
    # os.makedirs(each_fold_outpath+str(idx+1)+'/train')
    train_fold_list = all_list.copy()
    # for d in idx:
    #     del train_fold_list[d]
    print(train_fold_list)
    for d in range(2):
        del train_fold_list[idx]
    
    # print('\n')
    # print(train_fold_list)
    # print('\n')
    
    
    # shutil.copy2(path, each_fold_outpath+str(idx+1)+'/train')