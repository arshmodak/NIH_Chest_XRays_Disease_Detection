#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 17:26:40 2021

@author: adithyaabhishek
"""

from PIL import Image, ImageOps
import os, sys
import cv2
import numpy as np
import pywt
import pywt.data
import matplotlib.pyplot as plt
import cv2

img = Image.open("/Users/adithyaabhishek/Desktop/FAI5100/nih_cxray/resized/00000001_000.png")
img_array = np.array(img) 
"""rgb_array = cv2.cvtColor(img_array,cv2.COLOR_GRAY2RGB)
rimg = Image.fromarray(rgb_array)
print(rgb_array)"""

coef = pywt.wavedec2(img, 'db1' , level=4) # level3 decomposition #use db1 or haar

cA = coef[0]
(cH1,cV1,cD1) =  coef[-1]#level1
(cH2,cV2,cD2) =  coef[-2]#level2
(cH3,cV3,cD3) =  coef[-3]#level3
(cH4,cV4,cD4) =  coef[-4]#level4 output of level4 decomp and furthur level dont offer better features

plt.Figure(figsize=(20,20))

plt.subplot(2,2, 1)
plt.imshow(cA, cmap=plt.cm.gray)
plt.title('Approximation',fontsize=30)

plt.subplot(2, 2, 2)
plt.imshow(cH4, cmap=plt.cm.gray)
plt.title(' Horizontal ',fontsize=30)

plt.subplot(2,2, 3)
plt.imshow(cV4, cmap=plt.cm.gray)
plt.title('Vertical ',fontsize=30)

plt.subplot(2,2, 4)
plt.imshow(cD4, cmap=plt.cm.gray)
plt.title( 'Diagonal ',fontsize=30)