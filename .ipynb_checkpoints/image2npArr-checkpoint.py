import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

from PIL import Image
pic=Image.open('images/river.png')

##trying with open cv
# import cv2
# img=cv2.imread('../images/apple.jpg',cv2.IMREAD_COLOR)
# cv2.imshow('apple',img)
pic
type(pic)
#convert image to np array
pic_arr=np.array(pic)
type(pic_arr)
pic_arr.shape
pic_arr
pic
pic_red=pic_arr[:,:,0]
plt.imshow(pic_red)
