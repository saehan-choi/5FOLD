import os
from tqdm import tqdm

path1 = r'./FOLD/FOLD1/train'
path2 = r'./FOLD/FOLD2/train'

path1_list = os.listdir(path1)
path2_list = os.listdir(path2)

dup = []

for file in path2_list:
    if file in path1_list:
        dup.append(file)

print(f'{len(dup)} file is dup.')
for file in dup:
    print(file)
