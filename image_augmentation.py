import os
import numpy as np
import pandas as pd
import imgaug as ia
import cv2
from imgaug import augmenters as iaa
from tqdm.auto import tqdm

# import images into array

df = pd.read_csv('./dataset/train.csv')

images = []

for row in tqdm(df.iterrows()):
    label = row[1][1]
    image_name = row[1][0]
    img = cv2.imread(f'./dataset/image/{image_name}')
    images.append(img)

print(images[0].shape)

print(np.array(images).shape)

# augment images and keep labels


augmentor_rotate = iaa.SomeOf(1, [
    iaa.Affine(rotate=(-180, 180))    
])

augmentor_flip = iaa.SomeOf(1, [
    iaa.Fliplr(1)
])

images_rotate = augmentor_rotate(images=images)
images_flip = augmentor_flip(images=images)


# save images

os.chdir('./dataset')
print(os.getcwd())
try:
    os.makedirs(f'image_aug')
except:
    print('Failed')

labels = []
names = []
for i, row in tqdm(enumerate(df.iterrows())):
    label = row[1][1]
    image_name = row[1][0]
    if label == 'no_tumor':
        labels.append(label)
        labels.append(label)
        names.append('ROTATE_' + image_name)
        names.append('FLIP_'+ image_name)
        cv2.imwrite('./train/ROTATE_' + image_name, images_rotate[i])
        cv2.imwrite('./train/FLIP_' + image_name, images_rotate[i])


df2 = pd.DataFrame([names, labels])
df2 = df2.transpose()

df.columns = ['Name', 'Label']
df2.columns = ['Name', 'Label']
df = df.append(df2, ignore_index=True)


df.to_csv('train.csv', index=False)