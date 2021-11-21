import os
from numpy.random import RandomState
import pandas as pd
from shutil import copy2

# getting path to data
path = os.getcwd()
dataset_path = os.path.join(path, 'dataset')
data_path = os.path.join(path, 'dataset/label.csv')

df = pd.read_csv(os.path.join(path, 'dataset/label.csv'))

# creating test and train directories
try:
    os.mkdir(os.path.join(dataset_path, 'train'))
    os.mkdir(os.path.join(dataset_path, 'test'))
except:
    pass

# splitting dataset into train and test
rng = RandomState()
train = df.sample(frac=0.7, random_state=rng)
test = df.loc[~df.index.isin(train.index)]

# creating csv file for each and putting images in correct folder
train.to_csv(os.path.join(dataset_path, 'train.csv'))
test.to_csv(os.path.join(dataset_path, 'test.csv'))

for row in train.iterrows():
    image_path = os.path.join(dataset_path, f'image/{row[1][0]}')
    copy2(image_path, os.path.join(dataset_path, 'train'))

for row in test.iterrows():
    image_path = os.path.join(dataset_path, f'image/{row[1][0]}')
    copy2(image_path, os.path.join(dataset_path, 'test'))