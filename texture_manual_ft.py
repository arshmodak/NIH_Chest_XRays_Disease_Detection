#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 10:52:21 2021

@author: adithyaabhishek
"""

import pyfeats
from features import *
import numpy as np
import os,sys
import cv2

from PIL import Image
xray_features = dict()


path = "/Users/adithyaabhishek/Desktop/FAI5100/nih_cxray/images/"
dirs = os.listdir(path)


for m in dirs:
    if m == '.DS_Store':
        continue
    
    x=Image.open("/Users/adithyaabhishek/Desktop/FAI5100/nih_cxray/images/"+m)
    
    if m in dirs :
        img_array = np.array(x)
        rgb_array = cv2.cvtColor(img_array,cv2.COLOR_GRAY2RGB)
        features_mean, features_range, labels_mean, labels_range = glcm_features(rgb_array)
        xray_features[m] = features_mean
    else:
        continue

print(xray_features) #required texture features via glcm
    



