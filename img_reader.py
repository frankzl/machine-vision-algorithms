from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

def read_img(path):
    """
    returns a numpy array containing the image
    """
    return misc.imread(path)

def show_img(img):
    plt.imshow(img, cmap=plt.cm.gray)
    plt.show()
    return

    
def rgb2gray(rgb):
    return np.dot(rgb, [0.299, 0.587, 0.114])

def read_gray(path):
    return rgb2gray(misc.imread(path))