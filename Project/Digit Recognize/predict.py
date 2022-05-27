from ast import Global
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image,ImageOps
from os import listdir
from os.path import isfile, join
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import RandomizedSearchCV
import cv2
def train():
    zero = ['0_0','0_1','0_2','0_3']
    one = ['1_0','1_1','1_2','1_3']
    two = ['2_0','2_1','2_2','2_3']
    three = ['3_0','3_1','3_2','3_3']
    four = ['4_0','4_1','4_2','4_3']
    five = ['5_0','5_1','5_2','5_3']
    six = ['6_0','6_1','6_2','6_3']
    seven = ['7_0','7_1','7_2','7_3']
    eight = ['8_0','8_1','8_2','8_3']
    nine = ['9_0','9_1','9_2','9_3']

    folder = listdir('own_dataset')
    y = []
    count = 0
    for dir in  folder:
        f = listdir('own_dataset/'+dir)
        length = len(f)
        for name in f:
            img = Image.open('own_dataset/'+dir+'/'+name).convert('L')
            # img = ImageOps.invert(img)
            img = np.array(img.resize((8,8),Image.ANTIALIAS))
            pixel = img/255*16
            pixel.astype('int')
            digit_1_001 = pixel.reshape(1,-1)[0]
            if count == 0:
                df = pd.DataFrame([digit_1_001])
                count = 1
            else:
                df  = df.append([digit_1_001],ignore_index=True)
            if dir in zero:
                y.append(0)
            elif dir in one:
                y.append(1)
            elif dir in two:
                y.append(2)
            elif dir in three:
                y.append(3)
            elif dir in four:
                y.append(4)
            elif dir in five:
                y.append(5)
            elif dir in six:
                y.append(6)
            elif dir in seven:
                y.append(7)
            elif dir in eight:
                y.append(8)
            elif dir in nine:
                y.append(9)
            
    X = df
    y = np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
    param = {
        'warm_start': [False], 'solver': ['lbfgs'], 'shuffle': [False], 'random_state': [42], 'nesterovs_momentum': [False], 'max_iter': [500], 'learning_rate_init': [1e-05], 'learning_rate': ['invscaling'], 'hidden_layer_sizes': [(208, 208)], 'early_stopping': [True], 'alpha': [1e-07], 'activation': ['relu']

    }
    gsv = RandomizedSearchCV(MLPClassifier(),param,verbose=1,cv=5,n_jobs=-1)
    return gsv.fit(X_train,y_train)
